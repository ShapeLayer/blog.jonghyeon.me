---
layout: post
title: 클라이언트-서버 모델
date: '2026-01-06'
category: [network]
---

_사가대학 〈네트워크시스템〉 과목 성적 평가 리포트 제출물_  

[(ko) 제출분의 한국어 원본](#) | [(ja) 제출본](#)

> ネットワークの通信モデルである「クライアントサーバモデル」と 「P2Pモデル」について利点・欠点などともに A4 1～2 ページ程度でまとめなさい。  
> 네트워크 통신 모델인 '클라이언트 서버 모델'과 'P2P 모델'에 대하여 장단점 등을 포함해 A4 용지 1~2매 정도로 정리하시오.  

## 도입

클라이언트-서버 모델은 인터넷 서비스 대부분이 채택하여 가장 보편화된 네트워크 시스템의 구조이다. 이 모델에서는 서비스를 요청하는 프로그램인 '클라이언트'와 그 요청에 응답하는 프로그램인 '서버'가 역할을 분담하여 협업한다. [^1] [^2] 

디스플레이 프로토콜인 Wayland의 경우[^3], 그리고 게임 Minecraft의 MOD 로더에서의 싱글플레이 모드의 구현 구조[^4]와 같이 이 모델은 단일 컴퓨터 내부의 프로세스 간 통신에서도 활용될 수 있지만, 일반적으로는 네트워크를 통해 서로 다른 위치에 분산되어 있는 프로그램들을 연결하여 효율적인 컴퓨팅 환경을 구축하는 데 그 목적이 있다.

클라이언트는 사용자의 장치에서 실행되며 필요한 서비스나 데이터를 서버에 요청하는 역할을 수행한다. 우리가 일상적으로 사용하는 노트북, 스마트폰, 데스크톱 컴퓨터 등이 모두 클라이언트의 범주에 속한다. 서버-클라이언트 모델의 가장 일반화된 사례, 웹 브라우저를 통해 특정 사이트에 접속하는 행위 자체가 클라이언트가 서버에 요청을 보내는 과정이다.

반면 서버는 이러한 클라이언트의 요청을 받아들여 적절한 처리를 수행하고 그 결과를 다시 돌려주는 역할을 한다. 일반적으로 서버는 개인용 장치보다 훨씬 강력한 성능과 안정성을 갖추고 있으며, 전용 관리 환경에서 24시간 가동되어 여러 클라이언트의 요청을 동시에 처리할 수 있도록 설계된다.  

<br />

웹 개발 분야에서는 이를 '클라이언트 측(Client-side)'과 '서버 측(Server-side)'이라는 용어로 구분하여 설명하기도 한다.

클라이언트 측은 사용자의 브라우저 내에서 일어나는 모든 일을 의미한다. HTML이나 CSS, JavaScript와 같은 언어를 통해 화면을 구성하고 사용자의 입력에 즉각적으로 반응하는 역할을 한다. 반면 서버 측은 데이터베이스와의 상호작용, 사용자 인증, 푸시 알림 등 보안과 데이터 무결성이 중요한 핵심 프로세스를 담당한다.

## 클라이언트-서버 모델의 장점

클라이언트-서버 모델이 가진 가장 큰 장점은 자원 관리, 보안의 중앙 집중화다. 모든 데이터와 핵심 비즈니스 로직이 서버라는 중앙 장치에 집약되어 있기 때문에, 관리자는 데이터의 무결성을 유지하고 보안 정책을 일괄적으로 적용하기가 매우 용이하다.  

예를 들어, 수만 명의 사용자가 이용하는 서비스에서 소프트웨어 업데이트나 보안 패치가 필요할 때, 개별 클라이언트의 기기를 일일이 수정할 필요 없이 서버 측의 코드만 변경하면 모든 사용자에게 반영될 수 있다.

또한, 고성능 하드웨어를 갖춘 서버가 복잡한 연산과 대규모 데이터 처리를 전담함으로써, 상대적으로 성능이 낮은 스마트폰이나 저사양 PC에서도 고도화된 애플리케이션을 원활하게 구동할 수 있게 한다. 이는 시스템의 확장성(Scalability) 측면에서도 유리하여, 사용자가 증가함에 따라 서버의 성능을 높이거나(Scale-up) 서버의 대수를 늘리는(Scale-out) 방식으로 유연하게 대응할 수 있게 한다. [^5] [^6]


## 단일 장애점의 형성

반면, 이러한 중앙 집중식 구조는 단일 장애점(single point of failure)이 되기도 한다. 모든 서비스가 중앙 서버를 통해 이루어지기 때문에, 만약 서버에 하드웨어 결함이 발생하거나 네트워크 장애, 혹은 사이버 공격으로 인해 서버가 가동 중단될 경우, 해당 서버에 연결된 모든 클라이언트는 서비스를 이용할 수 없는 마비 상태에 빠지게 된다. [^7] 이러한 단일 장애점과 관련하여, 비대한 규모의 단일 장애점이 전 세계 인터넷에 끼치는 영향의 실제 사례로 최근 수 주 사이에 발생한 두 건의 Cloudflare 장애가 있었다. Cloudflare의 장애와 이 장애에서 연쇄 다발한 다른 장애들은 단순 클라이언트-서버 구조의 문제는 아니지만, 클라이언트-서버 모델이 가지고 있는 단일 장애점 문제와 동일했다. 이 장애로 인해 전 세계 인터넷 서비스 상당수가 일시적으로 마비되었으며, 이로 인해 많은 사용자와 기업이 큰 불편을 겪었다. [^8] [^9] [^10]

비용과 복잡성 측면에서도 문제가 있다. 다수의 클라이언트 요청을 안정적으로 처리하기 위해서는 고성능 서버 장비와 이를 운영하기 위한 전용 데이터 센터, 냉각 시설, 그리고 이를 관리할 전문 인력이 필요하여, 구축 비용과 유지 보수 비용 상승의 원인이 된다.  

특정 시간에 사용자가 일시적으로 몰리게 되면 서버에 과부하가 걸려 응답 지연이나 서비스 거부 상태가 발생할 수도 있다. 이러한 문제를 해결하기 위해 부하 분산(Load Balancing)이나 캐싱 기술 등이 도입되기도 하지만, 이는 다시 시스템 전체의 아키텍처를 복잡하게 만드는 요인이 된다. 이러한 시스템 복잡도의 증가는 현대에 와서는 아키텍트(Architect) 직군이 생김과 더불어 "Microsoft Certified: Azure Solutions Architect Expert"[^11], "AWS Certified Solutions Architect"[^12] 등의 전문 자격증 까지 등장하게 하는 배경이 되었다.  

이들 단점도 네트워크 인프라를 전제하여 논의할 수 있는 내용이나, 이 모델은 네트워크 인프라 자체에 대한 높은 의존성이 있어 네트워크 장애가 시스템 전체의 실패로 이어질 수 있음 역시 간과할 수 없다. 클라이언트와 서버 간의 통신은 전적으로 네트워크 상태에 의존하므로, 연결이 불안정하거나 대역폭이 좁을 경우 서비스 응답 속도가 급격히 저하되어 서비스 실패로 이어질 수 있다.  

## References

[^1]: Cloudflare, "What do client side and server side mean?." [Online]. Available: https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/

[^2]: IBM, "The client/server model." [Online]. Available: https://www.ibm.com/docs/en/cics-ts/6.x?topic=interfaces-clientserver-model

[^3]: Kristian Høgsberg, "The Wayland Protocol." [Online]. Available: https://wayland.freedesktop.org/docs/html/

[^4]: FabricMC, "Networking." [Online]. Available: https://wiki.fabricmc.net/tutorial:networking

[^5]: Microsoft, "スケールアップとスケールアウトの違い." [Online]. Available: https://azure.microsoft.com/ja-jp/resources/cloud-computing-dictionary/scaling-out-vs-scaling-up

[^6]: Amazon AWS, "What is Amazon EC2 Auto Scaling?." [Online]. Available: https://docs.aws.amazon.com/en_us/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

[^7]: IBM, "What is a single point of failure?." [Online]. Available: https://www.ibm.com/docs/en/zos/3.1.0?topic=data-what-is-single-point-failure

[^8]: Matthew Prince, "Cloudflare outage on November 18, 2025." [Online]. Available: https://blog.cloudflare.com/18-november-2025-outage/

[^9]: Dane Knecht, "Cloudflare outage on December 5, 2025." [Online]. Available: https://blog.cloudflare.com/5-december-2025-outage/

[^10]: 코딩애플, "ChatGPT を爆破させたクラウドフレア(ChatGPT를 폭파시킨 클라우드 플레어)." [Online]. Available: https://www.youtube.com/shorts/srdf56tlOW8

[^11]: Microsoft, "Microsoft Certified: Azure Solutions Architect Expert." [Online]. Available: https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/

[^12]: Amazon AWS, "AWS Certified Solutions Architect - Associate." [Online]. Available: https://aws.amazon.com/certification/certified-solutions-architect-associate/
