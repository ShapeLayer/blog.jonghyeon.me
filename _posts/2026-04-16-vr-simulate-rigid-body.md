---
layout: post
title: 강체 시뮬레이션
date: 2026-04-16
category: [virtual-reality]
---

_〈가상현실〉 수업 노트_

## 도입

$$
M \ddot{X} + C \dot{X} + K X = \sum{F_\text{external}}
$$

_강체 시뮬레이션에서 지배 방정식_

가상 세계에서 강체를 시뮬레이션하는 데 있어서, 현실 세계에서 물체 운동을 설명하는 지배 방정식을 사용한다. 질량 $M$, 감쇠 계수 $C$, 강성 $K$ 에 대해서 위와 같은 지배 방정식을 정의할 수 있다.  

$$
C \dot{X} + K X = F_\text{internal}
$$

강체는 6 자유도를 가진다. 3개의 병진 자유도 $(x, y, z)$ 와 3개의 회전 자유도(roll, pitch, yaw)가 있다. 따라서, 강체 시뮬레이션에서는 6차원 벡터 $X$ 를 사용하여 물체의 위치와 자세를 나타낸다.  

회전 운동은 [쿼터니언 표현](/posts/2026-04-14-vr-rotation-in-3d-space/) 표현을 사용함에도 불구하고 3개의 회전 자유도를 갖는 것은, 쿼터니언이 단위 쿼터니언으로 정의되어, 세 개 변수 요소로 네 개 값을 결정하기 때문이다.  

$$
q = w + x i + y j + z k
$$

$$
\sqrt{w^2 + x^2 + y^2 + z^2} = 1
$$

<br />

강체 시뮬레이션은 강체의 무게 중심을 기준으로 병진 운동과 회전 운동을 처리한다. 이렇게 가정함으로써, 강체의 병진 운동을 무게 중심에 모든 질량이 모여있는 질량 $m$ 의 입자가 위치 $x$ 에서 속도 $v$ 로 움직이는 것으로 단순화한다.  

![](/static/posts/2026-04-16-vr-simulate-rigid-body/rotate-rigidbody-in-center.png)  

회전 운동은 회전 축으로부터의 거리에 따라 회전 속도가 변화하므로, 병진 운동과 같이 입자의 회전으로 가정할 수는 없다. 대신 회전이 발생하는 상황에 따라서는 무게 중심을 사용해 회전 축이나 회전 모멘트를 정의할 수 있다.  


![](/static/posts/2026-04-16-vr-simulate-rigid-body/rotate-rigidbody-in-specific-point.png)

강체는 모든 부위가 동일한 각속도 $\omega$ 로 회전한다. 강체 위 한 점 $a$ 가 무게 중심으로부터 위치 벡터 $r_a$ 만큼 떨어져 있을 때, 회전에 의해 발생하는 점 $a$ 의 선속도 성분은 $\omega \times r_a$ 가 된다. 따라서 점 $a$ 에서 병진 운동을 포함한 전체 속도 벡터 $v_a$ 는 다음과 같이 얻을 수 있다.  

$$
v_a = v + \omega \times r_a
$$

## 관성과 관성 모멘트

<table>
  <tr>
    <td>
      $$
      \begin{aligned}
      f &= m a \\
      a &= \frac{1}{m} \cdot f
      \end{aligned}
      $$
    </td>
    <td>
      $$
      \begin{aligned}
      \tau &= I \alpha \\
      \alpha &= I^{-1} \cdot \tau
      \end{aligned}
      $$
    </td>
  </tr>
  <tr>
    <td>
      질량 $m$ (물체의 관성)
    </td>
    <td>
      관성 모멘트 $I$
    </td>
  </tr>
</table>

<br />

![](/static/posts/2026-04-16-vr-simulate-rigid-body/moment-of-intertia-rotate-axis-diff.png)  

토크에 대한 저항은 같은 물체에 적용되더라도, 회전 축이 어떻게 설정되는지에 따라 달라진다. 회전축을 중심으로 물체를 절단했을 때 절단면이 넓을수록, 혹은 회전축에서 멀리 떨어진 질량이 많을수록, 관성 모멘트가 커진다.  

$$
\tau = I \alpha
$$

관성 모멘트 $I$ 는 회전축에 대해서 물체의 질량의 분포를 나타낸다. 물체를 구성하는 질량 $m$ 의 개별 미소질량 $dm$ 이 회전축으로부터의 거리 $r$ 에 대해 적분하여 관성 모멘트를 획득할 수 있다.  

$$
\begin{aligned}
I &= \int r^2 dm \\
&= \int \int \int \rho r^2 dV
\end{aligned}
$$

만약 물체의 질량 분포가 일정하다면 관성 모멘트는 행렬로 표현할 수 있다. 더 나아가, 회전축이 물체의 대칭 축과 일치한다면, 관성 모멘트는 대칭 축에 대한 질량 분포, 대각 행렬로 표현할 수도 있다.  

$$
I_\text{uniform} = \begin{bmatrix}
I_{xx} & I_{xy} & I_{xz} \\
I_{yx} & I_{yy} & I_{yz} \\
I_{zx} & I_{zy} & I_{zz}
\end{bmatrix}
$$

$$
I_\text{aligned} = \begin{bmatrix}
I_{xx} & I_{0} & I_{0} \\
I_{0} & I_{yy} & I_{0} \\
I_{0} & I_{0} & I_{zz}
\end{bmatrix}
$$

<br />

이렇게 회전하는 면에 얼마나 많은 축이 관여하는지, 어떤 도형인지에 따라서 관성 모멘트는 단순화할 수 있다.  

## 직육면체의 관성 모멘트

![](/static/posts/2026-04-16-vr-simulate-rigid-body/box-size-whd-mass-m.png)  

가로 단면 $w$, 세로 단면 $h$, 깊이 $d$ 인 직육면체의 회전은 $x$ 축, $y$ 축, $z$ 축을 기준으로만 회전할 때 아래와 같이 관성 모멘트를 계산할 수 있다.  

밀도 $\rho$ 를 갖는 어떤 직육면체에 대해 $k$ 축을 중심으로 회전하고, 이 회전축에 수직인 두 축을 $u$, $v$ 축이라고 가정하면, 각 축 방향 길이를 $L_k$, $L_u$, $L_v$ 로, 직육면체의 무게 중심이 원점일 때 각 변수의 적분 범위를 $[-\frac{L_k}{2}, \frac{L_k}{2}]$, $[-\frac{L_u}{2}, \frac{L_u}{2}]$, $[-\frac{L_v}{2}, \frac{L_v}{2}]$, 전체 질량을 $m = \rho L_k L_u L_v$ 로 정리하고, 관성 모멘트 $I$ 를 구할 수 있다.  

$$
\begin{aligned}
I_k &= \int \int \int \rho r^2 dV \\
&= \int \int \int \rho (u^2 + v^2) du dv dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \int_{-\frac{L_u}{2}}^{\frac{L_u}{2}} \int_{-\frac{L_v}{2}}^{\frac{L_v}{2}} (u^2 + v^2) du dv dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \int_{-\frac{L_u}{2}}^{\frac{L_u}{2}} \Big[ \frac{1}{3} u^3 + u v^2 \Big]_{-\frac{L_v}{2}}^{\frac{L_v}{2}} dv dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \int_{-\frac{L_u}{2}}^{\frac{L_u}{2}} ((\frac{L_u^3}{24} + \frac{L_u}{2}v^2) - (- \frac{L_u^3}{24} - \frac{L_u}{2}v^2)) dv dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \int_{-\frac{L_u}{2}}^{\frac{L_u}{2}} (\frac{L_u^3}{12} + L_u v^2) dv dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \Big[ \frac{L_u^3}{12} v + L_u \frac{1}{3} v^3 \Big]_{-\frac{L_u}{2}}^{\frac{L_u}{2}} dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} (\frac{L_u^3 L_v}{12} + \frac{L_u L_v^3}{12}) dk \\
&= \rho \int_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \frac{L_u L_v}{12} (L_u^2 + L_v^2) dk \\
&= \rho \frac{L_u L_v}{12} (L_u^2 + L_v^2) \Big[ k \Big]_{-\frac{L_k}{2}}^{\frac{L_k}{2}} \\
&= \rho \frac{L_u L_v L_k}{12} (L_u^2 + L_v^2) \\
&= \frac{1}{12} m (L_u^2 + L_v^2)
\end{aligned}
$$

$$
\begin{aligned}
I_{xx} = \frac{1}{12} m (h^2 + d^2) \\
I_{yy} = \frac{1}{12} m (w^2 + d^2) \\
I_{zz} = \frac{1}{12} m (w^2 + h^2)
\end{aligned}
$$

## 구의 관성 모멘트

![](/static/posts/2026-04-16-vr-simulate-rigid-body/sphere-mass-m.png)  

반지름 $r$ 인 구의 회전은 어느 축을 기준으로 회전하더라도 아래와 같이 관성 모멘트를 계산할 수 있다.  

질량이 $m$, 반지름이 $R$ 인 구의 밀도 $\rho$ 는 $\frac{m}{\frac{4}{3} \pi R^3}$ 를 가진다.  

$$
\rho = \frac{m}{\frac{4}{3} \pi R^3}
$$

중심으로부터의 거리 $r$, $xy$ 평면과의 각도 $\theta$, $z$ 축과의 각도 $\phi$ 를 사용하여 구면 좌표계 $(r, \theta, \phi)$ 를 사용하면, 미소부피 $dV$ 는 $r^2 \sin \phi dr d\phi d\theta$, 적분 구간은 $r$ 에 대해서 $[0, R]$, $\theta$ 에 대해서 $[0, \pi]$, $\phi$ 에 대해서 $[0, 2\pi]$ 이다.

구의 회전축을 $z$ 축으로 가정할 때, 구의 회전축에서의 거리 제곱은 $r^2 \sin^2 \phi$ 이다.  

$$
\begin{aligned}
I_z &= \int \int \int \rho r^2 \cdot \text{distance} \cdot dV \\
&= \int \int \int \rho r^2 \sin^2 \phi (r^2 \sin \phi dr d\phi d\theta) \\
&= \rho \left( \int_{0}^{2\pi} d\theta \right) \left( \int_{0}^{\pi} \sin^3 \phi d\phi \right) \left( \int_{0}^{R} r^4 dr \right) \\
\end{aligned}
$$

<br />

$$
\int_0^{2 \pi} d\theta = 2\pi
$$

$$
\int_0^{R} r^4 dr = \frac{1}{5} R^5
$$

$$
\begin{aligned}
\int_0^{\pi} \sin^3 \phi d\phi &= \int_0^{\pi} \sin \phi (1 - \cos^2 \phi) d\phi \\
&= \Big[ -\cos \phi + \frac{1}{3} \cos^3 \phi \Big]_{0}^{\pi} \\
&= \frac{4}{3}
\end{aligned}
$$

<br />

$$
\begin{aligned}
I_z &= \rho \left( \int_{0}^{2\pi} d\theta \right) \left( \int_{0}^{\pi} \sin^3 \phi d\phi \right) \left( \int_{0}^{R} r^4 dr \right) \\
&= \rho \cdot 2\pi \cdot \frac{4}{3} \cdot \frac{1}{5} R^5 \\
&= \frac{8}{15} \rho \pi R^5 \\
&= \left( \rho \frac{4}{3} \pi R^3 \right) \frac{2}{5} R^2 \\
&= \frac{2}{5} m R^2

\end{aligned}
$$

$$
I = \frac{2}{5} m R^2
$$

## 원통의 관성 모멘트

![](/static/posts/2026-04-16-vr-simulate-rigid-body/cylinder-size-rh-mass-m.png)  

반지름 $R$, 높이 $L$ 인 원통의 회전은 $x$ 축, $y$ 축, $z$ 축을 기준으로만 회전할 때 아래와 같이 관성 모멘트를 계산할 수 있다.  

중심축 기준으로 원통을 분석하면, 질량 $m$, 반지름 $R$, 길이 $L$ 인 원통의 밀도 $\rho$ 는 $\frac{m}{\pi R^2 L}$ 를 가진다.  

$$
\begin{aligned}
m &= \rho \cdot \text{Volume} \\ 
&= \rho \cdot \pi R^2 L
\end{aligned}
$$

### 중심축($z$ 축) 기준 회전

이렇게 구한 밀도 $\rho$ 를 사용하여 원통의 중심축(길이 방향, $z$ 축)을 기준으로 회전할 때의 관성 모멘트 $I$를 구할 수 있다.  

이 때 원통 좌표계 $(r, \theta, z)$ 에서,  적분 구간은, $r$ 에 대해서 $[0, R]$, $\theta$ 에 대해서 $[0, 2\pi]$, $z$ 에 대해서 $[-\frac{L}{2}, \frac{L}{2}]$ 이다.

$$
\begin{aligned}
I_z &= \int \int \int \rho r^2 dV \\
&= \int_{-\frac{L}{2}}^{\frac{L}{2}} \int_{0}^{2\pi} \int_{0}^{R} \rho r^2 (r dr d\theta dz) \\
&= \rho (\int_{-\frac{L}{2}}^{\frac{L}{2}} dz) (\int_{0}^{2\pi} d\theta) (\int_{0}^{R} r^3 dr) \\
&= \rho \cdot \Big[ z \Big]_{-\frac{L}{2}}^{\frac{L}{2}} \cdot \Big[ \theta \Big]_{0}^{2\pi} \cdot \Big[ \frac{1}{4} r^4 \Big]_{0}^{R} \\
&= \rho \cdot L \cdot 2\pi \cdot \frac{1}{4} R^4 \\
&= \frac{1}{2} \rho \pi L R^4 \\
&= \frac{1}{2} m R^2
\end{aligned}
$$

### 중심을 가로지르는 축($x$, $y$ 축) 기준 회전

회전축을 $x$ 로 가정할 때, 임의의 위치 $(x, y, z)$ 에서 $x$ 축까지의 거리 제곱은 $y^2 + z^2$ 이다. 원통 좌표계에서 $y = r \sin \theta$, $z = z$ 이므로, $x$ 축까지의 거리 제곱은 $r^2 \sin^2 \theta + z^2$ 이다.  

$$
\begin{aligned}
y &= r \sin \theta \\
z &= z \\
y^2 + z^2 &= r^2 \sin^2 \theta + z^2
\end{aligned}
$$

첫 번째 항 $r^2 \sin^2 \theta$ 는 원통의 중심축에서 멀어지는 정도에 따른 회전 저항을 나타내고, 두 번째 항 $z^2$ 는 원통의 중심에서 멀어지는 정도에 따른 회전 저항을 나타낸다.

$$
\begin{aligned}
I_x &= \int \int \int \rho (r^2 \sin^2 \theta + z^2) dV \\
&= \int_{-\frac{L}{2}}^{\frac{L}{2}} \int_{0}^{2\pi} \int_{0}^{R} \rho (r^2 \sin^2 \theta + z^2) (r dr d\theta dz) \\
\end{aligned}
$$

두 번째 항 $z^2$ 는 $\theta$ 와 $r$ 에 대해서는 상수이므로, $z^2$ 항에 대한 적분은 다음과 같이 계산할 수 있다.

$$
\begin{aligned}
\rho \int_{-\frac{L}{2}}^{\frac{L}{2}} z^2 dz \int_{0}^{2\pi} d\theta \int_{0}^{R} r dr &= \rho \Big[ \frac{1}{3} z^3 \Big]_{-\frac{L}{2}}^{\frac{L}{2}} (2 \pi) (\frac{1}{2} R^2) \\
&= \rho (\frac{L^3}{12})(\pi R^2) \\
&= \frac{1}{12} (\rho \pi L R^2) L^2 \\
&= \frac{1}{12} m L^2
\end{aligned}
$$

두 항의 적분을 모두 계산하고 한 데 정리하면 다음의 원통의 관성 모멘트를 얻을 수 있다.  

$$
\begin{aligned}
I_x = I_y &= \frac{1}{4} m R^2 + \frac{1}{12} m L^2 \\
&= \frac{1}{12} m (3R^2 + L^2)
\end{aligned}
$$

### 정리 결과

$$
I_{xx} = I_{yy} = \frac{1}{12} m (3R^2 + L^2)
$$

$$
I_{zz} = \frac{1}{2} m R^2
$$

## 외부의 특정 점에서 강체에 힘을 가할 때의 처리

![](/static/posts/2026-04-16-vr-simulate-rigid-body/external-force-specific-point.jpg)  

$$
f = m \cdot a \quad a = 1/m \cdot f
$$

$$
\tau = I \cdot \alpha \quad \alpha = I^{-1} \cdot \tau
$$

강체에 외부에서 힘이 가해질 때, 그 힘이 가해지는 위치에 따라서 강체의 병진 운동과 회전 운동이 모두 발생할 수 있다. 이 대 병진 운동과 회전 운동에 관해서는 각각 처리하여 대응할 수 있다.  

외부에서 가해진 힘 $f$ 는 도입에서 언급했듯, 작용점의 위치와 무관하게 강체의 질량 중심에 직접 작용하는 것으로 가정한다.  

$$
a = \frac{1}{m} \cdot f
$$

토크는 질량 중심이 아닌 위치에 힘이 가해졌을 때 발생한다. 토크 $\tau$ 는 질량 중심에서 작용점으로의 위치 벡터 $r$ 와 가해진 힘 $f$ 의 외적으로 구할 수 있다. 이렇게 구한 토크 $\tau$ 는 각가속도 $\alpha$ 를 구하는 데 사용될 수 있다.  

$$
\tau = r \times f
$$

$$
\alpha = I^{-1} \cdot \tau
$$
