---
layout: post
title: OFDM
date: 2026-06-01
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

OFDM은 Wi-Fi, 디지털 방송 등에서 사용되다가, 다중 경로 간섭에 강한 특성 덕분에 4세대 이동통신(LTE) 시스템부터 셀룰러 통신에 도입된 변조 방식이다. 주파수를 여러 개의 직교하는 subcarrier로 분할하여 데이터를 전송하여 주파수를 효율적으로 이용한다.  

## 배경: CDM의 상황

OFDM 이전의 주요하게 사용된 CDM에서는 모든 사용자들이 같은 주파수 대역을 공유하여 데이터를 전송하였다. 이로 인해 다중 경로 페이딩과 간섭 문제가 발생하여 시스템의 성능이 저하되었다. 뿐만 아니라, (1) Near-far 문제가 발생하여 Rx로부터 멀리 있는 사용자의 신호를 제대로 수신하기 위해 전력 제어가 필요하게 되었다. (2) 만약 CDM이 넓은 대역폭을 사용한다면, 지연 신호를 분리하는 데 사용할 chip rate가 매우 짧아져 복잡한 수신기를 사용해야 하게 되었다. 또한 CDM은 지연 신호를 분리하는 데 있어서 (3) Rake receiver를 요구했다. Rake receiver는 다중 경로 신호를 수신하여 각 경로의 신호를 합성하여 데이터를 복원하므로, 복잡한 구조와 높은 계산량으로 높은 비용을 초래하였다.

<br />

그래서 OFDM에서는 주파수를 여러개 subcarrier로 분할하였다. (1) 각 밴드는 다른 밴드에 직교하여 서로 간섭을 일으키지 않으니 전력 제어 문제가 완화할 수 있었다. (2) subcarrier로 분할, 이들 subcarrier를 다양하게 동원하여 대역폭을 증가할 수 있었고, (3) Rake receiver가 없어도 Cyclic prefix를 사용하여 다중 경로 신호를 효과적으로 처리할 수 있었다.  

## OFDM

OFDM은 하나의 넓은 대역 신호를 여러 개의 직교한 좁은 subcarrier로 분할하여 동시에 전송하는 다중화 방식이다. 이들 subcarrier의 직교성 덕에 subcarrier들의 스펙트럼이 서로 겹치더라도 간섭이 발생하지 않는다. 다시 말해 가드밴드 없이도 높은 스펙트럼 효율을 얻을 수 있다.

전체 대역을 $N$ 개의 subcarrier로 분할하면, 각 subcarrier의 심볼 속도는 전체 대역의 심볼 속도의 $1/N$이 된다. 따라서 각 subcarrier는 더 긴 심볼 기간을 가지게 되어 다중 경로 페이딩에 대한 내성이 향상된다. 겹침이 실재하더라도 모수인 심볼 기간이 커졌기 때문에 문제가 되는 부분이 상대적으로 줄어드는 것이다. 또한 subcarrier는 서로 직교하기 때문에, 각 subcarrier의 스펙트럼이 겹치더라도 간섭이 발생하지 않는다.

## Orthogonal Frequency

각 subcarrier $k$ 의 복소수 파형은 $0 \le t < T_s$ 구간에서 표현할 수 있다. $f_k$ 는 $k$ 의 주파수, $T_s$ 는 OFDM에서의 심볼 기간, $\Delta k$ 는 subcarrier 간의 주파수 간격이다.  

$$
\phi_k(t) = \exp(j 2 \pi f_k t)
$$

$$
f_k = k \Delta f  \quad \text{where } \Delta f = \frac{1}{T_s}
$$

<br />

두 복소 파형 $\phi_k(t)$ 와 $\phi_l(t)$ 가 직교성을 가지려면 다음의 조건을 만족해야 한다.

$$
\begin{aligned}
\langle\phi_k, \phi_l\rangle &= \int_0^{T_s} \phi_k(t) \phi_l^*(t) dt = 0 \quad \text{for } k \neq l \\
&= \int_0^{T_s} \exp(j 2 \pi (f_k - f_l) t) dt = 0 \quad \text{for } k \neq l \\
\end{aligned}
$$

이러한 subcarrier의 심볼들을 선형 결합하여 OFDM 신호를 생성한다. 이렇게 구성하면, 시간 영역에서는 파형들이 겹쳐지더라도, 주파수 영역에서는 특정 지점에서 다른 subcarreir들이 0이 되어 한 subcarrier만 관측된다.

$$
x(t) = X_1 \phi_1(t) + X_2 \phi_2(t) + ... + X_N \phi_N(t)
$$

![](/static/posts/2026-06-01-comm-ofdm-overview/ofdm-orthogonaility.jpeg)  

## Guardband와 Cyclic Prefix

![](/static/posts/2026-06-01-comm-ofdm-overview/guardband.jpeg)

이전의 FDM에서는 심볼 간 간섭(ISI; Inter-Symbol Interference), 채널 간 간섭(ICI; Inter-Carrier Interference)을 완화하기 위해 Guardband(가드밴드), 인접 채널 사이에 주파수 여유를 두었다. 하지만 실제로는 다중 경로와 도플러 효과에 의해 발생하는 간섭을 해결하기에는 불충분했다. 또한 가드밴드의 사용은 가드밴드만큼의 주파수 자원을 낭비하여 전력 효율을 저하시키는 결과로 이어진다.    

OFDM에서는 주파수 축에서는 subcarrier가 orthogonal하므로 subcarrier 사이에 guardband를 없앴다. 

<br />

시간 축에서는 다중 경로 지연에 의해 ISI, ICI가 발생할 수 있었는데, 그래서 ICI를 극복하기 또 다른 방법으로 Cyclic Prefix(CP)를 사용하였다. 

CP는 말단의 신호를 앞단에 복사하여 붙여 접두어로 사용하는 것이다. 이렇게 함으로써 채널의 선형 컨볼루션이 Cyclic 컨볼루션으로 바뀌어, CP 길이보다 작은 지연에 대해서는 CP만큼 신호를 지연하여 해석할 수 있으므로, 심볼 경계 바깥에서 발생하는 ISI를 제거할 수 있다. (CP는 같은 신호를 반복하는 것이므로, 지나친 CP는 큰 오버헤드로 작용한다. 따라서 적정 선에서 CP의 길이를 조절하여야 한다.)

<br />

CP는 원래 심볼을 그대로 복사한 것이므로, 심볼 내의 원본 데이터와 CP 신호는 높은 상관성을 가진다. 수신기는 이 반복되는 신호 특성을 이용해 수신 신호와 $N$ 샘플 지연된 신호 사이의 상관성을 계산하여 채널의 주파수 응답을 추정할 수 있다. 이렇게 추정된 채널 응답을 사용하여 수신된 신호를 보상함으로써, 다중 경로로 인한 신호 왜곡을 효과적으로 완화할 수 있다.  

<br />

이렇게 CP를 사용해 획득한 OFDM의 스펙트럼 효율은 가드밴드를 사용한 FDM의 스펙트럼 효율의 거의 두 배에 달한다.  

$$
\begin{aligned}
B_\text{FDM} = 2N \Delta f + (N - 1) f_g \\
\lim_{N \to \infty} B_\text{FDM} = 2N \Delta f
\end{aligned}
$$

$$
\begin{aligned}
B_\text{OFDM} = (N + 1) \Delta f \\
\lim_{N \to \infty} B_\text{OFDM} = N \Delta f
\end{aligned}
$$

## CP-OFDM의 단점

CP는 원본 신호의 일부분을 복제하여 신호의 길이를 늘리기 때문에 OFDM 시스템의 data rate를 감소시킨다. 때문에 발생 가능한 지연 수준을 적절히 평가하여 CP가 지나치게 길어지지 않도록 조절하여야 한다.  

또한 만약 carrier에 frequency offset이 존재한다면, 직교성이 깨지게 되어 ICI가 발생할 수 있다. 때문에 주파수가 항상 정확하게 동기화되어야 한다.  

PAPR(Peak-to-Average Power Ratio)가 높은 것도 단점으로서 작용한다. 여러 개의 subcarrier를 동시에 사용함으로써, 신호의 전력이 특정 순간에 매우 높아질 수 있다. 이로 인해 송신기의 전력 증폭기가 비선형적으로 동작하여 신호를 왜곡시킬 수 있다.  

![](/static/posts/2026-06-01-comm-ofdm-overview/high-papr-non-linear.jpeg)
