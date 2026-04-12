---
layout: post
title: 전파의 간섭성
date: 2026-04-12
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## 전파의 간섭성

파동은 간섭성을 갖는다. 전파 역시 파동으로서, 간섭성을 가지게 되어, 다른 전파와 만났을 때 통신에 있어 방해를 받을 수 있다.  

![](interference-of-radio-waves/simple-model-1.png)

위와 같이 심플하게 표현된 모델에서, 기지국 Tx에서 수신기 Rx에 도달하는 전파는 두 가지 경로를 통해서 도달할 수 있다. 하나는 직선 경로이고, 다른 수신기를 지나쳐 벽에 반사되어 되돌아오는 경로이다. 이 두 경로를 통해서 도달하는 전파는 서로 간섭을 일으킨다.  

| 경로 | 수신 파형 | 참조 |
| :-: | --- | :-: |
| (파란색) <br /> $r$ | $$\begin{aligned}&\frac{\alpha}{r} cos{2\pi f t_0} \\ = &\frac{\alpha}{r} cos{2\pi f (t - \frac{r}{c})}\end{aligned}$$ | \*1 |
| (빨간색) <br /> $d + (d - r)$ | $$\begin{aligned}&-\frac{\alpha}{d + (d - r)} cos{2\pi f (t - \frac{d + (d - r)}{c})} \\ = &\frac{\alpha}{2d - r} cos{2\pi f (t - \frac{2d - r}{c})}\end{aligned}$$ | \*2 |

\*1: $t$는 수신 시점, $t_0$는 송신 시점, $c$는 전파의 속도이다. 따라서 $\frac{r}{c}$는 전파가 $r$ 거리를 이동하는 데 걸리는 시간이다.  
\*2: 수신 파형의 부호 $-$는 벽에서 반사되어 되돌아오는 전파가 위상 반전이 일어난다는 것을 의미한다. $d$는 벽과 수신기 사이의 거리이므로, $d + (d - r)$는 벽에서 반사되어 되돌아오는 전파가 이동하는 총 거리이다.  

따라서 이 모델에서 수신기 Rx는 위 두 전파를 모두 받아 다음과 같이 표현되는 신호를 수신하게 된다.  

$$
\begin{aligned}
\text{Sig}_\text{Rx} &= \text{Path}_1 + \text{Path}_2 \\
&= \frac{\alpha}{r} cos{2\pi f (t - \frac{r}{c})} - \frac{\alpha}{2d - r} cos{2\pi f (t - \frac{2d - r}{c})}
\end{aligned}
$$

## Delay Spread

두 신호는 이동 거리의 차이 때문에, 수신 시점에서 각 신호가 의미하는 내용이 달라지게 된다. 위 신호 수식을 위상 $\theta$ 로 정리하여 위상 차이 $\Delta \theta$ 를 표현하면 다음과 같다.  

$$
\begin{aligned}
\Delta\theta &= \underbrace{\left\{\frac{2\pi f(2d-r)}{c} + \pi\right\}}_{\text{Path 2의 위상}} - \underbrace{\frac{2\pi fr}{c}}_{\text{Path 1의 위상}} \\
&= 2\pi \left(\frac{(2d-r)-r}{c}\right) f + \pi \\
&= 2\pi \underbrace{\frac{(2d-r)-r}{c}}_{{T_d \text{ : Delay Spread}}} f + \pi
\end{aligned}
$$

$T_d$ 로 정리된 $((2d-r)-r) / c$ 는 이 식에서 시간항이다. 이 시간항은 두 경로의 차이에서 발생한 지연 시간의 차이를 나타낸다. 이 시간항을 Delay Spread라고도 부른다.  


![](/static/posts/2026-04-12-comm-interference-of-radio-waves/interference_waveforms_constructive_middle_destructive.png)

만약 이 $\Delta \theta$ 가 짝수배라면 $\text{Sig}_\text{Rx}$는 두 신호가 서로 보강하는 형태가 되어, 수신되는 신호의 세기가 커진다. 반대로 $\Delta \theta$ 가 홀수배라면 $\text{Sig}_\text{Rx}$는 두 신호가 서로 상쇄하는 형태가 되어, 수신되는 신호의 세기가 작아진다.  

$$
\begin{aligned}
\Delta \theta = \begin{cases}
2n\pi & \text{constructive} \\
(2n+1)\pi & \text{destructive}
\end{cases}
\end{aligned}
$$

![](/static/posts/2026-04-12-comm-interference-of-radio-waves/phase_difference_distribution.png)  
