---
layout: post
title: 강체 시뮬레이션에서의 수치적분
date: 2026-04-16
category: [virtual-reality]
---

_〈가상현실〉 수업 노트_

<br />

[&lt;강체 시뮬레이션&gt;](/posts/2026-04-16-vr-simulate-rigid-body/)에서 확인할 수 있듯, 강체의 운동을 처리하는 데에는 적분 계산이 요구된다.  

계산기에서는 적분 계산에 있어 방정식을 해석적으로 풀 수 없으므로, 적분 대상을 잘게 나누어 근사적으로 계산하는 수치적분 방법을 사용한다.  

$$
\begin{aligned}
v = \int a \, dt &\approx \sum_{i}{a_i} \Delta t \\
x = \int v \, dt &\approx \sum_{i}{v_i} \Delta t
\end{aligned}
$$

## 오일러 방법

![](/static/posts/2026-04-16-vr-numerical-integration-in-rigid-body-simulation/euler_method.png)  

_전진 오일러 방법(좌)과 후진 오일러 방법(우)_  

오일러 방법은 가장 간단한 수치적분 방법으로, 크게 두 가지 방법을 사용할 수 있다. 전진 오일러 방법(Forward Euler method, 외삽법; Explict method라고도 함)과 후진 오일러 방법(Backward Euler method, 내삽법; Implicit method라고도 함)이 있다.  

<br />

$$
\begin{aligned}
v_{i+1} &= v_i + a_i \Delta t \\
x_{i+1} &= x_i + v_i \Delta t
\end{aligned}
$$

_전진 오일러 방법의 정의_

<br />

$$
\begin{aligned}
v_{i+1} &= v_i + a_{i+1} \Delta t \\
x_{i+1} &= x_i + v_{i+1} \Delta t
\end{aligned}
$$

_후진 오일러 방법의 정의_

## 전진 오일러 방법

전진 오일러 방법은 현재 시간을 기준으로, 후진 오일러 방법은 다음 시간을 기준으로 잘게 자른 시간 간격 $\Delta t$ 동안의 가속도 $a$ 와 속도 $v$ 를 사용하여 적분 계산을 수행한다.  

<br />

전진 오일러 방법은 계산이 간단하지만, 시간이 진행됨에 따라 오차가 누적되어 시뮬레이션이 불안정해진다.  

아래 식과 같이 강체에 힘을 가하는 상황에서, 전진 오일러 방법을 사용하여 시뮬레이션을 수행할 때, 시뮬레이션이 불안정해지는 것을 확인할 수 있다.  

$$
y = - \frac{1}{2} g t^2 + 10, \quad g = 2
$$

$$
\dot{y}_{i + 1} = \dot{y}_i - g \Delta t, \quad y_{i + 1} = y_i + \dot{y}_i \Delta t
$$

| $t$ | exact $y$ | $y_i$ | $\dot{y}_i$ | $\Delta$ |
| :-: | :-: | :-: | :-: | :-: |
| 0 | 10 | 10 | 0 | 0 |
| 1 | 9 | 10 | -2 | -1 |
| 2 | 6 | 8 | -4 | -2 |
| 3 | 1 | 4 | -6 | -3 |
| 4 | -6 | -2 | -8 | -4 |

<br />

이렇게 오차가 누적되면, 모델을 렌더링하는 경우에는 각 정점이 발산하여 모델이 터지듯 사라진다.  

이전 시간 스텝과 다음 시간 스텝의 관계를 아래와 같이 정리할 때, 행렬 $A$ 가 단위 행렬보다 큰 경우, 시뮬레이션이 발산하는 것을 확인할 수 있다.  

$$
X_{t + 1} = A X_t
$$

$$
\text{if} \left\| A \right\| > 1 \text{ then } X \text{diverges}
$$


따라서 위 식에서 행렬 $A$ 의 고유값(eigenvalue)의 크기(절댓값)가 1 이하인 경우($\|\lambda\| \le 1$)에만 시뮬레이션이 안정적으로 수렴한다.  

## 후진 오일러 방법

후진 오일러 방법은 다음 시간을 기준으로 삼으면서, 전진 오일러 방법보다 계산이 복잡하다.  

$$
\begin{aligned}
v_{t + 1} &= v_t + a_{t + 1} \Delta t \\
x_{t + 1} &= x_t + v_{t + 1} \Delta t
\end{aligned}
$$

$$
\begin{aligned}
x_{t + 1} &= x_t + v_{t + 1} \Delta t \\
v_{t + 1} &= v_t + a_{t + 1} \Delta t \\
&= v_t + \left(- \frac{k (x_{t + 1} - x_0)}{m}\right) \Delta t \\
&= v_t - \frac{k \Delta t}{m} x_{t + 1} + \frac{k \Delta t}{m} x_0
\end{aligned}
$$

<br />

$x_{t + 1}$ 과 $v_{t + 1}$ 을 행렬 꼴 $s_{t + 1}$ 로 표현하면, 아래와 같이 $t + 1$ 과 $t$ 항으로 정리할 수 있다.  

$$
\begin{aligned}
x_{t + 1} - v_{t + 1} \Delta t &= x_t \\
v_{t + 1} + \frac{k \Delta t}{m} x_{t + 1} &= v_t + \frac{k \Delta t}{m} x_0 
\end{aligned}
$$

$$
\begin{aligned}
\begin{bmatrix}
1 & -\Delta t \\
\frac{k \Delta t}{m} & 1
\end{bmatrix} \begin{bmatrix}x_{t + 1} \\
v_{t + 1}
\end{bmatrix} &= \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} \begin{bmatrix}x_t \\
v_t
\end{bmatrix} + \begin{bmatrix}
0 \\
\frac{k \Delta t}{m} x_0
\end{bmatrix}
\end{aligned}
$$


$$
\begin{aligned}
S_{t + 1} &= \begin{bmatrix}x_{t + 1} \\
v_{t + 1}
\end{bmatrix} \\
A S_{t + 1} &= B S_t + C \\
S_{t + 1} &= A^{-1} B S_t + A^{-1} C
\end{aligned}
$$

<br />


행렬 $A$의 역행렬을 구하기 위해 행렬식을 계산하면 다음과 같다. $A$가 $2 \times 2$ 행렬이므로 역행렬 공식을 쉽게 적용할 수 있다. 수식의 편의를 위해 행렬식 $\det(A)$를 $D$로 치환한다.

$$
\begin{aligned}
D = \det(A) &= (1 \cdot 1) - \left(-\Delta t \cdot \frac{k \Delta t}{m}\right) = 1 + \frac{k \Delta t^2}{m} \\
A^{-1} &= \frac{1}{D} \begin{bmatrix}
1 & \Delta t \\
-\frac{k \Delta t}{m} & 1
\end{bmatrix}
\end{aligned}
$$

<br />

$B$는 단위행렬이므로 전이 행렬 $A^{-1}B$는 $A^{-1}$과 같다.

$$
\begin{aligned}
A^{-1} B &= \frac{1}{D} \begin{bmatrix}
1 & \Delta t \\
-\frac{k \Delta t}{m} & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} \\
&= \begin{bmatrix}
\frac{1}{D} & \frac{\Delta t}{D} \\
-\frac{k \Delta t}{m D} & \frac{1}{D}
\end{bmatrix}
\end{aligned}
$$

이렇게 산출한 점화식 $S_{t + 1} = A^{-1} B S_t + A^{-1} C$ 의 고유값(eigenvalue) 크기는 1보다 작다. 특성 방정식 $\det(A^{-1} B - \lambda I) = 0$ 을 통해 이를 증명할 수 있다.

$$
\det \begin{bmatrix}
\frac{1}{D} - \lambda & \frac{\Delta t}{D} \\
-\frac{k \Delta t}{m D} & \frac{1}{D} - \lambda
\end{bmatrix} = 0
$$

$$
\begin{aligned}
\left(\frac{1}{D} - \lambda\right)^2 - \left(\frac{\Delta t}{D}\right)\left(-\frac{k \Delta t}{m D}\right) &= 0 \\
\left(\frac{1}{D} - \lambda\right)^2 + \frac{k \Delta t^2}{m D^2} &= 0 \\
\left(\frac{1}{D} - \lambda\right)^2 &= - \frac{k \Delta t^2}{m D^2}
\end{aligned}
$$

우변이 음수이므로 고유값 $\lambda$ 는 복소수 식으로 도출된다.

$$
\begin{aligned}
\frac{1}{D} - \lambda &= \pm i \frac{\sqrt{\frac{k}{m}} \Delta t}{D} \\
\lambda &= \frac{1 \pm i \sqrt{\frac{k}{m}} \Delta t}{D} = \frac{1 \pm i \sqrt{\frac{k}{m}} \Delta t}{1 + \frac{k \Delta t^2}{m}}
\end{aligned}
$$

시뮬레이션이 안정적이려면 고유값의 크기(절댓값)가 1 이하여야 한다. 복소수 $\lambda = a + bi$ 의 크기 제곱 $\|\lambda\|^2 = a^2 + b^2$ 이므로 다음과 같이 계산된다.

$$
\begin{aligned}
|\lambda|^2 &= \left( \frac{1}{1 + \frac{k \Delta t^2}{m}} \right)^2 + \left( \frac{\sqrt{\frac{k}{m}} \Delta t}{1 + \frac{k \Delta t^2}{m}} \right)^2 \\
&= \frac{1 + \frac{k \Delta t^2}{m}}{\left(1 + \frac{k \Delta t^2}{m}\right)^2} \\
&= \frac{1}{1 + \frac{k \Delta t^2}{m}}
\end{aligned}
$$

질량 $m > 0$, 스프링 상수 $k > 0$, 시간 간격 $\Delta t > 0$ 이므로 $\frac{k \Delta t^2}{m} > 0$ 이다. 따라서 분모가 무조건 1보다 커지게 된다.

$$
|\lambda|^2 < 1 \quad \Rightarrow \quad |\lambda| < 1
$$

이 증명을 통해 후진 오일러 방법은 $\Delta t$ 의 크기와 무관하게 고유값의 크기가 항상 1보다 작으므로, 시뮬레이션이 무조건적으로 안정적임을 알 수 있다. (다만 $\|\lambda \| < 1$ 로 인해 에너지가 매 스텝 감소하므로 점차 움직임이 줄어드는 수치적 감쇠(Numerical Damping) 현상이 발생한다.)
