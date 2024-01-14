---
layout: post
title: 홈 서버로 맥미니를 사용해보기로 했습니다
date: '2024-01-11'
categories: [challenges]
tags: [challenges, apple, macmini]
---

![](/static/posts/2024-01-11-using-macmini-as-homeserver/IMG_3721.jpg)

남들 두개 세개씩 가지고 있는 홈 서버, 저는 그동안 여러가지 호스팅 서비스와 연구실 워크스테이션에 기생하면서 홈 서버 구축을 미뤄왔습니다. 장비를 마련할 돈이 없기도 했구요.  

하지만 입대하면서 호스팅 인스턴스들을 정리했고 연구실도 떠나면서 워크스테이션 접근 권한도 반환했습니다. 전역한 이제는 교수님의 은퇴로 돌아갈 연구실도 없어졌지만요. 다행히 군 적금 해지로 돈이 조금 생겨서 이젠 홈 서버를 구축할 수 있게 되었습니다.  

그래서 맥미니를 가져와서 홈 서버를 구축하게 되었습니다.  

**홈 서버를 구성하는 장비**

* Mac mini
  * Apple M2 (8 CPU, 10GPU, 16 NPU)
  * 256GB SSD
  * 16GB RAM
* Synology NAS DS120j
* ASUS RT-AX53U
  * Overwritted with OpenWrt

## vs 클라우드

이전처럼 클라우드 컴퓨팅 서비스에서 서버를 임대할 수도 있었지만 클라우드 서비스는 저와는 잘 맞지 않았습니다.  

클라우드는 월정액으로 유연하게 비용을 설정할 수 있다는 장점이 있긴 하지만, 다시 말하면 매달 비용을 지불해야한다는 문제가 있었습니다.  

항상 생활비의 일정 부분을 클라우드 이용료로 남겨두어야한다는 건 꽤 어려운 일입니다.  

이 때문에 비용 절감 차원에서 정말 필요할 때만 인스턴스를 만들고 용무가 끝나면 인스턴스를 최대한 빨리 정리했습니다. 때문에 클라우드 서비스를 사용할 땐 항상 꽤 성급하게 일을 마무리지으려고 했습니다. 정말 피곤하고 바람직하지 못한 일입니다.  

제대로 쿼터를 지정하면 문제가 없겠지만 설정 미스로 상당히 부담되는, 혹은 감당하기 어려운 비용이 청구될 것이라는 불안함에 여유만 나면 서비스 대시보드를 들여다보는 것도 생각보다 문제입니다. 열심히 설정한 나 자신을 믿는다면 걱정하지 않을 수 있겠지만, 실수는 인식하지 못한 곳에서 벌어지기 때문에 실수라고 하므로 자신을 믿는건 꽤나 어려운 일입니다.  

인스턴스를 정리할 때 함께 생성되는 다른 컴퓨팅 자원들도 부담스럽습니다. [Vultr](https://vultr.com) 같이 상대적으로 규모가 조금 작은 제공자는 조금 낫지만, AWS같이 규모가 큰 주요 제공자는 플로팅 IP 할당, 네트워크 비용 등을 모두 잘게 나눠 컴퓨팅 자원과는 별개로 각각 정산합니다. 문제는 인스턴스를 정리할 때 자동으로 정리되면 좋겠지만 그렇지 않은 곳도 있어서 정리하는 마지막 순간까지 확인의 확인을 거치게 됩니다. (설령 자동으로 함께 해지가 된다 하더라도.) 이 역시 지치는 일이었습니다.  

## 왜 맥미니인가?

맥미니를 홈 서버 장비로 채택한 데에는 몇가지 현실적인 문제가 있었습니다.  

**1. 학생 프로모션**

애플의 학생 프로모션 덕분에 맥미니를 20만원정도 싸게 가져올 수 있었습니다. 쿠팡, 다나와를 전전하며 이전 세대 모델도 찾아봤는데 오히려 그냥 학생 프로모션을 받는게 더 싸게 먹혔습니다. 학생복지스토어도 학생 프로모션이 적용된 비슷한 가격으로 판매하는걸로 알고는 있는데, 애플 홈페이지에서 구매하는 것 만큼 옵션 추가가 덜 자유롭기때문에 알아보지 않았습니다.  

**2. 물리적으로 굉장히 작은 크기와 인테리어**

방도 그렇고, 거실도 그렇고, 어딘가에 추가로 컴퓨터 본체를 놓는다는 것은 부담스러운 일입니다. 랙 케이스는 말할 것도 없고, 일반 데스크톱도 SFF가 아닌 이상에야 괜찮은 배치가 나오지 않았습니다. 그리고 SFF로 서버를 구성하자니 맥미니가 수 배 저렴했습니다.  

**3. 부모님의 전원 종료 욕구를 자극하지 않을 것 같다는 희망**

아직 자취하지 않고 있고 당분간 자취할 계획이 없기 때문에, 부모님의 전원 종료 욕구를 최대한 잠재우고자 했습니다. <물리적으로 굉장히 작은 크기와 인테리어>와 같이, 맥미니는 이전 세대의 VOD 셋톱박스라고 둘러대도 넘어갈 것 같은 디자인과 크기가 특징입니다.  

맥미니의 전원 LED는 굉장히 작은데다 팬 소리도 사실상 안들리니, 전원이 켜져있는지 의식해서 확인하려고 하지 않는 이상 전원 상태를 확인하기 어려울 것 같았습니다.  

게다가 전원 버튼은 존체 뒤에 조그맣게 위치하여 전원 버튼을 찾는데에도 다소의 소모가 있기도 합니다.  

**4. 일반 데스크톱과 비교해 우세한 전력 효율과 전기세**

애플 실리콘 프로세서가 전성비가 뛰어나다는 것은 이미 잘 알려진 사실입니다. 아무리 <부모님의 전원 종료 욕구를 자극하지 않을 것>을 찾아다니는 불효자라고 하더라도 24시간 전원을 넣을 장비에 전기세를 외면하기란 조금 어려웠습니다.  

물론 여러가지 가속기로 중무장한 애플 실리콘이 전성비가 좋은 대신 여러가지 작업에서 속도가 일반 데스크톱보다 잘 안나온다는 것도 알긴 하지만, 그렇게 무거운 작업은 돌릴 생각이 없었으니 괜찮았습니다.  

## 이어지는 비표준의 향연

애플이 자체 표준을 만들어 사용한다는 건 이미 널리 알려진 사실이죠. 사실 그걸 감수하고 맥미니를 가져온거긴 한데, 자체 표준의 매운맛은 꽤 여운이 남는 것 같습니다.  

아래는 맥에서 `systemctl` 대신 사용하는 유틸리티로 ssh를 새로고침한 명령어입니다.  

```zsh
sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

이미 잘 알고있는 명령이나 유틸들도 사용하기전에 다시 한번 찾아보게 되니 조금씩 시간 소요가 더 되는 것 같습니다..  

## 대체 무슨 일이 일어나는거야..?

그래도 단순 시간 소요는 좀 봐줄만 한데, 생각지도 못한 부분에서 꽤 치명적인 문제들이 한번씩 터집니다.  

Podman 위에 마인크래프트 서버 컨테이너를 올리니 마인크래프트 서버가 제대로 작동하지 않고 뻗는 문제가 발견되었습니다. 우선 맥os 바로 위에서 실행하는건 이러한 오류가 발생하지 않고 잘 작동합니다.  

```txt
Starting net.minecraft.server.Main
[19:04:01] [ServerMain/WARN]: Failed to get system info for Microarchitecture
java.lang.NullPointerException: Cannot invoke "String.toUpperCase()" because "this.cpuVendor" is null
        at oshi.hardware.CentralProcessor$ProcessorIdentifier.queryMicroarchitecture(CentralProcessor.java:825) ~[oshi-core-6.4.5.jar:6.4.5]
        at oshi.util.Memoizer$1.get(Memoizer.java:61) ~[oshi-core-6.4.5.jar:6.4.5]
        at oshi.hardware.CentralProcessor$ProcessorIdentifier.getMicroarchitecture(CentralProcessor.java:816) ~[oshi-core-6.4.5.jar:6.4.5]
        at ab.a(SourceFile:66) ~[server-1.20.4.jar:?]
        at ab.a(SourceFile:128) ~[server-1.20.4.jar:?]
        at ab.c(SourceFile:75) ~[server-1.20.4.jar:?]
        at ab.a(SourceFile:82) ~[server-1.20.4.jar:?]
        at ab.a(SourceFile:75) ~[server-1.20.4.jar:?]
        at ab.c(SourceFile:52) ~[server-1.20.4.jar:?]
        at ab.a(SourceFile:82) ~[server-1.20.4.jar:?]
        at ab.<init>(SourceFile:52) ~[server-1.20.4.jar:?]
        at o.<init>(SourceFile:36) ~[server-1.20.4.jar:?]
        at o.h(SourceFile:277) ~[server-1.20.4.jar:?]
        at net.minecraft.server.Main.main(SourceFile:99) ~[server-1.20.4.jar:?]
        at net.minecraft.bundler.Main.lambda$run$0(Main.java:54) ~[?:?]
        at java.lang.Thread.run(Unknown Source) ~[?:?]
```

Docker에서도 같은 문제가 발생하는걸 보니, 아무래도 두 프로그램이 맥 환경에서 가상화 레이어로 사용하는 QEMU에서 CPU 벤더 정보를 제대로 전달하지 않고 있는 것 같습니다.  

```txt
2024-01-11T19:04:18.651+0900    WARN    mc-server-runner        Minecraft server failed. Inspect logs above for errors that indicate cause. DO NOT report this line as an error.    {"exitCode": -1}
2024-01-11T19:04:18.656+0900    INFO    mc-server-runner        Done
```

이 문제는 흥미로워서 이것저것 연구해보고 싶은 게 있긴 한데, 아직 시간적인 여유가 없어서 차후에 과제로 미뤄두기로 했습니다.  

## 마무리

아무튼 홈 서버를 준비할 때 고려했던 문제 몇을 제외하고는 당장 선택을 후회할만한 문제는 없었던 것 같습니다. 앞으로 본격적으로 사용해봐야 알겠지만 당장은 맥미니로 홈 서버를 돌리는게 꽤 만족스럽습니다.  
