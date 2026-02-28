---
layout: post
title: "AI가 자원봉사자들에게 가하는 부담: arXiv의 CS 카테고리 중재 관행 업데이트와 FFmpeg의 입장 발표를 중심으로"
date: '2025-11-19'
categories:
tags: [paper]
---

## 배경

이제 arXiv CS(컴퓨터 과학) 카테고리에 리뷰 논문, 서베이 논문, 입장문은 arXiv에 투고하려면 저널이나 학회에 채택되고 동료 심사를 통과해야 한다. 제출 시 동료 심사 자료가 없다면 arXiv에서는 논문을 거부할 수 있다.  

## arXiv의 관행 업데이트
[Attention Authors: Updated Practice for Review Articles and Position Papers in arXiv CS Category](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category)

### arXiv에서 리뷰 논문, 서베이 논문, 입장문에 대한 기존 관행

arXiv 정책에서 리뷰 논문, 서베이 논문, 입장문은 예나 지금이나 허용되는 콘텐츠 유형 목록에 포함되어있지 않았다.  

과거 arXiv CS는 비교적 적은 양의 리뷰, 서베이 논문을 받았고, 이들 논문은 Annual Reviews, Proceddings of the IEEE, Computing Surveys와 같은 출판물의 요청에 따라 선임 연구원이 작성한 품질 높은 논문들이었다. 입장문도 비슷한 수준에서 드물게 제출되었고, 일반적으로 과학 학회, 정부 연구 기관 등이 작성한 것이었다.  

arXiv에서 공식적으로 허용하는 콘텐츠 유형이 아니었음에도 이러한 자료를 수락한 것은, 이러한 논문들이 높은 품질을 보여주었고 독자와 과학계에 가치를 제공했기 때문에 중재자 재량을 발휘한 것일 뿐이었다.

### LLM의 등장과 상황 변화

그럼에도 불구하고 CS 카테고리의 리뷰, 서베이, 입장문에 대해 명시적인 업데이트를 발표한 것에는, AI와 LLM에 의해 작성된 논문이 CS 카테고리에서 두드러지게 급증한 데에 배경이 있다. 모든 카테고리에서 전반적으로 제출량이 증가했지만, CS 카테고리는 arXiv 팀의 검토 역량을 상회하는 수준으로 제출되고 있다.  

이제 매달 수백 건의 리뷰 논문이 arXiv CS에 제출되고 있고, 대부분의 리뷰 논문은 연구 문제에 대한 실질적인 논의 없이 주석이 달린 참고문헌 목록에 불과했다.

arXiv 자원봉사 중재자들은 이러한 논문 수백 건을 검토할 수 있는 시간이나 역량이 없고, 이러한 논문으로 인해 더욱 가치있는 입장문과 리뷰 논문을 공유하는 것이 방해받고 있다고 주장했다.  

### 리뷰 논문과 입장문을 arXiv에 제출하기 위해서

합리적이고 신뢰 가능한 심사 수단은 이미 존재하므로, 리뷰 논문과 입장문에 대한 검토는 이들 수단에 의존하는 것으로 변경된다.  

arXiv에 리뷰 논문이나 입장문을 제출하려면 저널, 학회와 같이 동료 심사를 거치는 곳에서 채택되어야 한다. 다만 학회 워크숍에서 수행되는 심사는 전통적인 동료 심사의 엄격한 기준을 충족하지 못하므로 이에 해당하지 않는다.

## AI 생성물이 자원봉사자에 가하는 부담

arXiv CS 카테고리의 중재 관행 업데이트는 AI 생성물이 자원봉사자 중재자들에게 큰 부담을 주고 있었기 때문이다. AI 생성물은 양에 대비하여 질이 좋지 않은 경향이 있었다.  

AI 생성물이 자원봉사자 커뮤니티에 부담을 주는 것은 비단 arXiv CS 카테고리의 문제 뿐이 아니다.

## FFmpeg, 구글에 "자금을 지원하거나 버그 제보를 중단하라"고 요구

[FFmpeg to Google: Fund Us or Stop Sending Bugs](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/)

### FFmpeg

FFmpeg는 전 세계 미디어 처리의 핵심 오픈소스 프레임워크로, VLC, Chrome, YouTube 등 미디어를 사용하는 거의 대부분의 소프트웨어와 서비스에서 사용되는 필수 구성 요소이다.  

하지만 다른 오픈소스 프로젝트와 마찬가지로 FFmpeg는 주로 자원봉사자 개발자들에 의해 유지되고 있고, 심각한 재정 부족 상태에 시달리고 있다.

### 구글 AI가 발견한 사소한 버그와 CVE 남발

최근 구세대 게임 코덱과 관련한 사소한 버그를 구글의 AI 기반 보안 스캐너가 발견하여 보고했다. LucasArts Smush 코덱 디코딩 관련 버그로, 1995년 발표된 게임 〈Rebel Assault 2〉의 첫 10~20프레임에만 영향을 주는 "중간 수준" 취약점이었다.  

FFmpeg 개발자들은 이를 패치했지만, 동시에 "CVE 남발"이라고 표현하면서 비효율적인 버그 리포트를 비판했다.

### 구글 프로젝트 제로의 보고 투명성 정책

25년 7월 구글 프로젝트 제로(GPZ)는 "보고 투명성(Reporting Transparency)" 정책을 도입했다. 이 정책에 따라 GPZ는 취약점 발견 1주일 내 취약점을 공개하고 90일 내 패치 기한을 자동으로 설정하여 수정할 것을 요구한다.  

이 정책으로 패치가 준비되지 않아도 취약점이 공개되므로, 자원봉사자 중심 프로젝트에 과도한 압박을 준다는 비판이 제기되었다. 

비슷한 건으로 libxml2의 유지보수자 Nick Wellnhofer는 지속적인 보안 보고를 두고 "무보수 자원봉사자가 매주 수 시간을 보안 이슈 처리에 시간을 쏟을 수 없다"고 유지보수 중단을 선언하기도 했다.  

### 자금을 지원하거나 버그 제보를 중단하라

FFmpeg 프로젝트는 구글과 같이 FFmpeg를 사용하는 대기업들이 무급 자원봉사자에게 취약점 수점을 떠넘기고 있고, 취약점 보고 시 패치를 제공하거나 재정을 지원해야한다고 요구했다.  

Chainguard의 Dan Lorenc는 "보안 취약점 공개도 디지털 공공재에 대한 기여이고, 구글은 오픈소스 지원에 가장 적극적인 기업 중 하나이다. 이러한 논쟁이 후원자를 멀어지게 할 수 있다."고 지적했고, 보안 전문가들 역시 FFmpeg이 인터넷 인프라의 핵심 구성 요소이므로 취약점은 공개되어야 한다고 주장했다.

그럼에도 불구하고 FFmpeg 측은 AI가 생성한 대량 CVE에 대응할 인력과 자금이 부족하고, 대기업의 실질적인 지원 없이는 유지 불가능하다고 강조했다.

## 참고 문헌
- [Attention Authors: Updated Practice for Review Articles and Position Papers in arXiv CS Category](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category)
- [FFmpeg to Google: Fund Us or Stop Sending Bugs](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/)
