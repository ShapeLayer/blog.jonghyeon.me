---
layout: post
title: The haptic display of complex graphical environments 리뷰
date: 2026-07-09
categories: [paper]
tags: [paper, vr, haptic]
---

[Ruspini, Diego C., Krasimir Kolarov, and Oussama Khatib. "The haptic display of complex graphical environments." Proceedings of the 24th annual conference on Computer graphics and interactive techniques. 1997.](https://dl.acm.org/doi/10.1145/258734.258878)

〈가상현실〉 수업 참고자료

## 배경

이 연구에 앞서서, [Zilles와 Salisbury가 햅틱 시스템에서 반작용 힘을 처리하는 방법으로 god-object를 제안](/posts/2026-07-02-paper-a-constraint-based-god-object-method-for-haptic-display)했다. 하지만 god-object 방법에서 god-object는 object라는 이름과는 달리 부피가 없는 point였다. 그래서 폴리곤 경계에서 폴리곤 사이의 아주 작은 간격을 통과해버릴 수 있었고, 이것을 막기 위해 표면의 토폴로지를 사전에 분석해두어야 했다. 또한 같은 이유에서 마찰이나 강성, 질감과 같은 표면의 속성은 god-object 방법만으로는 표현할 수 없어, 추가적인 계산 계층을 덧붙여야 했다.  

## Proxy

이 연구에서는 god-object를 대신해 proxy를 제안했다. 대체로는 god-object와 비슷하지만, proxy는 질량 없는 구체로서, 기본 도형(Primitive)의 미세한 폴리곤 간격 사이에 빠지지 않을 수준의 반지름을 가진다.

![](/static/posts/2026-07-09-paper-the-haptic-display-of-complex-graphical-environments/phy-pos-prx-pos.png)  

햅틱 센서인 실제 장치 끝점(프로브)은 가상 물체를 뚫고 들어갈 수 있다. proxy는 god-object와 비슷하게 장치 끝점의 위치를 따라가지 않고, 가상 세계에서 상호작용을 시뮬레이션한다면 위치할 의도된 접촉 위치를 유지한다. proxy는 매 time step마다 프로브의 현재 위치를 도달 목표로 두고 그 목표를 향해 움직인다.  

proxy는 장애가 없으면 직선으로 따라가고, 장애를 만나면 구속 면을 따라 목표까지의 거리를 국소적으로 줄이는 쪽으로만 미끄러지다가, 더 줄일 수 없으면 그 자리에서 멈춘다.  

<br />

햅틱 장치에 실제로 가해지는 힘은 proxy와 프로브 위치 차이에 비례한다. God-object 방법에서처럼 가상의 스프링을 연결한 것과 같이 프로브를 proxy 쪽으로 당기는 힘을 출력하여, 물체로부터의 반작용 힘을 느끼게 한다.  

## Proxy 위치 계산과 최적화

![](/static/posts/2026-07-09-paper-the-haptic-display-of-complex-graphical-environments/swept-proxy.png)  

전체 기본 도형을 일일이 검사하면 비용이 크므로, 런타임에서는 이 proxy가 물체의 표면을 휩쓰는 부피를 구해서, 이 부피 범위 안에서 충돌하는 기본 도형을 찾는다. proxy 경로는 직선이므로, proxy와 프로브 위치를 잇는 선분이 환경 물체에서 반지름 1개 거리 안에 있는지를 검사한다. 충돌이 없으면 proxy는 프로브 위치로 직행, 있으면 경로상 첫 장애물이 접촉할 때까지 전진한다.  

<br />

이 과정을 효율적으로 처리하기 위해 구현에서는 configuration space를 제안해 도입했다. Proxy를 점으로 가정[^1]하고, proxy의 장애물이 될 가상 물체의 표면을 proxy가 가질 반지름 $r$ 만큼 확장시켜 이 확장분을 C-obstacle(configuration space obstacle)로 정의한다. C-obstacle은 연속 표면과 non-zero의 두께를 가지므로, proxy의 경로 선분이 C-obstacle과 만나는 곳에 proxy의 진입을 막는 제약 평면(constraint plane)이 유일하게 정해진다.  

[^1]: Proxy가 god-object에 부피를 도입한 듯한 맥락이었지만, 실제 구현에서는 다시금 god-object와 같이 부피 없는 점으로서 proxy를 다루게 되었다. 그럼에도 부피 요소를 고려하여 구현하고 있으므로 proxy를 god-object로 판단할 수는 없다.  

![](/static/posts/2026-07-09-paper-the-haptic-display-of-complex-graphical-environments/c-planes-equiv-free-space.png)  
_Constraint plane과 그에 대응하는 자유공간_  

Proxy가 어떤 한 평면에 접촉하면, 그 아래에 겹쳐진 평면들로는 이동할 수 없다. (Proxy가 직육면체의 윗면에 접촉하면, 그 아래의 바닥면으로는 내려갈 수 없다.) 따라서 계산하는 순간에는 접촉한 평면 아래 공간을 고려하지 않고(논문에서는 이 반공간<sup>half-space</sup>를 제거한다고 표현한다.) 남은 반공간들의 교집합으로 만들 수 있는, 볼록한 자유공간 안에서 사용자의 프로브 위치까지 거리를 최소화하는 점을 새 서브 목표로 삼는다.*

\* 이후의 서브 목표는 proxy가 현재 프레임에서 도달하고자 하는 최적의 목표 위치로 이해한다.    

현재 proxy에서 사용자 위치로의 벡터를 $p$, 새 서브목표를 $x$, 제약 평면의 단위 법선을 $\hat{n}_i$라 할 때  

$$
\begin{aligned}
\text{minimize} \quad & \vert x - p\vert \\
\text{subject to} \quad & \hat{n}_i^{\,T} x \ge 0, \quad i = 1,\ldots,m
\end{aligned}
$$

를 푼다. 모든 제약 평면이 현재 proxy를 지나므로 좌표계 평행이동에 독립이다.  

### 서브목표의 계산

서브 목표는 산출한 자유공간의 쌍대공간[^2]에서 목표 점 $\hat{p}$ 에 가장 가까운 면, 모서리, 꼭짓점을 찾아서 결정한다. 이 과정에서 고려하게 되는 제약 평면이 많아도 한 번에 최대 3개 평면까지만 평면 위에 고정하도록 제약하여, 등식으로 만들어 라그랑주 승수법을 사용한다.  

- 해가 자유공간의 한 면 위에 있으면 활성 평면 1개  
- 모서리 위면 2개  
- 꼭짓점이면 3개  
- 사용자가 이미 자유공간 안이면 0개  

라그랑주 승수법으로 $O(m)$ 에 서브 목표를 구할 수 있고, 각 iteration은 proxy와 사용자 프로브 간의 거리를 줄이므로, 사용자 입력이 안정적으로 주어지면 proxy의 이동도 안정적이다.  

[^2]: 여기서 만들어지는 쌍대공간은 각 평면에 대해서, 이 평면의 외향 법선과 무한 평면을 이용해 만들 수 있는 공간을 의미한다. 쌍대공간에 대해서는 ([\#1](https://aerospacekim.tistory.com/58) [\#2](https://gosamy.tistory.com/258) 참조)  

## Force shading

모서리나 꼭짓점 부분에서는 여전히 힘이 불연속적으로 바뀌어서, 사용자가 느끼는 햅틱 감각이 의도와 다르게 출력되고 있었다. 그래서 이 연구에서는 그래픽 처리에서 [Phong shading](https://en.wikipedia.org/wiki/Phong_shading)의 원리를 도입하여, 폴리곤 정점의 법선을 보간하는 것으로 문제를 완화했다.  

![](/static/posts/2026-07-09-paper-the-haptic-display-of-complex-graphical-environments/force-shading.png)  

Force shading은 proxy의 위치를 조정하는 방식으로 구현한다. 이 업데이트 과정은 두 단계에 걸쳐 이루어진다.  

우선 서로 인접한 폴리곤에 대해서는 이 폴리곤의 정점 법선들을 보간해 새롭게 법선 벡터를 만든다. 이렇게 생성된 보간 법선들로 새 평면을 만들 수 있다. 이 평면을 제약 조건으로서 1차 서브 목표를 구할 수 있다.   

이어서 이 서브 목표를 사용자의 프로브 위치로 가정하고, 원래의 실제 제약 평면을 다시 적용하여 서브 목표를 재계산한다. 만약 1차 서브 목표가 실제 제약 평면 위에 있으면, 가장 가까운 실제 평면으로 다시 투영한다. 이렇게 하여 이후 마찰이나 텍스처와 같은 표면 효과가 물체 표면 위에서 올바르게 적용되도록 한다.  

## 표면 속성

이전 연구들에서, 마찰, 점성, 텍스처와 같은 물체의 표면 속성은 별도의 힘 항으로 처리해왔다. 이 연구에서는 이러한 표면 속성을 proxy 이동을 제한하는 것으로 구현하였다.  

### 정지 마찰


사용자의 프로브 입력이 가상의 물체를 밀 때 발생하는 힘을 평면 법선 성분 $f_n$ 과 접선 성분 $f_t$로 분해한다. 만약 접선 힘이 정지 마찰 계수 $\mu_s$ 와 법선 힘의 곱 $\mu_s \vert f_n \vert$ 보다 작으면, 사용자 입력이 아직 물체 표면을 뚫고 지나갈 만큼 강한 힘을 주지 않은 것으로 판단할 수 있다.  

$$
f_{s,\text{max}} = \mu_s N
$$  

_\* 최대 정지 마찰력은 정지 마찰 계수 $\mu_s$ 와 수직항력 $N$ 의 곱으로 표현한다._  

$$
\vert f_t\vert  \le \mu_s \vert f_n\vert
$$

물체 표면을 뚫고 지나갈 만큼의 힘이 주어져야 물체를 미는 것으로 처리하고 있으므로, 이 물체가 미끄러지지 않고 멈춰있는 듯한 정지 마찰 효과를 구현할 수 있다.  

### 점성, 동적 마찰

질량 $m$, 점성 $b$, 쿨롱 마찰 $\mu_d$ 를 받는 1차원 물체의 운동 방정식을 사용하여 점성 감쇠와 동적 마찰을 구현한다.  

$$
f_t - \mu_d f_n = m\ddot{x} + b\dot{x}
$$

<br />

Proxy의 질량이 0으로 수렴하면, 시스템은 관성이 원인이 되는 가속 구간을 거의 즉시 통과하여, 곧바로 포화 속도에 도달한다. 이 동적 평형 상태에서 proxy의 속도 $\dot{x}$ 는 다음과 같이 계산된다.  

$$
\dot{x} = \frac{f_t - \mu_d f_n}{b}
$$

이 관계를 사용하여 매 클록 사이클마다 프록시가 이동할 수 있는 최대 속도를 계산하고, proxy의 위치를 업데이트한다.  

점성 계수 $b$ 가 클수록 proxy의 속도는 느려지고, 동적 마찰 계수 $\mu_d$ 가 클수록 proxy가 이동하기 위해 필요한 힘이 커진다. 이를 통해 사용자는 물체 표면을 미끄러지듯이 이동하는 느낌을 받을 수 있다.

### 표면 강성

통상적으로는 컨트롤러의 강성 반환값을 낮추어 부드러운 벽을 묘사한다. 하지만 proxy가 이미 여러 표면 속성을 함께 표현하고 있어 이득을 조정하지는 않는다.  

대신 이 연구에서는 proxy가 도달할 목표 위치 $p'$ 를 조정하여 표면 강성을 구현한다. 이상적인 강체 표면에서의 proxy 위치 $p$ 와 사용자 손가락 입력 위치 $v$ 사이의 중간 지점을 목표 위치로 삼아, 물체가 압력에 의해 찌그러지는 느낌을 구현한다.  

<br />

구체적으로 무한 강성 가정 proxy 위치 $p$와 손가락 $v$, 강성 파라미터 $s_s \in [0,1]$에 대해  

$$
p' = v + s_s (p - v)
$$

를 햅틱 제어 루프에 넘길 proxy로 사용하고, 추적용 proxy $p$는 표면을 계속 따라가도록 유지한다.

### 질감

물체 표면의 마찰, 점성, 강성 속성들을 텍스처 맵 이미지로 변조함으로써 질감 데이터를 생성한다. 기본적으로는 매 클록 시작 시점의 proxy 위치에서 텍스처 값을 샘플링한다.  

<br />

주의할 점으로, 고마찰의 격자선이 매우 미세하게 평면에 깔려있다면, proxy의 경로 전체를 샘플링하지 않으면 이 고마찰 격자선을 건너뛸 수 있다고 언급한다.  

## 마무리

이 연구에서는 proxy를 제안했다. 대략적으로 god-object 방법의 확장으로 받아들일 수 있고, 배경으로 언급했던 god-object 방법의 문제점들을 보완했다고 볼 수 있다.  

특히 force shading\*\*과 표면 속성 처리도 proxy 처리로 한 데 모아 다루면서, 원래 계산 레이어를 추가해 개별적으로 처리해야해 요구되었던 높은 컴퓨팅 비용을 일련의 파이프라인으로 묶어 최적화했다는 점에서 큰 의미가 있다.  

또한 이번 연구에서 god-object를 proxy로 이름을 바꾸면서 기능을 확장한 것과 달리, 이후의 연구에서는 proxy라는 명칭을 그대로 사용한다는 점에서 앞으로의 연구에서 사용할 표준적인 언어로서 proxy를 정의했다고 볼 수도 있다.  

\*\* force shading 과정에서 요구되는 값들은 proxy 위치를 갱신하는 과정에서 이미 계산된 값을 사용하면 된다:
> Since the required interpolation weights have already been computed as part of the collision detection process, this determination requires little additional computation.  
>
> p. 4
