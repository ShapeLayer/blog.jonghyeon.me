---
layout: post
title: Delay Spread
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

![](/static/posts/2026-04-20-correlation-coefficient-and-correlation-analysis/delay-spread-in-env.png)  
_지역 별 Delay Spread $T_d$_

전원 지역은 장애물이 적어 비교적 작은 Delay Spread를 보이는 반면, 도심 지역은 장애물이 많아 큰 Delay Spread를 보인다.  

만약 주파수 $f$ 가 $\frac{1}{2T_d}$ 만큼 변경되면, 결합된 사인파는 마루에서 골로 이동한다. 마루는 보강간섭이 발생하여 신호의 최대점이 되는 지점이고, 골은 상쇄간섭이 발생하여 신호의 최소점이 되는 지점이다. 따라서 주파수 변동 스케일의 차수는 $\frac{1}{2 T_d}$ 라고 할 수 있다.  

$$
\begin{aligned}
\text{Peak} \theta(f_1) &= 2\pi f_1 T_d + \pi = 2n\pi  \quad (n = 0, 1, 2, \ldots) \\
&\Rightarrow f_1 = \frac{2n-1}{2T_d} \\
\text{Valley} \theta(f_2) &= 2\pi f_2 T_d + \pi = (2n+1)\pi  \quad (n = 0, 1, 2, \ldots) \\
&\Rightarrow f_2 = \frac{n}{T_d} \\
\end{aligned}
$$

$$
\Delta f = f_2 - f_1 = \frac{1}{2T_d}
$$


## Coherence Bandwidth

Coherence Bandwidth(코히어런스 대역폭)은 채널이 비슷한 성질(동일한 채널 이득)을 유지할 수 있는 주파수 범위이다. 구체적으로는 특정한 시간동안 스냅샷을 찍었을 때, 게인이 어느정도 유지되는 대역폭을 의미한다. 다른 채널과 구분되는 성질이 유지되어야 하므로, 신호의 다중경로 간섭에 큰 영향을 미치는 Delay Spread $T_d$ 가 Coherence Bandwidth를 결정하는 중요한 요소가 된다. 

앞서 확인했듯, 주파수 변동 스케일은 $\frac{1}{2 T_d}$ 에 비례한다. Delay Spread $T_d$ 가 클수록 주파수에 따른 채널 변화가 심해져 Coherence Bandwidth가 좁아진다. 반대로 $T_d$ 가 작을 수록 Coherence Bandwidth는 넓어진다.  

따라서 Coherence Bandwidth $W_c$ 는 Delay Spread $T_d$ 와 반비례 관계를 갖는다.  

$$
W_c \approx \frac{1}{2 T_d}
$$ 

## Flat Fading (평탄 페이딩)

![](/static/posts/2026-04-21-comm-delay-spread/flat-fading.jpeg)

$$
W_c \gg W
$$

신호의 대역폭 $W$ 가 Coherence Bandwidth $W_c$ 보다 훨씬 좁을 때, 평탄 페이딩이 나타난다.  

신호가 차지하는 대역 내에서 채널의 응답(게인)이 거의 일정하므로, 신호 전체가 동일한 비율로 강해지거나 약해진다. 주로 대역폭이 좁은 Narrowband(협대역) 통신 시스템에서 발생한다.  

## Frequency Selective Fading (주파수 선택적 페이딩)

![](/static/posts/2026-04-21-comm-delay-spread/frequency-selective-fading.jpeg)

$$
W_c < W
$$

신호의 대역폭 $W$ 가 Coherence Bandwidth $W_c$ 보다 넓을 때, 주파수 선택적 페이딩이 나타난다.  

신호 대역 내에 채널의 마루와 골이 모두 존재하여, 어떤 주파수 성분은 통과하고, 어떤 주파수 성분은 상쇄된다. 주로 대역폭이 넓은 Wideband(광대역) 통신 시스템에서 발생한다.  

<br />

시나리오에 따라서, Flat Fading이 좋은 상황이 있고, Frequency Selective Fading이 좋은 상황이 있다. 만약 음성 데이터를 보내야 하는 상황에선, 음성 데이터는 대체로 대역폭이 좁은 신호이기 때문에, Flat Fading이 더 좋을 수 있다. 반면에 다중 안테나 등으로 사용 가능한 채널이 많다면 Frequency Selective Fading을 활용하는 것이 더 좋을 수 있다.  

## 심볼 간 간섭(ISI: Inter-Symbol Interference)

![](/static/posts/2026-04-21-comm-delay-spread/isi.jpeg)

다시 시간 관점에서, Delay Spread $T_d$ 가 얼마나 늦게 반사되어 들어오는지 고려한다면, Delay Spread $T_d$ 가 지나치게 길어져 다른 심볼이 다루어지는 시점에, 지연된 신호가 도달하여 간섭을 일으킬 수 있다. 이것을 심볼 간 간섭(ISI: Inter-Symbol Interference)이라고 한다. 심볼 간 간섭을 완화하거나 보상하기 위해 Equalizer를 사용할 수 있다.  

$$
\begin{aligned}
&y(t) = s(t) * h(t) + n(t) \\
\overset{ft}{\Leftrightarrow} &
Y(f) = S(f)H(f) + N(f) \\
\Rightarrow & Y_{u}(f) = S(f) + \frac{N(f)}{H(f)} 
\end{aligned}
$$

Equalizer는 채널의 역응답을 적용하여, 원래 신호 $S(f)$ 를 복원하려고 시도한다. 하지만 $H(f)$ 를 어떻게 추정하는지에 따라, 오히려 노이즈가 증폭될 수도 있다.  

<br />

![](/static/posts/2026-04-21-comm-delay-spread/linear-equalizer-ko.png)  
_선형 이퀄라이저의 개념도_  

<br />

![](/static/posts/2026-04-21-comm-delay-spread/non-linear-equalizer-ko.png)  
_비선형 이퀄라이저 예시의 개념도_

<br />

![](/static/posts/2026-04-21-comm-delay-spread/rake-recv.png)

심볼 간 간섭을 제거하기보다 적절히 활용해내는 방법도 있는데, Rake Receiver를 그 사례로 꼽을 수 있다. Rake Receiver는 다중 경로로 들어오는 신호를 각각 수신하여, 각 경로의 신호를 최대한 활용하여 원래 신호를 복원하려고 시도한다. 각 다중경로의 신호를 독립적인 코릴레이터를 사용하여 신호를 복호화한 후, 각 경로의 신호 강도에 비례해 가중합함으로써 신호를 복원하면서 에너지 이득을 획득한다.  

## Delay Spread의 채널 응답

Delay Spread를 채널 응답 관점에서 정리할 수 있다. 수신 신호 $r(t)$ 는 LOS 신호 $As(t)$ 와 지연된 신호 $As(t - \tau)$ 의 합이다.  

$$
\begin{aligned}
r(t) &= As(t) + As(t - \tau) \\
\overset{ft}{\Leftrightarrow} R(f) &= AS(f) + A S(f) e^{-j 2 \pi f \tau} \\
&= AS(f) (1 + e^{-j 2 \pi f \tau})
\end{aligned}
$$

유효 채널 응답(Effective Channel Response) $H(f)$ 도 위에서 구한 $R(f)$ 를 이용하여 표현할 수 있다.  

$$
\begin{aligned}
H(f) &= 1 + e^{-j 2 \pi f \tau} \\
&= e^{-j \pi f \tau} (e^{j \pi f \tau} + e^{-j \pi f \tau}) \\
&= 2 e^{-j \pi f \tau} \cos(\pi f \tau)
\end{aligned}
$$

따라서 채널 스펙트럼 $\|H(f)\|$ 는 $\cos(\pi f \tau)$ 의 형태로 표현될 수 있다.  

$$
\|H(f)\| = 2 \| \cos(\pi f \tau) \|
$$

## 움직이는 Rx

![](/static/posts/2026-04-21-comm-delay-spread/simple-model-2.png)  

만약 도입에서 제시한 1차원 신호 모델에서, Rx가 속도 $v$ 로 이동하고 있다면, 주파수 천이가 발생하여 신호의 위상과 진폭이 변화하게 된다.  

$$
r(t) = r_0 + vt
$$

$$
\begin{aligned}
S_1 &= \frac{\alpha}{r(t)} \cos(2 \pi f_c (t - \frac{r(t)}{c})) \\
S_2 &= -\frac{\alpha}{(d + (d - r(t)))} \cos(2 \pi f_c (t - \frac{d + (d - r(t))}{c})) \\
&= -\frac{\alpha}{2d - r(t)} \cos(2 \pi f_c (t - \frac{2d - r(t)}{c}))
\end{aligned}
$$

- $S_1$: LOS 신호, $S_2$: 반사 신호

$$
\begin{aligned}
S &= S_1 + S_2 \\
&= \frac{\alpha}{r(t)} \cos(2 \pi f_c (t - \frac{r(t)}{c})) - \frac{\alpha}{2d - r(t)} \cos(2 \pi f_c (t - \frac{2d - r(t)}{c})) \\
&= \frac{\alpha}{r_0 + vt} \cos(2 \pi f_c ((1 - \frac{v}{c})t - \frac{r_0}{c})) - \frac{\alpha}{2d - (r_0 + vt)} \cos(2 \pi f_c ((1 + \frac{v}{c})t - \frac{2d - r_0}{c}))
\end{aligned}
$$

반사 신호의 경로에서 움직인 거리가 LOS 신호의 경로에서 움직인 거리와 같다고 가정하면 $r_0 + vt$ 를 $2d - r(t)$ 로 근사할 수 있다.  

$$
r_0 + vt \approx 2d - r_0 - vt
$$

$$
\begin{aligned}
&\frac{\alpha}{r_0 + vt} \cos(2 \pi f_c ((1 - \frac{v}{c})t - \frac{r_0}{c})) - \frac{\alpha}{2d - (r_0 + vt)} \cos(2 \pi f_c ((1 - \frac{v}{c})t - \frac{2d - r_0}{c})) \\
\approx & \underbrace{\frac{2 \alpha}{r_0 + vt} \sin(2 \pi f_c (\frac{vt}{c} + \frac{r_0 - d}{c}))}_\text{Time-varying envelope} \sin(2 \pi f (t - \frac{d}{c}))
\end{aligned}
$$

<!-- ## 도플러 스프레드 -->
