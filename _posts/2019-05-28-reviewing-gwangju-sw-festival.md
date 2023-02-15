---
layout: post
title: 2019 광주SW체험축전을 되돌아보며
date: '2019-05-28'
categories: [review]
tags: [review, project]
---

5월 26일자로 광주SW체험축전이 성황리에 마무리되었습니다.  
체험 프로그램 기획부터 개발, 운영까지 학생들끼리 모두 알아서 준비했던지라 체험축전을 준비하고 운영했던 과정을 되돌아보려고 합니다. 지도 선생님이 거의 개입하지 않으신 덕분에 많은 것들을 배우게 되었습니다.

## 생활기록부를 위한 첫 걸음
이번 체험 축전은 학생 자율동아리, "404 컴퓨터 못 찾음" 명의로 참가하였습니다.  

사실 저를 포함한 대부분의 인원이 생활기록부에 전공 관련 활동을 기록하고자 시작한 동아리였습니다.  
이렇게 목적이 순수하지 않다 보니 무언가 특기할 활동 내용이 필요했습니다. 이 상황에서 2019 광주SW체험축전 체험프로그램 공모 공문을 동아리 지도 선생님으로부터 전달받게 되었습니다.  
이 축전에 참가 의사를 내비친건 그로부터 머지 않은 날이었습니다.  

체험 프로그램 주제를 결정하는 과정은 정말 어려웠습니다.  
일반적인 교육 키트를 활용한 체험 프로그램은 이미 타 학교에서 사실상 고정 참가자로서 프로그램을 운영하고 있었습니다. 그리고 이러한 체험 프로그램은 저희같이 학생 주도라기보다 교사 주도 동아리에서 참여하므로 학교 행정 지식과 자금 동원력이 없는 저희에겐 불리했습니다.  
여기서 유일하게 자신 있는 것은 제 코딩 지식뿐이었습니다.  
최소한 일반 지도 교사보다 상대적으로 코딩 지식이 조금은 더 우위이고, 이 프로그램 준비에 투자할 수 있는 시간도 저희가 좀 더 자유로웠습니다.  
비록 개인적으로나마 작은 프로젝트를 해 본 것이 전부라고 해도, 그조차도 만족스러운 성과를 내지 못했다고 해도, 체험 프로그램에 선정되려면 독자적인 체험 과정을 설계하고 필요한 소프트웨어를 독자적으로 개발해야 한다는 데 생각이 미쳤습니다.  

## 한글 코드로 만드는 디스코드 챗봇
저는 항상 교육용 프로그래밍 언어가 스크래치, 엔트리로 대표되는 블록 코딩으로 설명된다는 사실이 못마땅했습니다. 블록 코딩이 입문자, 초중등학생에게 컴퓨터 프로그램이 작동하는 방식을 탁월하게 표현한다는 데에 반대하는 것은 아닙니다.  
하지만 일반적인 프로그래밍과는 우리의 상상, 인식과 큰 차이가 있었고, 실제 워크플로우와도 큰 차이를 보이므로 현실과 어딘가 괴리감이 느껴지는 체험/교육 과정이라고 생각했습니다.  

이에 여기서 시작하여 코딩에 지식이 없는 사람들이 코딩을 어려워하는 것은 "프로그래밍 언어가 영어로 구성되어있어서 그런 것이 아닐까"는 생각에 이르렀습니다.  
이전에 [약속 프로그래밍 언어](http://yaksok.org/)라는 것을 처음 접했을 때 한국어로 코드를 작성하면 프로그램을 이해하기 더 쉽지 않을까 생각한 적이 있었습니다.  
더 이전엔 로봇 교육을 받으며 ROBOTIS의 독자적인 한국어 프로그래밍 언어를 경험하기도 했습니다.  
이미 한국어 프로그래밍 언어 개발 시도, 그리고 교육용으로 실제로 한국어가 채택된 사례를 목격하며 자연스럽게 "교육용" 한국어 프로그래밍 언어에 대해 생각한 것 같습니다.  

![](/static/posts/2019-05-28-reviewing-gwangju-sw-festival/roboplus_task_001.png)  
_source: ROBOTIS_; ROBOTIS 자체 설계 언어

이어 자체 설계한 한국어 프로그래밍 언어로 디스코드 챗봇을 구현하도록 체험 프로그램을 준비했습니다.  
일반적인 CLI 환경으로 코드 실행 결과를 출력하도록 하는 것보다 내용면으로 다른 체험부스와 구분되면서 체험자들에게도 더 나은 사용자경험을 제시할 수 있다고 생각했으므로 이렇게 판단했습니다.  
일반 체험자들 입장에서 "프로그램"은 CLI 프로그램이라기보다 시각적으로 만족감을 주는 인터페이스가 갖춰진 프로그램이므로 "내가 직접 프로그램을 만들었다"고 느끼게 하는데 더 좋은 경험을 제시할 수 있었을 것입니다.  

## 구현
체험 소프트웨어는 자체 설계 언어에서 파이썬 코드로 변환하는 트랜스컴파일러로 구현했습니다.  
일반적으로 컴파일러가 이렇게 동작하지는 않겠지만, 자체 설계 언어에서 확인할 수 있는 주요 코드 패턴을 정규표현식으로 처리하고 파이썬 코드를 문자열로서 변환시키는 방식으로 개발했습니다.  
이전에 잠시 발 담궜던 오픈나무 프로젝트가 동일한 형식으로 나무마크를 변환하는 것을 참고했습니다.

만들어낸 언어 구현체는 컴파일러라기보다 코드 템플릿 작성기에 가까웠습니다. 언어를 컴파일하고 discord.py 모듈이나 디스코드 API에 한국어 API 레이어를 추가해야했지만 현실적으로 시간과 지식이 부족했습니다.  
구현체는 결국 `if-else-then`식으로 문자열 수정(`replace`)을 거듭해 파이썬 코드를 작성하도록 해서 코드 스타일이 조금만 바뀌어도 트랜스 컴파일러가 제대로 작동하지 않았습니다.  
그리고 자체 설계 언어에 파이썬 코드를 추가하더라도 설계 언어 규격이 아님에도 트랜스 컴파일러가 그대로 코드를 통과시키면서 잘 작동했습니다.

## 운영
체험 부스를 운영하는데 체험 소프트웨어만 개발하면 끝나는 것도 아니었습니다.  
체험 부스 운영을 위해 축전 운영 측과 계속해서 연락과 공문을 주고 받았는데, 거의 대부분이 소프트웨어 개발을 주도한 제 개입이 필요한 내용이었습니다.  
개발을 진행하며 체험 소프트웨어 사용자 매뉴얼 작성, 공문/행정 문서 작성, 홍보물 디자인 등을 병행해야 했습니다.

체험에 사용되는 기자재 투입 역시 조금 난관이 있었습니다. 처음에는 학교에 남는 노트북을 사용하고자 했는데, 기자재 담당 선생님의 협조를 받아내는 것 조차 쉽지 않았습니다.  
제공받은 노트북도 이미 상당히 소모되어 포맷 없이는 사용이 어려운 것 뿐이었습니다. 이왕 포맷이 필요하다면 임시로 상대적으로 부하가 덜한 리눅스를 설치하고 반납할때 원상 복구 시키는 것이 낫겠다 싶었지만, 포맷도 리눅스 설치도 허락을 받아내지 못했습니다.

이 상황 속에서 마침 축전 지원 예산을 받을 수 있다는 공지를 전달받았습니다. 그리고 우여곡절 끝에 지원 예산으로 100만원을 받아왔습니다.  
하지만 리눅스의 힘을 너무 과신한 나머지 30만원대 노트북 세 대를 구입했다가 생각보다 훨씬 저열한 성능에 결과적으로 예산 100만원을 그냥 날리게 되었습니다. 얻은 것은 늘어난 노트북 세 대에 대한 행정 처리로 기자재 담당 선생님이 일하시는 모습뿐이었습니다.  
결국 체험 부스에선 집에 돌아다니는 애슬론 II와 샌디브릿지 펜티엄으로 데스크톱을 급하게 만들어 사용하는 것으로 마무리지었습니다.

## 체험 프로그램은 성공했나?
누군가 체험 프로그램 운영이 만족스러웠냐고 물어본다면 저는 다방면으로 아쉬웠다고 대답할 것 같습니다.

### 체험 프로그램 설계 자체가 잘못됐다.
저는 코딩의 진입 장벽을 인간 언어(Human Language) 하나만 조명했습니다. 훨씬 진입 장벽이 되는 다른 요소들이 충분히 많았음에도 코딩의 진입 장벽을 지나치게 비약했습니다.  
프로그래밍 언어가 한국어라면 일반인의 접근성이 더 증대될 것이라 기대한 것은 무리수였습니다. 저는 ROBOTIS 자체 설계 한글 프로그래밍 언어를 처음 접했을 때 느꼈던 막막함을 잊었습니다. 분명 코드는 한글이었음에도 저는 아무것도 하지 못했었습니다.

프로그래밍 언어가 영어인 것은 가장 낮은 진입 장벽, 혹은 진입 장벽이 아닐 지도 모릅니다. 체험자들은 기대와 달리 지정된 문법에 따라 코드를 작성하지 않았습니다.

![](/static/posts/2019-05-28-reviewing-gwangju-sw-festival/eng-cannot.jpg)

체험자들은 자신이 작성한 문장을 컴퓨터가 잘 이해할 수 있을 것이라는 생각으로 자유롭게 문장을 작성했습니다. 모두 자체 설계 언어 규격에서 벗어난 것이었습니다. 아마 NLP 정도는 도입해야 잘 처리할 수 있을 정도의 자유로운 문장이었습니다.  

어찌보면 당연한 결과입니다.  
프로그래밍 언어는 인간 자연어와 달리 경직된 자유도의 문법만을 가지고 있습니다.  
뿐만 아니라 `1`과 `'1'`의 차이와 같이 주요한 기초 컴퓨터 개념도 일반 체험자는 알고 있을리 만무합니다. 전공자에게는 너무 기초적이어서 무의식적으로 활용하는 지식도 체험자에게는 집중해서 학습해야 하는 난해한 개념이었던 것입니다.  

이번 체험 프로그램은 이렇게 요구되는 관련 지식들이 블록 코딩보다 훨씬 많았습니다.  
다시 말해 체험에 불필요할지 모르는 수많은 인식과 지식들을 스크래치처럼 사용자가 무의식적으로 인식하게 하거나 잠재적으로 의식시키지 못했습니다.  
처음부터 자체 개발된 교육/체험용 프로그래밍 언어는 교육용도, 일회적인 체험용도 될 수 없었던 모양입니다.

### 팀 프로젝트 운영의 실패, 미숙함
이번 프로젝트는 동아리 명의로 진행되었지만, 사실상 제 개인 프로젝트였습니다.  
부원들에게 빠르게 파이썬을 교육해주고 개발에 투입하고자 했지만 파이썬 진도는 뜻대로 나가지 못했습니다. 사실 진도가 마무리되었다 할지라도 경험의 부재로 개발 소요 시간이 오히려 늘어나게 됬을 것입니다.  
이러나 저러나 제게 부담이 덜어지진 않았을 것입니다.  

개발은 차치하고서라도 행정이나 다른 업무들은 부원들에게 맡겨봤어야 했는데, 그것조차 제가 전부 처리한 것은 좋은 선택이 아니었습니다.  
저는 제게 들어오는 부담에 힘겨워하며 부원들과 소통을 단절했습니다. 부원들은 무엇을 해야 할 지 모르는 채 "그저 공중에 붕 떠 있었습니다". 심지어 축전 전날까지도 체험 부스 운영 내용을 제대로 이해하지 못하는 부원도 있었습니다.  

부장 역할에 있는 제가 부원들 업무를 조정하고 교통 정리를 하는 대신 개발 일을 이유로 부재 상태에 있으니 부원들 사이에 업무 하나하나에도 크고 작은 갈등이 이어졌습니다.  
갈등은 봉합되지 않은 채 결국 제 앞에서 부원 한명이 터지는 것으로 축전과 함께 마무리되었습니다.  
가장 좋지 않은 형태로 마무리된 셈입니다.

## 마무리
이번 경험으로 체험 부스를 방문했던 체험객이든, 체험 부스를 운영했던 동아리 부원이든 제가 바라보는 세상과 다른 이들이 바라보는 세상이 너무 다르다는 것을 느꼈습니다.  
아직 저는 배울 점이 많고 더욱이 미숙한 것을 실감했습니다.