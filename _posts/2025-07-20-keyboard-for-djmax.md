---
layout: post
title: 리듬게임 전용 컨트롤러 제작
date: '2025-07-20'
categories: [report]
tags: [report]
---

## 도입

지난 두 학기에 걸쳐 프로젝트 수업 &lt;IoT컴퓨팅&gt;와 &lt;임베디드소프트웨어&gt;를 수강하면서, 소위 디맥콘, 사볼콘 등으로 불리는 리듬게임 컨트롤러를 제작했다.  

첫회 째는 &lt;임베디드소프트웨어&gt;에서 아케이드 버튼을 사용하는 컨트롤러를 제작했고, 두번째에는 &lt;IoT컴퓨팅&gt;에서 키보드 스위치와 핫스왑 소켓을 사용하여 커스터마이징한 키보드를 제작했다.  

## 목표 설정

두 컨트롤러 모두 DJMAX RESPECT V에 8B에 대응하여 제작하였다. 모두 흔히 말하는 디맥콘에 가까운 형태이다.  

학업 중에 수강 중인 다른 과목과 병행하면서 제작해야 했으므로, 지연율, 편의성 등의 구체적인 품질 요구 목표를 설정하지는 않았다.  

두 과목 모두 아두이노를 사용하는 수업이어서, 특별한 컨트롤러 제어 보드를 별도로 사용하지는 않았다. 두 기체 모두 아두이노 레오나르도를 사용했다.  

## 아케이드 버튼 컨트롤러

![](/static/posts/2025-07-20-keyboard-for-djmax/arcade-device.png)  

_상판의 일러스트는 계획되지 않았다. 제작 과정에서 팀원들이 임의로 추가한 것이다._

[구현체 리포지토리](https://github.com/undefined-rainy-storm/embedded-rhythm-game-controller)  

### 스위치와 회로

이 컨트롤러에서는 IST몰의 405 버튼, 406 버튼을 아두이노 레오나르도에 연결해서 사용했다.  

IST 405 버튼, 406 버튼은 각 규격 크기에 맞는 아케이드 버튼 하우징, LED 모듈, LED 전극 연결 단자가 장착된 COM-NO 스위치로 구성되어있다.  

COM-NO 스위치는 [거성 엔지니어링의 Micro Switch V형, GSM-V0303A06](http://gersung.co.kr/kor_pro01)을 사용한다.

![](/static/posts/2025-07-20-keyboard-for-djmax/gsm-nc-no.png)  

이 COM-NO 스위치는 두 개의 전극을 가지고 있으나, 이 스위치에 장착된 LED 전극 연결 단자의 존재로 이 결합체에는 총 네 개의 전극이 존재한다. 스위치와 LED 단자는 물리적으로 결합되어있을 뿐, 전기적으로 연결되어 있지 않으므로 회로를 설계할 때 이들도 연결할 것을 고려해야 한다.  

![](/static/posts/2025-07-20-keyboard-for-djmax/arcade-circuits.png)  

아케이드 버튼 컨트롤러에서는 각 스위치와 아두이노 핀을 1:1로 연결했다. 스위치와 LED의 각 한쪽 전극을 각각 VIN, GND에 연결하고, 다른 쪽의 전극 두 개와 아두이노 핀을 연결하였다.  

### 하우징

![](/static/posts/2025-07-20-keyboard-for-djmax/arcade-model-drawn.png)  

![](/static/posts/2025-07-20-keyboard-for-djmax/entire-dxf.png)  

하우징은 육면체의 각 판을 5T 아크릴로 커팅하여 만든 후, 조립하여 결합했다.

![](/static/posts/2025-07-20-keyboard-for-djmax/KakaoTalk_Snapshot_20241101_181936.png)  

### 제어 보드의 선정과 제어 코드 구현

아두이노를 제어 보드로 사용한다면, 사용하고자 하는 보드가 HID 키보드 라이브러리를 지원하는지 확인해야 한다.

[Keyboard, Arduino Documentation](https://docs.arduino.cc/library/keyboard)

2024년 하반기 기준으로 키보드 라이브러리를 지원하는 보드 중 아두이노 레오나르도가 가장 저렴하다.  

<br />

회로 상 각 스위치는 보드 핀과 1대1 대응하므로, 매 루프마다 각 핀의 상태를 읽어들여와 키보드 press와 release를 호출한다.  

```cpp
#include <Keyboard.h>

// 아래 코드에서의 PIN_BUTTON_TUNE_LEFT_0, KEYBOARD_BUTTON_TUNE_LEFT_0 등은 define으로 사전 정의되어있다.
void setup() {
  pinMode(PIN_BUTTON_TUNE_LEFT_0, INPUT_PULLUP);
  ...
}

void loop() {
  if (!digitalRead(PIN_BUTTON_TUNE_LEFT_0)) {
    Keyboard.press(KEYBOARD_BUTTON_TUNE_LEFT_0);
  } else {
    Keyboard.release(KEYBOARD_BUTTON_TUNE_LEFT_0);
  }
  ...
}
```

키보드 라이브러리에는 `Keyboard.write` 함수도 있으나, 권장하지 않는다.  

리듬게임에는 한 번만 키를 누르는 단노트 뿐 아니라, 계속해서 키를 누르고 있어야하는 장노트도 존재하므로 매 루프마다 `write`를 호출하는 것은 적절하지 않다.

만약 스터터링에 대응하여 수 밀리초 간 입력값을 무시하는 방식의 구현을 추가하고자 한다면, `Keyboard.write`는 더욱 부적절하다.  

### 재료

- 아두이노 레오나르도 호환보드  
    ![](/static/posts/2025-07-20-keyboard-for-djmax/product-arduino.jpg)  
    일반적으로 정품 보드보다 저렴한 호환 보드를 사용한다. 이번 구현에서도 호환 보드를 사용하였다.  
- AWG 22 케이블  
    ![](/static/posts/2025-07-20-keyboard-for-djmax/product-cable.jpg)  
    점프선으로 사용하기 위해 [쿠팡에서 구매](https://www.coupang.com/vp/products/8351400074)하였다. 다만 구매한 케이블은 구리선에 비해 피복이 두꺼워 다루기 어려웠다.
- IST 405 버튼, 406 버튼  
    ![](/static/posts/2025-07-20-keyboard-for-djmax/product-btn405.jpg)![](/static/posts/2025-07-20-keyboard-for-djmax/product-btn406.jpg)  
    많은 사람들이 주로 채택하는 삼덕사의 아케이드 버튼이 아니라, 가격이 상대적으로 저렴한 IST 버튼을 사용했다. 이후에 아케이드 게임을 주로 플레이하는 사람들의 피드백을 받았는데, 삼덕사 버튼에 비해 누르는 데 힘이 많이 들어가 손가락에 부담이 많이 간다는 의견이 많았다.  
- 하우징 케이스  
    이 작업에서는 학교 메이커스페이스 운영 사업단의 지원을 받아, 5T 아크릴 판과 레이저 커팅을 지원받았다. 사업단에서는 일반적으로 5T 아크릴 판을 개당 25,000원에 재료비를 받아 제공한다고 한다.

그 외에 회로를 연결하고 구현하는데 추가적인 재료 소요가 있다. 케이블을 압착식으로 연결하고자 하면 케이블 압착 단자와 압착기, 납땜으로 연결하고자 하면 납땜 재료를 준비한다.  

## 키보드 스위치 컨트롤러

![](/static/posts/2025-07-20-keyboard-for-djmax/keyboard-device.png)  

[구현체 리포지토리](https://github.com/ShapeLayer/keyboard-for-djmax)  

### 스위치와 회로: 스위치 매트릭스

&lt;IoT컴퓨팅&gt; 수업에서는 세 종 이상의 센서를 사용할 것을 요구했다. 때문에 아케이드 버튼 컨트롤러와는 달리 가용 핀이 포화상태가 되지 않도록 해야했다.  

![](/static/posts/2025-07-20-keyboard-for-djmax/sw-matrix.jpg)  

아케이드 버튼 컨트롤러에서는 스위치와 핀을 1대1로 연결했다면, 키보드 스위치 컨트롤러에서는 스위치 매트릭스를 구성하여 핀을 절약했다.  

스위치 매트릭스는 스위치의 행과 열을 구성하여, 각 스위치가 행과 열의 교차점에 위치하도록 하는 방식이다. 이 방식은 스위치의 개수가 많아질수록 핀 수를 절약할 수 있다.  

이와 같이 매트릭스를 구성하면 1대1 구성보다 제어 코드의 구현이 복잡해진다. 매 루프의 짧은 순간마다 일시적으로 시험 전류를 흘려보내어 각 스위치가 닫힌 상태인지 검정하여야 한다.

```cpp
/**
 * 기체의 좌우측 각 5개의 스위치를 하나의 그룹, 총 두개의 그룹으로 설정
 * 각 그룹을 스위치 매트릭스 상의 행으로 가정
 */

void init_key_pins() {
  /**
   * 핀 입력 상태의 초기화
   *
   * 입력 검정 과정 중에 스위치가 닫힌 상태인지 확인하려면, 각 핀의 저항과
   * 출력 전압을 적절히 조정하여 검정 상황에서 의도한 경로로 전류가 흐를 수
   * 있도록 해야 한다.
   */

  /**
   * 스위치 매트릭스 상의 행 구성 핀
   *
   * 행 핀을 출력 모드로 설정하고 아이들 상태에 HIGH 전압을 출력하도록 함
   */
  pinMode(PIN_TRACK_L, OUTPUT);
  digitalWrite(PIN_TRACK_L, HIGH);
  
  pinMode(PIN_TRACK_R, OUTPUT);
  digitalWrite(PIN_TRACK_R, HIGH);

  /**
   * 스위치 매트릭스 상의 열 구성 핀
   *
   * 열 핀을 입력 모드, 풀업 저항 사용을 설정하여 핀 측에 HIGH 전압이 수용되도록 함
   */
  pinMode(PIN_TRACK_SIDE, INPUT_PULLUP);
  pinMode(PIN_TRACK_1, INPUT_PULLUP);
  ...
}
```

```cpp
void proc_keys_handler(...) {
  /**
   * 스위치 입력 상태 검정
   */

  // 좌측 스위치 5개 그룹 검사 시작
  digitalWrite(PIN_TRACK_L, LOW);
  delayMicroseconds(10);  // 스터터링 방지

  !(bool)digitalRead(PIN_TRACK_SIDE);
  !(bool)digitalRead(PIN_TRACK_1);
  ...
  
  /**
   * 좌측 스위치 5개 그룹 검사 종료
   * 좌측 스위치 그룹의 전압 출력을 다시 HIGH로 설정하여 아이들 상태로 복귀
   */
  digitalWrite(PIN_TRACK_L, HIGH);

  // 우측 스위치 5개 그룹 검사 시작
  digitalWrite(PIN_TRACK_R, LOW);
  ...
}
```

위 코드는 원본 제어 코드의 [핀 초기화 부분](https://github.com/ShapeLayer/keyboard-for-djmax/blob/main/controller/keystate.h)과 [스위치 입력 검정 부분](https://github.com/ShapeLayer/keyboard-for-djmax/blob/main/controller/keypress.h)을 일부 발췌한 것이다.  

<br />

초기화 과정을 거치면서 행 핀(`PIN_TRACK_L`, `PIN_TRACK_R`)은 HIGH 전압을 출력하고 있고, 입력 핀인 열 핀들(`PIN_TRACK_SIDE`, `PIN_TRACK_1`, ...)은 풀업 입력 모드로 HIGH 전압 상태를 유지하고 있다.  

각 그룹의 검정을 시작할 때, 행 핀의 전압 출력을 LOW로 설정하면 행 핀과 열 핀 사이에 전위차가 발생하여 전류 흐름이 발생한다.  

이 때, 스위치가 눌려 회로가 닫힌 상태라면 열 핀의 전압은 LOW로 떨어져, 스위치 입력을 감지할 수 있다.  

- 검정 대상의 회로 상태
    ```
    행 핀 (LOW, 0V) ← 스위치 ← 열 핀 (HIGH, 5V via 풀업 저항)
    ```
- 아이들 상태의 회로 상태
    ```
    행 핀 (HIGH, 5V) - 스위치 - 열 핀 (HIGH, 5V via 풀업 저항)
    ```

<br />

![](/static/posts/2025-07-20-keyboard-for-djmax/sw-matrix-ghost.jpg)  

유의할 점으로는 검정 과정에서 두 개 이상의 스위치가 동시에 눌리는 경우, 두 스위치에 의해 닫힌 상태가 된 다른 경로가 발생할 수 있다는 것이다.  

전류는 항상 전압이 높은 곳에서 낮은 곳으로 가능한 한 모든 경로를 따라 흐르기 때문이다.  

위 그림에서 0번 스위치와 6번 스위치가 동시에 눌렸다면, 1번과 5번 스위치를 경유하는 회로도 닫힌 상태가 되어 총 네 개의 스위치가 눌린 것으로 인식될 수 있다.  

이러한 현상을 고스트 입력이라고 한다.

![](/static/posts/2025-07-20-keyboard-for-djmax/keyboard-circuit.png)

다이오드는 역방향의 전압을 차단하는 정류작용을 하므로, 고스트 입력을 방지할 수 있다.  

스위치에 다이오드를 추가하여 전류가 한 방향으로 흐르도록 한다.  

### 스위치와 회로: 핫스왑 소켓

![](/static/posts/2025-07-20-keyboard-for-djmax/keyboard-hotswap-socket.png)  

_[카일 기계식 핫스왑 소켓](https://www.monstargear.co.kr/1475/?idx=1047)_

키보드 스위치 컨트롤러는 고장난 기계식 키보드에서 추출한 체리 프로필 스위치를 사용했다.  

고장품에서 추출하였기 때문에 스위치의 상태에도 우려가 있어, 이 스위치를 그대로 납땜하여 결선하는 것이 아니라 핫스왑 소켓을 사용하여 스위치를 교체할 수 있도록 하였다.  

### 하우징 케이스 및 회로 구현

![](/static/posts/2025-07-20-keyboard-for-djmax/keyboard-case-model.png)

키보드 스위치 컨트롤러 제작 기간에는 아케이드 버튼 컨트롤러 때와는 달리, 아크릴 판을 지원받을 수 없었다.  

그래서 키보드 스위치 컨트롤러의 하우징 케이스는 교내 메이커스페이스의 3D 프린터를 사용하여 출력하였다.  

<br />

케이스 하우징은 (1) [키보드 레이아웃 에디터](https://www.keyboard-layout-editor.com/)를 이용하여 스위치의 키보드 레이아웃을 설정하고, (2) [키보드 캐드 어시스턴트](https://www.keyboardcad.com/)에서 레이아웃을 실제 크기의 캐드로 변환하여, (3) 캐드 소프트웨어로 3D 모델로 작성하였다.

구체적인 구현 결과는 [여기를](https://github.com/ShapeLayer/keyboard-for-djmax/tree/main/models) 참조할 수 있다.  

### 재료

- 아두이노 레오나르도 호환보드  
    아케이드 버튼 컨트롤러 작업 후의 여분 보드를 사용했다.
- 체리 프로필 키보드 스위치  
- [카일 기계식 핫스왑 소켓](https://www.monstargear.co.kr/1475/?idx=1047)  
    몬스타기어에서는 5,000원 이상 구매해야 하므로 대량 구매를 요하나, 같은 판매처가 쿠팡에서는 소량 판매한다.  
- AWG 22 케이블  
    아케이드 버튼 컨트롤러와 동일한 여분 케이블을 재사용했다.  

<br />

그 외에 앞서 언급한 바와 같이, 평과 과정에서 세 종 이상의 센서를 사용할 것을 요구받았기 때문에 로터리 인코더로 노브를, 평가 기준 상 센서로 인정받은 OLED 디스플레이로 상태 표시를 구현했다.  

키보드 스위치 컨트롤러 제작에는 10개의 키보드 스위치 뿐 아니라 1개의 로터리 인코더, 1개의 128x32 픽셀 I2C OLED 디스플레이가 더 사용되었다.  

## 마무리

아케이드 버튼 컨트롤러는 24년 2학기에 팀 프로젝트, 키보드 스위치 컨트롤러는 25년 1학기에 개인 프로젝트로 진행했다.  

아케이드 버튼 컨트롤러의 경험을 살려 키보드 스위치 컨트롤러는 더 쉽게 높은 퀄리티로 제작할 수 있을 것으로 기대했으나, &lt;IoT컴퓨팅&gt; 수업의 요구사항이 더 많고 복잡했기 때문에 더 많은 시간과 노력이 요구되었다.  

특히 [키보드 스위치 컨트롤러의 제어 코드 리포지토리](https://github.com/shapelayer/keyboard-for-djmax)에서 확인할 수 있듯, 세 개의 모듈을 각각 제어하고 모듈 간 데이터 교환, 출력 처리를 하는데 있어 코드가 매우 복잡해졌다.  

### 키보드 스위치 컨트롤러를 구현하고도 낮은 성적을 받았다

&lt;IoT컴퓨팅&gt; 수업의 프로젝트 마감 기한 중에는 캡스톤 디자인 과목의 마감과 다른 과목의 기말고사도 임박하여서, 구체적인 평가 항목을 고려하지 못했다.  

이로 인해 갖은 세부 평가 기준을 크게 벗어났음에도 대응 여력이 없었다. 키보드 스위치 컨트롤러의 구현이 아케이드 버튼 컨트롤러보다 더 높은 퀄리티를 보였음에도, 더 낮은 평가를 받는 원인이 되었다.  

구체적으로 "5분 내외의 소스코드 설명 영상"의 길이가 그보다 길거나, 이미 발표 중에 구현체의 각 핵심 기능을 설명하였음에도 "데모 영상에서 구현체의 기능을 설명하지 않았다", 비슷한 내용의 소주제를 첨부하였음에도 "요구되는 소주제가 발표 슬라이드에 정확히 존재하지 않는다" 등의 이유로 감점이 있었다.  

<br />

&lt;IoT컴퓨팅&gt;은 전 과정이 교수님이 아니라 조교에 의해 진행되었다. 교수자는 아두이노 소스코드가 C++의 방언임을 이해하지 못한 채 과목을 진행하고, 수업 내용에는 소스코드 상에서 `setup` 함수의 선언이 무조건 `loop` 함수의 선언보다 앞에 위치해야 한다는 등 꽤 틀린 내용이 많이 포함되어 있었다.

나는 별도로 이러한 오류를 제보했으나, 수업에서는 이를 정정하지 않았다. 오류, 그리고 오류 제보는 없었다는 듯이 조용히 넘어갔다.

이러한 이유로 수업을 다소 덜 신뢰하는 상황이었으므로, 낮은 평가를 받아들일 수 없어 이의를 제기했다. 그리고 받아들여지지 않았다.  

평가 과정에서 평가를 깎은 이유에 동의하는 것은 아니다. 하지만 세부 평가 기준을 면밀히 확인하고 엄격히 대응하지 못한 것은 사실이므로, 다소 꽤 아쉬운 결과가 되었다고 생각하기로 했다.  

<br />

![](/static/posts/2025-07-20-keyboard-for-djmax/keyboard-circuit-impl.jpg)  

_키보드 스위치 컨트롤러는 하드보드에 글루건으로 회로를 고정시켜 구현했다._  
