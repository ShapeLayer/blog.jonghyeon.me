---
layout: post
title: '클라우드플레어 운용사례: 알려진 포트를 사용하지 않으면서 Full (Strict)모드로 SSL 프록시'
date: '2026-09-17'
category: [infra]
---


## 배경

단일한 공인 IP만을 가지고 있는 네트워크에서 외부 세계에 여러개 서버를 노출시켜야 한다면, 사람에 따라서 조금씩 다른 나름대로의 답안을 만들 수 있을 것이다. 

나는 이전에는 웹서버에 한정하여 모든 HTTP/HTTPS 트래픽을 단일 서버로 포워딩한 후, Nginx를 사용해 트래픽이 요청하는 도메인 이름을 조건문으로 분기하여, 리버스 프록시하는 방법을 사용했다. 하지만 이 방법은 마땅히 추천할 수 있다고 하기에는 무리가 있다.

![리버스 프록시로 운용했을 때의 트래픽 이동(녹색)](/static/posts/2026-09-17-cloudflare-ssl-full/topology.png)  

_리버스 프록시로 운용했을 때의 트래픽 이동(녹색)_

<br />

모든 트래픽이 리버스 프록시를 처리하는 컴퓨터를 거쳐야 해, 부하 측면이나 보안 측면에서 이 관문 컴퓨터를 더욱 신경써서 관리해야했다. 모든 INCOMING 트래픽이 한 곳에 집중된다는 것은 로드 밸런싱 관점에서는 바람직하지 않다. 심지어 홈 서버에서는 이 관문 컴퓨터도 몇 개 서버 호스트로 사용되고 있으므로, 더욱이 바람직하지 않다. 그래서 한 번은 게이트웨이 역할을 하고 있는 공유기에 OpenWRT를 플래시하고 공유기에서 리버스 프록시하기도 했는데, 공유기에서 Nginx 프로세스를 처리하는 것이 적절하지는 않은 것 같아 머지않아 원래대로 되돌렸다.

또한 AI 이전에는 트래픽을 리버스 프록시하고 내부 네트워크에서 리버스 프록시한 트래픽을 암호화하도록 설정하는 과정에서 계속해서 시행착오를 겪으며 시간 소모적인 상황이 많이 발생하게 되어, 로컬호스트로 리버스 프록시하는 트래픽 등에는 암호화하지 않게 되기도 했다. (로컬호스트 역시 트래픽이 캡쳐될 수 있으므로 암호화해야하지만, 이 경우에는 네트워크 내부에 개인 PC와 홈서버, Wi-Fi 공유기만 연결되어있었으므로, ‘공격하면 어떻게 할건데’ 마인드로 방치하곤 했다.)

## 클라우드플레어를 적극 사용하기

최근에 원래의 방법 대신 새 방법을 사용해보고 있다. DNS 레코드 관리용으로만 사용하고 있던 클라우드플레어(CF)를 적극 사용하는 것이다.

1. 홈 게이트웨이에서 비표준 포트를 외부 세계에 노출, 서버 프로세스에 포트포워딩 설정
2. Cloudflare DNS에서 서비스용 서브도메인을 프록싱 상태로 설정
3. Origin Rule에서 해당 서브도메인의 목적지 포트를 홈 게이트웨이에 개방한 포트로 재정의
4. Configuration Rule에서 해당 서브도메인의 SSL 모드를 Full (Strict)로 지정
5. Cloudflare Origin CA 인증서를 발급해 오리진 웹 서버에 설치

리버스 프록시를 사용했을 때는 사용자가 포트가 생략된 일반적인 URL로 접속하게 하기 위해서, 항상 홈 게이트웨이가 80/443 포트를 개방하도록 해야했다. 하지만 Origin Rule로 목적지 포트를 재정의하면 프록시된 DNS 레코드에 들어온 요청을 다른 오리진 포트로 전달할 수 있다. ([Cloudflare Origin Rules](https://developers.cloudflare.com/rules/origin-rules/), [Origin Rule의 목적지 포트 설정](https://developers.cloudflare.com/rules/origin-rules/features/))

DNS에서 클라우드 플레어의 프록시 설정을 활성화해두면, 사용자는 항상 클라우드 플레어와 응답을 주고받고, 클라우드 플레어는 오리진과 응답을 주고받는다. 

```
사용자 ── HTTPS ── Cloudflare ── HTTP(S) ── Origin
```

첫 번째 연결에서는 클라우드플레어가 공개 인증서를 제시한다. 여기서의 HTTPS 연결은 그 뒤의 오리진 연결이 HTTPS를 지원하는지 여부와 관계 없이 성립되기 때문에, 이전에 설정에 따라서는 전체 통신 구간이 안전하지 않음에도 안전한 것처럼 보이게 한다며 문제제기된 적이 있었다. ([#](https://www.evilsocket.net/2016/01/28/Why-you-shouldn-t-trust-CloudFlare-s-Flexible-SSL-and-how-to-bypass-it-with-BetterCap/))

문제가 되는 클라우드플레어-오리진 구간의 연결을 안전하게 만들려면, Cloudflare Origin CA 인증서를 발급해 Origin 측에서 제시하도록 하면 된다. ([Full (Strict) 모드](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/), [Cloudflare Origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/))

이 구성을 사용하면 홈 게이트웨이의 외부 80/443 포트를 반드시 홈 서버에 전달할 필요는 없다. 사용자의 80/443 요청은 먼저 Cloudflare에 도달하고, Cloudflare가 Origin Rule에 지정된 별도 포트로 홈 서버에 새 연결을 만들기 때문이다.

## 여러 홈 서버 서비스의 분기

이 작업의 목적인데, 이렇게 하여 여러 서비스를 하나의 공인 IP에서 운영할 수 있다.

```
golf.example.com  → 공인 IP:11443 → 서버 A:443
git.example.com   → 공인 IP:22443 → 서버 B:443
media.example.com → 공인 IP:33443 → 서버 C:443
```

사용자는 모두 표준 HTTPS 443으로 클라우드플레어에 접속한다. 클라우드플레어는 요청의 호스트 이름을 기준으로 Origin Rule을 적용하고, 각 서비스에 대응하는 목적지 포트로 연결한다. 이 구조에서는 트래픽 분기가 홈 네트워크의 리버스 프록시가 아니라 클라우드플레어의 엣지에서 이루어진다.

또한 이렇게하여 외부 HTTP 트래픽 정책을 클라우드플레어에 중앙화할 수 있다. TLS 종료, HTTP→HTTPS 리다이렉트, WAF, 요청 필터링, 속도 제한과 호스트별 오리진 선택을 하나의 규칙 계층에서 관리할 수 있다.
