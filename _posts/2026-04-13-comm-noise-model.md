---
layout: post
title: 잡음 모델
date: 2026-04-13
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

통신 시스템의 성능은 신호 전력에 대한 잡음비와 비례한다. 신호전력 대 잡음비 SNR $G$, 잡음 인자(noise factor) $f$, 잡음 지수(noise figure) $F$ 는 다음의 관계로 이루어진다.  

$$
F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} = \frac{S_i / N_i}{G S_i / G(N_i + N_{ai})}
$$

- $S_i$ : 입력 신호 전력
- $N_i$ : 입력 잡음 전력
- $N_{ai}$ : 증폭기에 의해 추가된 잡음 전력
- $G$ : 증폭기 이득

이 때 $S_i$ 는 입력 신호 전력, $N_i$ 는 입력 잡음 전력, $N_{ai}$ 는 시스템이 추가하는 잡음 전력이다.  

<br />

만약 증폭기가 잡음을 고려하면서 처리하지 않고 모든 신호를 증폭한다면, 노이즈도 함께 증폭되어 출력된다.  

신호를 20dB 증폭시키는 장치에서 SNR이 10dB만큼 감소했다면, 잡음 인자 $f$ 는 10dB로 판단할 수 있다.

<br />

위의 잡음 지수 $F$ 정의를 변형하여 아래와 같이 정리할 수 있다.  

$$
\begin{aligned}
F &= \frac{S_i / N_i}{G S_i / G(N_i + N_{ai})} \\
&= \frac{S_i / N_i}{S_i / (N_i + N_{ai})} \\
&= \frac{N_i + N_{ai}}{N_i} \\
&= 1 + \frac{N_{ai}}{N_i}
\end{aligned}
$$

노이즈는 온도의 영향을 받는다. [열 잡음에 근거](/posts/2026-03-29-comm-thermal-noise)하여 입력 잡음 전력 $N_i$ 는 다음과 같이 표현할 수 있다.    

$$
\begin{aligned}
N_{ai} &= (F - 1) N_i \\
K T_e W &= (F - 1) K T_0 W \\
T_e &= (F - 1) T_0 = (F - 1) 290 \text{K}
\end{aligned}
$$
