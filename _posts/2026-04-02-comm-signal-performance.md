---
layout: post
title: 신호의 성능과 채널 용량
date: 2026-04-02
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## 신호의 성능

어떤 통신에 대해서 통신 성능을 평가하는 방법은 여러 가지가 있을 수 있다. 보통 수율(throughput)이라고 이야기하는데, 오늘날 통신은 여러 개 레이어를 겹쳐 구현되므로, 각 단계마다 각각의 방법으로 정의하고 평가할 수 있다.  

![](/static/posts/signal-performance/throughput.png)

물리 단계에서 수율을 평가하는 방법으로는, 물리적인 거리 $d$ 를 특정한 신호 비트가 얼마나 빨리, 속도 $v_\text{sig}$ 혹은 전송시간 $t_\text{sig}$ 를 사용하여, 이동할 수 있는지 판단하는 것이 가능할 것이다.  

![](/static/posts/signal-performance/transfer-speed.png)

$$
\begin{aligned}
t_\text{sig} &= t_1 - t_2 \\
&= d / v_\text{sig}
\end{aligned}
$$

## 채널 용량

어떤 통신 채널의 성능을 이야기할 때, 논의할 수 있는 것 중 하나로 채널 용량이 있다. 채널에 얼마나 많은 데이터를 실어 보낼 수 있는지에 관한 것이다.  

1920년대, Nyquist가 제시한 Nyquist's Formula에서는, Bandwidth $B$, Binary level (혹은 Symbol Level) $M$ 에 대해서 Capacity $C$ 가 다음과 같이 도입된다:  

$$
C = 2B \log_{2}{M}
$$

Nyquist의 모델은 노이즈가 없는 이상적인 환경에서의 채널 용량을 가정한 것이다. 실제 환경에서는 통신 환경에 잡음이 계속해서 영향을 끼치므로, 이들 잡음을 고려할 필요가 있다.  

<br />

Shannon는 Nyquist 채널 용량 수식의 $M^2$ 부분을 잡음을 고려하여, 신호 대 잡음비(SNR; Signal-to-Noise-Ratio)를 사용해 채널 용량을 정의했다.  

$$
\begin{aligned}
C &= B \log_2{\frac{N + S}{N}} \\
&= B \log_2{(1 + S / N)}
\end{aligned}
$$

$S$ 는 신호강도, $N$ 은 잡음 강도로, 전체 신호 세기 $S + N$ 에 대해서 잡음 $N$ 의 비율을 나타낸다.  

<br />

![](/static/posts/signal-performance/shannon.jpeg)  

_채널 별로 만족할 SNR은 여유분을 고려하여 설정된다. 아래 항목의 10dB는 계산 결과로는 0dB이다._

위 상황과 같이, 대역폭이 각각 1MHz, 10MHz인 채널을 가정한다. 이들 대역폭을 사용하는 채널의 용량이 동일하게 10Mbps이어야 한다면, 각 채널의 SNR 요구량은 다음과 같이 계산할 수 있다.  

$$
\begin{aligned}
C &= B \log_{2}{1 + \text{SNR}} \\
10 \text{Mbps} &= 1 \text{MHz} \log_{2}{(1 + \text{SNR}_{1\text{MHz}})} \\
\text{SNR}_{1\text{MHz}} &= 2^{10} - 1 \approx 1023 \\
&\approx 30.1 \text{dB} \\
\end{aligned}
$$

$$
\begin{aligned}
10 \text{Mbps} &= 10 \text{MHz} \log_{2}{(1 + \text{SNR}_{10\text{MHz}})} \\
\text{SNR}_{10\text{MHz}} &= 2^{1} - 1 = 1 \\
&\approx 0 \text{dB} \\
\end{aligned}
$$

다시 말해 대역폭 $B$ 와 SNR은 서로 Trade-off 관계이다.  

## $E_b/N_0$

"비트당 에너지 대 잡음 전력 스펙트럼 밀도 비율"인 $E_b/N_0$ 는 아날로그 통신 시스템에서 사용하는 성능 평가 특성 SNR를 디지털 시스템에서 사용할 수 있게 정규화한 것이다. $E_b$ over $N_0$ 로 말하는데, $E_b$ 는 비트당 에너지, $N_0$ 는 잡음 전력 스펙트럼 밀도이다.  

비트 당 에너지 $E_b$ 는 비트 시간 $T_b$와 신호 전력 $S$의 곱으로 표현된다. 잡음 전력 스펙트럼 밀도 $N_0$ 는 잡음 전력 $N$을 대역폭 $B$로 나눈 값이다.  

$$
E_b = S T_b \\
N_0 = \frac{N}{B}
$$

잡음을 열잡음만 고려한다면, [전력 $N$ 은 절대온도 $T$ 에 비례하므로](/posts/2026-03-29-comm-thermal-noise/) $N_0 = kT$ 로 가정할 수 있다. ($N = kTB; N_0 = kTB/B$)

또한 전송 속도인 비트 전송률 $R$ 에 대해서 $T_b = 1 / R$ 이므로 아래와 같이 변형할 수 있다.  

$$
T_b = \frac{1}{R}\\
\frac{E_b}{N_0} = ST_b \times \frac{1}{N_0} = \frac{S}{R} \times \frac{1}{kT}
$$

혹은 아래와 같이 SNR과 대역폭 효율성 $\frac{R}{B}$ 사이의 곱으로 표현할 수 있다.  

$$
\frac{E_b}{N_0} = \frac{S}{N} \times \frac{B}{R}
$$
