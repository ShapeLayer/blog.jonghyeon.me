---
layout: post
title: 트렁킹(Trunking)
date: 2026-04-22
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

통신 시스템에서 가용 자원은 항상 한정되어있다. 이 자원을 얼마나 사용할 수 있는지 추정, 평가하여야만 시스템을 설계하거나 서비스를 제공할 수 있다.  

트렁킹 이론은 한정된 자원인 채널을 다시의 가입자가 공유하는 방법에 대한 것이다. 채널에 가입한 모든 가입자는 극히 예외적인 상황이 아니라면 동시에 통화하지 않을 것이므로, 가입자 수보다 적은 채널로도 원활하게 서비스를 제공할 수 있다.

## GoS: Grade of Service

GoS는 일정한 시간 동안 통화가 연결되거나 실패하는 정도를 표현한다. Offered Traffic Intensity per Subscriber(구독자 당 제공되는 트래픽 강도) $A_u$ [Erl]과 Total Offered Traffic Intensity (제공되는 전체 트래픽 강도) $A$ [Erl]는, 시간 당 통화 횟수 $\lambda$ [call/s]와 시간 당 평균 통화 시간 $h$ [s], 총 가입자 수 $U$로 정의된다.

$$
A_u = \lambda h
$$

$$
A = U A_u
$$

GoS의 단위 Erl(Erlang, 얼랑)은 트래픽을 측정하는 단위로, 1 Erl은 1시간동안 1개의 채널이 완전히 사용되고 있음을 의미한다.  

<br />

여기서 확장하여, 채널 당 제공 트래픽 강도 $A_c$, Carried Traffic(실제 전달되는 트래픽) $A_{ca}$, Trunking Efficiency(트렁킹 효율) $\eta$ 는 다음과 같이 정의된다.

$$
A_c = \frac{A}{C}
$$

\* $C$ = 채널 수

$$
A_{ca} = A(1 - P_b)
$$

\* $P_b$ = 통화 실패 확률

$$
\eta \text{[Erl]} = \frac{A_{ca}}{C} = \frac{A(1 - P_b)}{C}
$$

트렁킹 효율은 채널 당 Effective Traffic, 즉 얼마나 통화가 성공적으로 점유되는지를 나타낸다.  

## 얼랑 트래픽 모델(Erlang Traffic Model)

얼랑 트래픽 모델에서는 통화 실패에 관한 모델인 B 모델과 통화 지연/대기에 관한 모델인 C 모델이 있다. B 모델은 몇 %의 통화가 차단되는지에 관해 표현하고, C 모델은 평균적으로 얼마나 오래 통화가 지연되는지에 관해 표현한다.  

### B 모델

B 모델에서 차단 확률 $P_b$ 는 시스템의 채널 수 $N$ 과 총 제공 트래픽 $A$ 에 대해 표현된다.  

$$
P_b = B(A, N) =  \frac{\frac{A^N}{N!}}{\sum_{i=0}^N \frac{A^i}{i!}}
$$

이 때, 차단된 통화는 즉시 사라지고 재시도되지 않는다고 가정한다. 이 값은 "$N$ 개의 채널의 시스템에서 몇 %의 통화 시도가 차단된다"고 서술하는 데 사용한다.  

### C 모델

C 모델에서 대기 확률 $P_w$, 평균 대기 시간 $D$ 는 시스템의 채널 수 $C$, 총 제공 트래픽 $A$, 평균 통화 시간 $h$ 에 대해 표현된다.

$$
\begin{aligned}
P_W &= \mathbb{P}[\text{delay} > t] \\
&= \mathbb{P}[\text{delay} > t \mid \text{delay} > 0] \cdot \mathbb{P}[\text{delay} > 0] \\
&= \mathbb{P}[\text{delay} > 0] \cdot \exp(-(C - A) t / H)
\end{aligned}
$$

$$
D = \mathbb{P}[\text{delay} > 0] \cdot \frac{H}{C - A}
$$

## 예시 계산

요구되는 시간 당 통화 횟수는 3000회, 전체 가입자 수는 3750명, 시간 당 평균 통화 시간이 1.76분이라고 할 때, 통화 실패(Blockiing) 확률을 2% 이하가 되도록 하려면 필요한 채널 수 $C$ 는 다음과 같이 계산된다.  

$$
\lambda = 3000 / 3750 \approx 0.8 \text{ call/subscriber/hour}
$$

$$
A_u = \lambda h = (0.8 / 60) \cdot 1.76 \approx 0.0235 \text{ Erl}
$$

$$
A = U A_u = 3750 \cdot 0.0235 \approx 88.13 \text{ Erl}
$$

$$
\cancel{P_b} = B(\cancel{A}, C) \leq 0.02 \Rightarrow C \approx 100
$$

<br />

15개 채널을 가지고 있는 시스템의 가입자가 310명이고, 가입자 당 제공 트래픽 강도가 0.029 Erl, 시간 당 통화 발생 횟수가 1 call/hour, 얼랑 C 모델에서 통화 지연 확률이 5%가 확보되었다. 이 때, 10초를 넘겨서 통화가 지연될 확률은 다음과 같이 계산된다.  

$$
H = A_u / \lambda = 0.029 / (1/3600) = 104.4 \text{ s}
$$

$$
\begin{aligned}
\mathbb{P}[\text{delay} > 10] &= \mathbb{P}[\text{delay} > 10 \mid \text{delay} > 0] \cdot \mathbb{P}[\text{delay} > 0] \\
&= 0.05 \cdot \exp(-(C - A) \cdot t / H) \\
&= 0.05 \cdot \exp(-(15 - 310 \cdot 0.029) \cdot 10 / 104.4) \\
&\approx 0.0281 = 2.81\%
\end{aligned}
$$
