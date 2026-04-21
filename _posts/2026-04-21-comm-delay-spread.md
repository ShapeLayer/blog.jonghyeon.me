---
layout: post
title: Delay Spread와 Coherence Bandwidth
date: 2026-04-21
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

## Delay Spread

![](/static/posts/2026-04-21-comm-delay-spread/simple-model-1.png)  

위와 같이, 1차원 상으로 모델링된 길이 $r$ 인 신호, 거리 $d$ 밖의 벽에 부딪혀 돌아오는 신호가 Rx에 도달하는 상황을 가정할 수 있다. 이 때 $r$ 동안 전파된 신호를 LOS 신호로, 길이 $d + (d - r)$ 동안 전파된 신호를 NLOS 신호로 간주할 수 있다. 이 때 Rx에 도달하는 신호는 보강간섭 혹은 상쇄간섭이 발생할 수 있다. NLOS 신호를 다중 경로에 의해 소규모 페이딩되었다고 표현할 수 있다.  

만약 LOS 신호가 지배적이라면 Rician fading으로, NLOS 신호가 지배적이라면 Rayleigh fading으로 모델링할 수 있다.  

<br />

LOS 신호를 $S_1$, NLOS 신호를 $S_2$ 라고 할 때, Rx에 도달하는 신호의 세기는 다음과 같이 표현될 수 있다.  

$$
\begin{aligned}
S_1 &= \frac{\alpha}{r} \cos(2 \pi f_c (t - \frac{r}{c})) \\
S_2 &= -\frac{\alpha}{(d + (d - r))} \cos(2 \pi f_c (t - \frac{d + (d - r)}{c})) \\
&= -\frac{\alpha}{2d - r} \cos(2 \pi f_c (t - \frac{2d - r}{c}))
\end{aligned}
$$

$c$ 는 빛의 속도, $f_c$ 는 중심 주파수, $\alpha$ 는 송신 전력과 안테나 이득을 포함하는 상수이다.  

$$
\begin{aligned}
S &= S_1 + S_2 \\
&= \frac{\alpha}{r} \cos(2 \pi f_c (t - \frac{r}{c})) - \frac{\alpha}{2d - r } \cos(2 \pi f_c (t - \frac{2d - r}{c}))
\end{aligned}
$$

<br />

이렇게 LOS 신호와 NLOS 신호가 서로 간섭을 일으키는 상황에서는, 신호의 이동 거리에 따라 보강간섭이 발생할 수도 있고, 상쇄간섭이 발생할 수도 있다. 따라서 신호의 이동 거리를 NLOS 신호의 지연에 크게 관여하는 요인으로 간주, Delay Spread라고 표현한다. 어떤 NLOS 신호의 원 신호와의 위상차이 $\Delta \theta$ 는 $((2d-r)-r)/c$ 이다.  

$$
S = \frac{\alpha}{r} \cos(2 \pi f_c (t - \frac{r}{c})) - \frac{\alpha}{(2d - r)} \cos(2 \pi f_c (t - \frac{2d - r}{c}))
$$

$$
\begin{aligned}
\Delta \theta &= \frac{2 \pi f_c (2d - r)}{c} + \pi - \frac{2 \pi f_c r}{c} \\
&= 2 \pi f_c \underbrace{\left( \frac{2d - r}{c} - \frac{r}{c} \right)}_{\text{Delay Spread}} \\
&= 2 \pi f_c \underbrace{\frac{2d - 2r}{c}}_{\text{Delay Spread}} \\
\end{aligned}
$$

$$
T_d = \frac{2d - 2r}{c}
$$

<br />

$$
\begin{aligned}
\Delta \theta &= \begin{cases}
2 n \pi & \text{constructive interference} \\
(2 n + 1) \pi & \text{destructive interference}
\end{cases}
\end{aligned}
$$

<br />

![](/static/posts/2026-04-21-comm-delay-spread/delay-spread-in-env.png)  
_지역 별 Delay Spread $T_d$_

전원 지역은 장애물이 적어 비교적 작은 Delay Spread를 보이는 반면, 도심 지역은 장애물이 많아 큰 Delay Spread를 보인다.  

만약 주파수 $f$ 가 $\frac{1}{2T_d}$ 만큼 변경되면, 결합된 사인파는 마루에서 골로 이동한다. 마루는 보강간섭이 발생하여 신호의 최대점이 되는 지점이고, 골은 상쇄간섭이 발생하여 신호의 최소점이 되는 지점이다. 따라서 주파수 변동 스케일의 차수는 $\frac{1}{2 T_d}$ 라고 할 수 있다.  

$$
\begin{aligned}
\text{Peak} \theta(f_1) &= 2 \pi f_1 t_d + \pi = 2 n \pi \Leftrightarrow f_1 = \frac{1 + 2n}{2 T_d} \\
\text{Valley} \theta(f_2) &= 2 \pi f_2 t_d + \pi = (2 n + 1) \pi \Leftrightarrow f_2 = \frac{2n + 2}{2 T_d} \\
\end{aligned}
$$

$$
\Rightarrow f_2 - f_1 = \frac{1}{2 T_d}
$$

## Coherence Bandwidth

Coherence Bandwidth(코히어런스 대역폭)은 채널이 비슷한 성질(동일한 채널 이득)을 유지할 수 있는 주파수 범위이다. 다른 채널과 구분되는 성질이 유지되어야 하므로, 신호의 다중경로 간섭에 큰 영향을 미치는 Delay Spread $T_d$ 가 Coherence Bandwidth를 결정하는 중요한 요소가 된다. 

앞서 확인했듯, 주파수 변동 스케일은 $\frac{1}{2 T_d}$ 에 비례한다. Delay Spread $T_d$ 가 클수록 주파수에 따른 채널 변화가 심해져 Coherence Bandwidth가 좁아진다. 반대로 $T_d$ 가 작을 수록 Coherence Bandwidth는 넓어진다.  

따라서 Coherence Bandwidth $W_c$ 는 Delay Spread $T_d$ 와 반비례 관계를 갖는다.  

$$
W_c \approx \frac{1}{2 T_d}
$$ 

## Flat Fading (평탄 페이딩)

$$
W_c \gg W
$$

신호의 대역폭 $W$ 가 Coherence Bandwidth $W_c$ 보다 훨씬 좁을 때, 평탄 페이딩이 나타난다.  

신호가 차지하는 대역 내에서 채널의 응답(게인)이 거의 일정하므로, 신호 전체가 동일한 비율로 강해지거나 약해진다. 주로 대역폭이 좁은 Narrowband(협대역) 통신 시스템에서 발생한다.  

## Frequency Selective Fading (주파수 선택적 페이딩)

$$
W_c < W
$$

신호의 대역폭 $W$ 가 Coherence Bandwidth $W_c$ 보다 넓을 때, 주파수 선택적 페이딩이 나타난다.  

신호 대역 내에 채널의 마루와 골이 모두 존재하여, 어떤 주파수 성분은 통과하고, 어떤 주파수 성분은 상쇄된다. 이로 인해 수신 신호가 심하게 왜곡되며 심볼 간 간섭이 발생할 수 있다. 이를 보상하기 위해 Equalizer나 OFDM이 사용된다. 주로 대역폭이 넓은 Wideband(광대역) 통신 시스템에서 발생한다.  
