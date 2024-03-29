---
layout: post
title: 군대에서 프로그래밍 취미 갖기
date: '2023-04-19'
categories: [review]
tags: [review, tools, web]
---
군대에서 프로그래밍 취미를 갖는다는 것은 상당히 어려운 일입니다. 군에서는 IT 강군을 꿈꾼다고 여러가지 시도를 하는 모양이지만, 동시에 프로그래밍을 불건전한 것으로 이미 낙인찍은 듯한 여러가지 정책도 목격됩니다. 사실 임의로 작성한 코드는 어떻게 보면 비인가 SW에 해당하므로 어느정도 이해는 되지만 공감은 되지 않는 것 같습니다.

## 코드 에디터, 컴파일러 사용하기

군부대 사지방은 프로그램을 함부로 설치할 수 없습니다. VSCode같은 단순한 코드 에디터는 잘 모르겠으나, 컴파일러를 절대 설치할 수 없다는 사실은 이미 널리 알려져 있습니다.

다행인 것은 요즘은 로컬에 설치하지 않아도 사용할 수 있는 개발 환경이 많다는 것입니다.

### Google Colaboratory (Google Colab; 구글 코랩)

구글 코랩은 주피터 노트북의 구글용 파생 버전으로 거의 모든 사항이 주피터 노트북과 일치합니다. 동시에 구글의 컴퓨팅 자원을 사용해 코드를 실행할 수 있습니다.

주피터 노트북이 그렇듯 AI 연구용으로 사용하기 위해 개발되었으므로, 충분한 컴퓨팅 자원을 사용할 수 있습니다. 하지만 역시 주피터 노트북이 그렇듯, 파이썬 외의 언어에서 사용하기에는 조금 어렵습니다.

### Github Codespaces (코드스페이스)

코드스페이스는 VSCode의 온라인 호스팅 버전입니다. 널리 사용되고 있는 VSCode와 사실상 동일하므로 개인적으로 다른 그 어떤 대안들보다 편리하게 사용할 수 있었습니다.

각각의 코드스페이스 인스턴스는 독립적인 VPC이므로 VPC 로컬에 그 어떤 소프트웨어든 설치해서 사용할 수 있습니다. 일례로, 저는 백준에 제출할 어셈블리 코드와 아희 코드를 작성하기 위해 코드스페이스에 NASM과 아희 컴파일러를 설치했습니다.

### 구름 IDE

육군은 구름과 계약하여 군 장병 AI/SW 역량 강화 교육을 시행하고 있습니다. 이 교육을 수강하면 구름 IDE를 사용할 수 있으며, 저 역시 교육을 신청하여 수강 중에 있습니다. 하지만 구름 IDE가 얼마나 쓸만할지 아직 제대로 사용해본 적 없어 일단 충분히 사용해보고 생각해보아야할 것 같습니다.

### Online Compilers

검색엔진에 “\~\~ Online”, “\~\~ Online Compiler”로 작성하면 찾을 수 있는 사이트들입니다. 간단한 코드 조각을 테스트삼아 실행하기에 적합합니다.

## 스마트폰 환경에서 사용하기

저렇게 대안이 많은데도 부대 사지방이 여건이 많이 좋지 않아 고려해야할 점이 더 있습니다. 부대 사지방은 막사 건물 외부의 컨테이너에 조성되어있습니다. 이해할 수 없는 전우조 정책은 어떻게든 할 수 있지만, 관리 중대 행정반에서 사지방 좌물쇠 키를 빌려다가 사용해야 한다는 점이나 사지방이 애초에 관리되지 않아 매우 노후되고 더럽다는 점이 사지방으로의 발걸음을 막고 있습니다. 물론 마음만 먹으면 이 모든 것을 감수할 수 있지만, 항상 그런 것은 아닙니다.

위 대안들은 웹 환경에서 동작하므로 스마트폰이라고 동작하지 않을 이유는 없습니다. 코드를 스마트폰 키패드로 입력할 필요도 없습니다. 인가만 받으면 블루투스 장비는 부대 안에 반입할 수 있습니다.

문제는 의외에 부분에서 발생하는데, 바로 운영체제 종류에 따라 코드 작성 편의가 비약적으로 달라진다는 점입니다. 애플은 아이폰을 컴퓨터처럼 사용하는 것을 원치 않는 것 같습니다. 아이패드는 마우스 지원, 멀티뷰(멀티 애플리케이션) 등 여러가지 지원 사항이 있지만 아이폰은 블루투스 키보드를 지원한다는 사실로도 안도해야하는 느낌입니다.

이에 반해 안드로이드 기기는 이러한 면에서 조금 더 나은 편입니다. 멀티뷰는 실제로 매우 유용하므로 생산성 면에서 큰 차이가 납니다. 특히 널리 사용되는 안드로이드 기기, 삼성 스마트폰은 플래그십 모델에 한해 데스크톱 모드, DeX 모드를 지원합니다. 

![](/static/posts/2023-04-19-programming-in-roka/9B55E60D-5625-40E5-93E6-1056E66C24F0.jpeg)  
_Source: 펀디지_  

이 모드가 얼마나 유용한지 심지어 노트북 폼팩터의 DeX 전용 장비가 따로 판매되고 있습니다. 저 역시 부대 안에서 플립북이라 불리는 이 전용 장비를 사용하는 모습을 드물지 않게 목격하고 있습니다.

하지만 저는 아이폰 사용자입니다. 그리고 iOS의 편의 기능들이 블루투스 키보드를 이용해 코드를 작성하는 상황에서는 불편함으로 작용할 수 있습니다.

<video loop="loop" muted="muted" autoplay="autoplay" playsinline style="width: 100%; height: 100%;">
  <source src="/static/posts/2023-04-19-programming-in-roka/IMG_2696.MOV" type="video/mp4">  
</video>

_터미널에 어떤 내용을 넣는지 모르니 계속해서 오타가 납니다: "I cannot see what I(?) typing now"_

위 영상은 Codespaces에서 블루투스 키보드를 이용해 터미널에 명령을 넣는 모습입니다. 입력기가 활성화되면 나타나는 하단의 UI가 터미널을 가리고 있습니다.

## 마무리

아무래도 군대라는 특수한 상황 아래에서 프로그래밍 취미를 가지려면 삼성 안드로이드 스마트폰이 여러 방면에서 더 나은 선택인 것 같습니다. 사실 안드로이드 스마트폰에서 아이폰으로 바꾼 것도 군 입대가 계기였는데 아이러니합니다.

![](/static/posts/2023-04-19-programming-in-roka/031BAA6D-A428-4B28-8B6C-10D1F035F0AF.jpeg)  
_집에 가고 싶습니다_

하지만 부대 안에서 코드 작성보다는 원신을 더 많이 하니 이정도 불편함은 견뎌야 할 것 같습니다.
