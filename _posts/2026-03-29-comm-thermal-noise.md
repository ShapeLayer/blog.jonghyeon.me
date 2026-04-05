---
layout: post
title: 열잡음과 그 계산
date: 2026-03-29
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

모든 통신 시스템은 송수신 과정 중에 원하지 않는 잡음이 더해진다. 이 잡음은 통신 성능을 저하시키는 주요한 요인 중의 하나로 꼽히므로, 이것을 완화하거나 복원하는 데 집중하여 통신 성능을 개선할 수 있다.  

## 열 잡음

열 잡음은 분자들의 불규칙한 움직임에 의해 나타나므로, 어떠한 형태의 전자장비나 매체에서든 나타날 수 있다. 분자 운동은 고온에서 더 활발해지기 때문에, 열 잡음도 절대 온도에 비례한다.  

열 잡음의 원인은 신호의 주파수와는 독립적이므로, 모든 범위의 주파수 스펙트럼에 균일하게 분포한다. 열 잡음은 흰색 잡음, 화이트 노이즈이다.  

<br />

열 잡음은 잡음전력밀도(watts/Hz) $N_o$, 볼츠만 상수 $K$ ($1.3803 \times 10 ^{-23} J / K$), 캘빈 온도 $T$에 대해서 아래와 같이 정의된다:

$$
N_o = K T
$$

실제로 $N_o$ 과 주파수 $B \text{Hz}$ 를 사용하여 열잡음전력 $N$ dBW에 대해 다음과 같이 표현할 수 있다:

$$
\begin{aligned}
N &= kTB = N_o B \\
&=10 \log k + 10 \log T + 10 \log B \\
&\approx -228.6 \text{dBW} + 10 \log T + 10 \log B
\end{aligned}
$$

<br />

일반적으로 290K(약 17도)를 상온으로 설정한다. 따라서 상온에서의 열 잡음 밀도는 $-174 \text{dBm/Hz}$ 로 정의할 수 있다.  

$$
\begin{aligned}
N_o = KT &\approx 1.38 \times 10^{-23} \times 290 \\
&\approx 4.0 \times 10 ^ {-21} \text{W/Hz} \\
&\approx -204 \text{dBW/Hz} \\
&\approx -174 \text{dBm/Hz}
\end{aligned}
$$

$N_o$ 를 이용해 사용 주파수가 $1.23 \text{MHz}$ 인 CDMA의 총 열잡음 전력을 구할 수 있다.

$$
\begin{aligned}
N &= -174 \text{dBm/Hz} \times 1.23 \text{MHz} \\
&= -174 + 10 \log {(1.23 \cdot 10^6)} \\
&= -113 \text{dBm/1.23 MHz}
\end{aligned}
$$

이러한 계산 결과는 이상적인 상황을 고려한 것이므로, 실제로는 $N = −113 \text{dBm} + \text{NF}$ ($\text{NF}$는 잡음 지수(Noise Figure))와 같이 고려된다.  
