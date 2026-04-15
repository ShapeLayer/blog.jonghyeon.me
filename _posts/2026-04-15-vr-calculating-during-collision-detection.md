---
layout: post
title: 거리 계산 충돌 검사의 처리
date: 2026-04-14
category: [virtual-reality]
---

_〈가상현실〉 수업 노트_

## 점과 점, 원과 원 사이의 충돌 검사

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-point.png)  

어떤 두 정점에 대해서, 혹은 정점을 중심으로 한 원에 대해서, 충돌 검사는 두 점 사이의 거리를 계산하여 실현할 수 있다.  

$$
l = \left\| p_1 - p_2 \right\|
$$

$$
if\ l < r_1 + r_2\ then\ collision
$$

## 점과 선분 사이의 충돌 검사

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-line.png)  

어떤 점 $p_1$ 과 $l_1$, $l_2$ 로 정의된 선분 $L$ 사이의 충돌 검사는 $p_1$ 으로부터 $L$ 에 수선의 발을 내리는 것으로 실현할 수 있다.  

이 경우에, $p_1$ 에서 내리는 수선의 발이 $L$ 위에 닿을 수도 있고, $L$ 에는 닿지 않아 $L$ 의 연장선 위에 닿을 수도 있다.  

<br />

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-line-perpendicular.png)  

$l_1$ 에서 위 사진의 각 점 $p_i$ 까지의 벡터 $\vec{v_i}$ 를 계산하면, 각 점에서 $L$ 에 내리는 수선의 발에 대한 벡터를 계산할 수 있다.  

$$
\begin{aligned}
\vec{v_1} &= p_1 - l_1 \\
\vec{v_2} &= p_2 - l_1 \\
\vec{v_3} &= p_3 - l_1 \\
\end{aligned}
$$  

$$
\vec{n} = \frac{l_2 - l_1}{\left\| l_2 - l_1 \right\|}
$$

$$
\begin{aligned}
\vec{v_i} \cdot \vec{n} < 0 \quad &\text{if } p_i \text{ is left-outside of the line} \\
0 < \vec{v_i} \cdot \vec{n} \le \left\| L \right\| \quad &\text{if } p_i \text{ is on the line} \\
\vec{v_i} \cdot \vec{n} > \left\| L \right\| \quad &\text{if } p_i \text{ is right-outside of the line} \\
\end{aligned}
$$

이와 같이 분할한 각 경우는 충돌 검사에서 각각 다른 계산 과정을 필요로 한다.  

<br />

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-line-calc-case1.png)

선분 위에 수선의 발이 닿지 않는 경우, 선분 $L$ 을 정의하는 양 끝점 $l_1$, $l_2$ 에 대해서, 점 $p_1$ 과 각 끝점 사이의 거리를 계산하여, 그 중 작은 값을 충돌 검사에 사용한다.  

$$
l_\text{min} = \min \left( \left\| p_1 - l_1 \right\|, \left\| p_1 - l_2 \right\| \right)
$$

<br />

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-line-calc-case2.png)

선분 위에 수선의 발이 닿는 경우, 점 $p_1$ 과 수선의 발 $p_\text{middle}$ 사이의 거리를 계산하여, 그 값을 충돌 검사에 사용한다.  

$$
\begin{aligned}
p_\text{middle} &= l_1 + \vec{n} \cdot \left( \vec{v_1} \cdot \vec{n} \right) \\
&= l_1 + \frac{l_2 - l_1}{\left\| l_2 - l_1 \right\|} \cdot \left( (p_1 - l_1) \cdot \frac{l_2 - l_1}{\left\| l_2 - l_1 \right\|} \right) \\
\end{aligned}
$$

$$
l_\text{min} = \left\| p_1 - p_\text{middle} \right\|
$$

<br />

이와 같이 계산된 $l_\text{min}$ 이 점 $p_i$ 가 형성하는 반지름 $r_i$ 보다 작은 경우, 충돌이 발생한 것으로 간주할 수 있다.  

$$
if\ l_\text{min} < r_i\ then\ collision
$$

### 예시 사례

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-line-example.png)  

시나리오 1에서 $p = (3, 1, 2)$, $l_1 = (0, 0, 0)$, $l_2 = (2, 2, 1)$ 이다. $l_1$ 에서 $l_2$ 로 향하는 단위벡터 $\vec{u}$ 와 $p - l_1$, $p - l_2$ 벡터는 다음과 같이 구할 수 있다.  

$$
\begin{aligned}
\vec{u} &= \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} / \sqrt{2^2 + 2^2 + 1^2} = \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \\
\vec{p - l_1} &= \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} \\
\vec{p - l_2} &= \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} - \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix} \\
\end{aligned}
$$

$p_\text{middle}$ 을 $p$ 와 $l_1$ 사이의 벡터 $\vec{p - l_1}$ 의 $\vec{u}$ (혹은 $\vec{l_2 - l_1}$) 방향 성분으로 구한다면 아래와 같이 구할 수 있다.  

$$
\begin{aligned}
p_\text{middle} &= l_1 + \vec{u} \cdot \left( \vec{p - l_1} \cdot \vec{u} \right) \\
&= \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} + \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \left( \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} \cdot \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \right) \\
&= \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \left( \frac{2}{3} \cdot 3 + \frac{2}{3} \cdot 1 + \frac{1}{3} \cdot 2 \right) \\
&= \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \frac{10}{3} \\
&= \begin{bmatrix} \frac{20}{9} \\ \frac{20}{9} \\ \frac{10}{9} \end{bmatrix} \\
l_\text{min} &= \left\| p - p_\text{middle} \right\| = \left\| \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} - \begin{bmatrix} \frac{20}{9} \\ \frac{20}{9} \\ \frac{10}{9} \end{bmatrix} \right\| \\
&= \sqrt{\left( 3 - \frac{20}{9} \right)^2 + \left( 1 - \frac{20}{9} \right)^2 + \left( 2 - \frac{10}{9} \right)^2} \\
&= \sqrt{\frac{234}{81}} = \frac{\sqrt{26}}{3}
\end{aligned}
$$

<br />

시나리오 2에서 $p = (1, 1, 1)$, $l_1 = (0, 0, 0)$, $l_2 = (2, 2, 1)$ 이다. $l_1$ 에서 $l_2$ 로 향하는 단위벡터 $\vec{u}$ 와 $p - l_1$, $p - l_2$ 벡터는 다음과 같이 구할 수 있다.  

$$
\begin{aligned}
\vec{u} &= \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} / \sqrt{2^2 + 2^2 + 1^2} = \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \\
\vec{p - l_1} &= \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \\
\vec{p - l_2} &= \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ -1 \\ 0 \end{bmatrix} \\
\end{aligned}
$$

$p_\text{middle}$ 을 $p$ 와 $l_1$ 사이의 벡터 $\vec{p - l_1}$ 의 $\vec{u}$ (혹은 $\vec{l_2 - l_1}$) 방향 성분으로 구한다면 아래와 같이 구할 수 있다.  

$$
\begin{aligned}
p_\text{middle} &= l_1 + \vec{u} \cdot \left( \vec{p - l_1} \cdot \vec{u} \right) \\
&= \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} + \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \left( \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \right) \\
&= \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \left( \frac{2}{3} \cdot 1 + \frac{2}{3} \cdot 1 + \frac{1}{3} \cdot 1 \right) \\
&= \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix} \cdot \frac{5}{3} \\
&= \begin{bmatrix} \frac{10}{9} \\ \frac{10}{9} \\ \frac{5}{9} \end{bmatrix} \\
l_\text{min} &= \left\| p - p_\text{middle} \right\| = \left\| \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \frac{10}{9} \\ \frac{10}{9} \\ \frac{5}{9} \end{bmatrix} \right\| \\
&= \sqrt{\left( 1 - \frac{10}{9} \right)^2 + \left( 1 - \frac{10}{9} \right)^2 + \left( 1 - \frac{5}{9} \right)^2} \\
&= \sqrt{\frac{18}{81}} = \frac{\sqrt{2}}{3}
\end{aligned}
$$

<br />

시나리오 1에서 만약 $p$ 가 반지름 $r = \frac{\sqrt{26}}{3}$ 보다 큰 구체를 형성한다면, 선분 $L$ 과 충돌이 발생한 것으로 간주할 수 있다.

시나리오 2에서 만약 $p$ 가 반지름 $r = \frac{\sqrt{2}}{3}$ 보다 큰 구체를 형성한다면, 선분 $L$ 과 충돌이 발생한 것으로 간주할 수 있다.

## 점과 삼각형 사이의 충돌 검사

$ax + by + cz + d = 0$ 으로 정의되는 3차원 공간에서의 평면은 법선 벡터 $\vec{n} = (a, b, c)$ 를 가진다.  

이 평면의 정의는 원점에서 $n(x, y, z)$ 방향으로 $d$ 만큼 밀어낸 점에 대한 표현으로도 해석할 수 있다. 따라서 $d' = -d$ 라면 원점을 지나는 평면으로 생각할 수 있다.  

$$
ax + by + cz + d = 0
$$

$$
d' = -d = \vec{n} \cdot p(x, y, z) = ax + by + cz
$$

<br />

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-polygon.png)  

3차원 공간에서 점과 삼각형 사이의 충돌을 검사하기 위해서는, 먼저 점 $p$ 에서 삼각형이 위치한 평면에 수선의 발을 내리는 것으로 시작한다.  

삼각형을 구성하는 세 점 $t_1$, $t_2$, $t_3$ 이 나타내는 평면의 수직 방향 법선 벡터 $\vec{n}$ 는 벡터의 외적으로 구한다.  

$$
\vec{n} = (t_2 - t_1) \times (t_3 - t_1)
$$

$$
\hat{n} = \frac{\vec{n}}{\left\| \vec{n} \right\|}
$$

<br />

점 $p$ 에서 삼각형 평면에 내린 수선의 발 $p'$ 는 점 $p$ 에서 평면을 향해 법선 방향으로 거리 $d$ 만큼 이동한 좌표가 된다.  

$$
p' = p - d \hat{n}
$$

$$
\begin{aligned}
p' &= p - \frac{d'}{\left\| n \right\|^2} \cdot n \\
&= p - \frac{\vec{n} \cdot p}{\left\| n \right\|^2} \cdot n
\end{aligned}
$$

이 수선의 발 $p'$ 가 삼각형 내부에 위치하는지 여부에 따라서, 점과 삼각형 사이의 충돌 검사는 다른 계산 과정을 필요로 한다.

<br />

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-polygon-interpoint-outerprod.png)  

수선의 발이 삼각형 내부에 위치하는 지 여부를 확인하는 방법으로는 외적을 응용하여 각 삼각형의 변과 점 $p$ 를 잇는 벡터의 외적이 모두 같은 방향을 향하는지 확인하는 방법이 있다. 이는 선분 교차 알고리즘에서 선분의 구성성분들을 순회할 때 같은 방향으로 회전하는지 확인하는 CCW 검사와 동일한 원리이다.  

삼각형을 구성하는 세 점 $t_1$, $t_2$, $t_3$ 과 점 $p$ 의 수선의 발 $p'$ 에 대해서, 점 $p'$ 가 삼각형 내부에 위치하고 있다고 가정하고 다음과 같이 계산한다.  

$$
\begin{aligned}
\vec{n_{11}} &= (t_2 - t_1) \times (p' - t_1) \\
\vec{n_{12}} &= (p' - t_1) \times (t_3 - t_1) \\
\vec{n_{21}} &= (t_3 - t_2) \times (p' - t_2) \\
\vec{n_{22}} &= (p' - t_2) \times (t_1 - t_2) \\
\vec{n_{31}} &= (t_1 - t_3) \times (p' - t_3) \\
\vec{n_{32}} &= (p' - t_3) \times (t_2 - t_3) \\
\end{aligned}
$$

$$
\begin{aligned}
\vec{n_{11}} \cdot \vec{n_{12}} &\le 0 \quad \text{?} \\ 
\vec{n_{21}} \cdot \vec{n_{22}} &\le 0 \quad \text{?} \\ 
\vec{n_{31}} \cdot \vec{n_{32}} &\le 0 \quad \text{?} \\ 
\end{aligned}
$$

만약 점 $p$ 의 수선의 발 $p'$ 가 삼각형 내부에 위치한다면 위의 내적값이 모두 0 이상이다. (실제로는 3개 중 2개만 같은 방향으로 회전하는지 확인하면, 나머지 하나도 같은 방향으로 회전함이 보장된다.)  

점 $p'$ 가 삼각형 내부에 위치한다면, 점 $p$ 와 수선의 발 $p'$ 사이의 거리를 계산하여 충돌 검사에 사용한다.  

만약 점 $p$ 의 수선의 발 $p'$ 가 삼각형 내부에 위치하지 않는다면, 점 $p$ 와 삼각형의 각 변 사이의 거리를 점과 선분 사이의 거리 계산법을 사용하여 최소 거리를 구하여 충돌 검사에 사용한다.  

<br />

만약 점 $p$ 가 반지름 $r$ 을 위와 같이 구한 최소 거리보다 크게 형성한다면, 삼각형과 충돌이 발생한 것으로 간주할 수 있다.  

### 예시 사례

![](/static/posts/2026-04-15-vr-calculating-during-collision-detection/point-to-polygon-example.png)  

점 $p = (1, 0, 1)$ 와, $t_1 = (0, 0, 0)$, $t_2 = (0, 1, 2)$, $t_3 = (0, 2, 0)$ 로 구성된 삼각형이 있다. 점 $p$ 에서 삼각형이 있는 평면에 내리는 수선의 발은 다음과 같이 법선 벡터 $\vec{n}$ 과 단위 법선 벡터 $\hat{n}$ 을 구하여 계산할 수 있다.  

$$
\begin{aligned}
\vec{v_1} &= t_2 - t_1 = \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} \\
\vec{v_2} &= t_3 - t_1 = \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix} \\
\vec{n} &= \vec{v_1} \times \vec{v_2} = \begin{bmatrix} -4 \\ 0 \\ 0 \end{bmatrix} \\
\end{aligned}
$$

$$
\begin{aligned}
\hat{n} &= \frac{\vec{n}}{\left\| \vec{n} \right\|} \\
&= \frac{1}{\sqrt{(-4)^2 + 0^2 + 0^2}} \cdot \begin{bmatrix} -4 \\ 0 \\ 0 \end{bmatrix} \\
&= \frac{1}{4} \cdot \begin{bmatrix} -4 \\ 0 \\ 0 \end{bmatrix} \\
&= \begin{bmatrix} -1 \\ 0 \\ 0 \end{bmatrix}
\end{aligned}
$$

<br />

$$
\begin{aligned}
d &= (p - t_1) \cdot \hat{n} \\
&= \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} -1 \\ 0 \\ 0 \end{bmatrix} \\
&= -1
\end{aligned}
$$

점 $p$ 에서 평면까지의 수직 거리 $d$ 는 -1 이므로, 점 $p$ 에서 평면을 향해 법선 방향으로 1 만큼 이동한 좌표가 수선의 발이 된다. 따라서 점 $p$ 에서 삼각형이 위치한 평면에 내리는 수선의 발 $p'$ 는 다음과 같이 구할 수 있다.

$$
\begin{aligned}
p' &= p - d \hat{n} \\
&= \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} - (-1) \cdot \begin{bmatrix} -1 \\ 0 \\ 0 \end{bmatrix} \\
&= \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
\end{aligned}
$$

<br />

이렇게 획득한 수선의 발 $p'$ 가 삼각형 내부에 위치함을 가정하고, 삼각형의 각 꼭짓점과 수선의 발이 같은 방향으로 회전하는지 확인한다.  

$$
\begin{aligned}
\vec{n_{11}} &= (t_2 - t_1) \times (p' - t_1) = \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} \times \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \\
\vec{n_{12}} &= (p' - t_1) \times (t_3 - t_1) = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \times \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \\ 0 \end{bmatrix} \\
\vec{n_{21}} &= (t_3 - t_2) \times (p' - t_2) = \begin{bmatrix} 0 \\ 1 \\ -2 \end{bmatrix} \times \begin{bmatrix} 0 \\ -1 \\ -1 \end{bmatrix} = \begin{bmatrix} -3 \\ 0 \\ 0 \end{bmatrix} \\
\vec{n_{22}} &= (p' - t_2) \times (t_1 - t_2) = \begin{bmatrix} 0 \\ -1 \\ -1 \end{bmatrix} \times \begin{bmatrix} 0 \\ -1 \\ -2 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \\
\vec{n_{31}} &= (t_1 - t_3) \times (p' - t_3) = \begin{bmatrix} 0 \\ -2 \\ 0 \end{bmatrix} \times \begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \\ 0 \end{bmatrix} \\
\vec{n_{32}} &= (p' - t_3) \times (t_2 - t_3) = \begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix} \times \begin{bmatrix} 0 \\ -1 \\ 2 \end{bmatrix} = \begin{bmatrix} -3 \\ 0 \\ 0 \end{bmatrix} \\
\end{aligned}
$$

$$
\begin{aligned}
\vec{n_{11}} \cdot \vec{n_{12}} &= \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} -2 \\ 0 \\ 0 \end{bmatrix} = -2 \le 0 \\
\vec{n_{21}} \cdot \vec{n_{22}} &= \begin{bmatrix} -3 \\ 0 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = -3 \le 0 \\
\vec{n_{31}} \cdot \vec{n_{32}} &= \begin{bmatrix} -2 \\ 0 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} -3 \\ 0 \\ 0 \end{bmatrix} = 6 \ge 0 \\
\end{aligned}
$$

내적이 음수인 사례가 있으므로, 점 $p$ 의 수선의 발 $p'$ 는 삼각형 내부에 위치하지 않는다. 따라서 점 $p$ 와 삼각형의 각 변 사이의 거리를 계산하여, 그 중 최소값을 충돌 검사에 사용한다.  

<br />

점 $p$ 와 삼각형의 각 변 사이의 거리를 계산하기 위해, 점과 선분 사이의 거리 계산법을 사용하여 각 변과의 거리를 계산한다.  

$$
\begin{aligned}
l_1 &= \text{distance}(p, t_1, t_2) \\
l_2 &= \text{distance}(p, t_2, t_3) \\
l_3 &= \text{distance}(p, t_3, t_1) \\
\end{aligned}
$$

$$
\begin{aligned}l_1 &= \text{distance}(p, t_1, t_2) = \frac{\left\| (t_2 - t_1) \times (p - t_1) \right\|}{\left\| t_2 - t_1 \right\|} \\
&= \frac{\left\| \begin{bmatrix} (1 \cdot 1) - (2 \cdot 0) \\ (2 \cdot 1) - (0 \cdot 1) \\ (0 \cdot 0) - (1 \cdot 1) \end{bmatrix} \right\|}{\left\| \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} \right\|} = \frac{\left\| \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} \right\|}{\sqrt{0^2 + 1^2 + 2^2}} \\
&= \frac{\sqrt{6}}{\sqrt{5}} \\

l_2 &= \text{distance}(p, t_2, t_3) = \frac{\left\| (t_3 - t_2) \times (p - t_2) \right\|}{\left\| t_3 - t_2 \right\|} \\
&= \frac{\left\| \begin{bmatrix} (1 \cdot -1) - (-2 \cdot -1) \\ (-2 \cdot 1) - (0 \cdot -1) \\ (0 \cdot -1) - (1 \cdot 1) \end{bmatrix} \right\|}{\left\| \begin{bmatrix} 0 \\ 1 \\ -2 \end{bmatrix} \right\|} = \frac{\left\| \begin{bmatrix} -3 \\ -2 \\ -1 \end{bmatrix} \right\|}{\sqrt{0^2 + 1^2 + (-2)^2}} \\
&= \frac{\sqrt{14}}{\sqrt{5}} \\

l_3 &= \text{distance}(p, t_3, t_1) = \frac{\left\| (t_1 - t_3) \times (p - t_3) \right\|}{\left\| t_1 - t_3 \right\|} \\
&= \frac{\left\| \begin{bmatrix} (-2 \cdot 1) - (0 \cdot -2) \\ (0 \cdot 1) - (0 \cdot 1) \\ (0 \cdot -2) - (-2 \cdot 1) \end{bmatrix} \right\|}{\left\| \begin{bmatrix} 0 \\ -2 \\ 0 \end{bmatrix} \right\|} = \frac{\left\| \begin{bmatrix} -2 \\ 0 \\ 2 \end{bmatrix} \right\|}{\sqrt{0^2 + (-2)^2 + 0^2}} \\
&= \frac{\sqrt{8}}{\sqrt{4}} \\
\end{aligned}
$$

각 변과의 거리 $l_1$, $l_2$, $l_3$ 중 최소값을 구하여 충돌 검사에 사용한다. 최소 값은 $l_1 = \frac{\sqrt{6}}{\sqrt{5}}$ 이다.  

따라서 점 $p$ 가 반지름 $r$ 을 위와 같이 구한 최소 거리 $\frac{\sqrt{6}}{\sqrt{5}}$ 보다 크게 형성한다면, 삼각형과 충돌이 발생한 것으로 간주할 수 있다.  
