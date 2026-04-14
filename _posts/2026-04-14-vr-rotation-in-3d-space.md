---
layout: post
title: 3차원 공간에서의 회전 처리
date: 2026-04-14
category: [virtual-reality]
---

_〈가상현실〉 수업 노트_

## 오일러각

![](./vr-rotation-in-3d-space/unity-transform.png)  

3차원 공간에서 어떤 물체의 회전 상태를 표현할 때, $x$, $y$, $z$ 로 위치 값으로 표현한 것에서 기인하여 익숙한 형태인 $(x, y, z)$ 벡터로 표현하곤 한다. 이렇게 표현하고자 한다면, 실제로 이 벡터의 값은 아래와 같이, $x$, $y$, $z$ 축을 기준으로 물체가 얼마나 회전하였는지 나타낼 수 있을 것이다.  

![](./vr-rotation-in-3d-space/rotate-based-in-axes.png)  


## 고정된 축 기준 회전 표현

![](./vr-rotation-in-3d-space/euler-2-stage-rotate.png)  

하지만 단순 축 기준 표현으로는 물체와 함께 회전축도 회전하므로, 여러 개 축에 대해서 회전을 적용할 때 그 결과가 기대와는 다르게 나타날 것이다. 그래서 회전을 어떤 축에 대한 회전으로 표현하려면 회전을 정의하는 축이 고정되어야 한다.  

축을 고정하여 Roll, Pitch, Yaw 축을 정의하고, 이 축을 기준으로 반시계 방향으로 얼마나 회전하는지 표현할 수 있다.  

![](./vr-rotation-in-3d-space/airplane-rotate-based-in-fixed-axes.png)  

<br />

![](./vr-rotation-in-3d-space/fixed-angle-def-airplane.png)  

$$
R = (\theta, \phi, \psi)
$$


## 회전 행렬

3차원 공간에서의 회전을 일관성 있게 계산하기 위해서 회전 행렬을 사용한다.  

3차원에서 각 축을 기준으로 행렬을 정의한다면 $R_x(\theta)$, $R_y(\phi)$, $R_z(\psi)$ 는 다음과 같이 표현할 수 있다.  

$$
R_x(\theta) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos \theta & -\sin \theta \\
0 & \sin \theta & \cos \theta
\end{bmatrix}
$$

_$x$ 축(Pitch) 고정, $y$ - $z$ 평면에서 회전_

<br />

$$
R_y(\phi) =
\begin{bmatrix}
\cos \phi & 0 & \sin \phi \\
0 & 1 & 0 \\
-\sin \phi & 0 & \cos \phi
\end{bmatrix}
$$

_$y$ 축(Roll) 고정, $x$ - $z$ 평면에서 회전_

<br />

$$
R_z(\psi) =
\begin{bmatrix}
\cos \psi & -\sin \psi & 0 \\
\sin \psi & \cos \psi & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

_$z$ 축(Yaw) 고정, $x$ - $y$ 평면에서 회전_

## 회전 계산과 교환법칙

두 개 이상의 축에 대해 회전을 표현할 때, 회전 순서에 따라 결과가 달라질 수 있다.  

<br />

$(\hat{x}, \hat{y}, \hat{z}) = (30, 45, 0)$ 를 적용할 때 $x$ 축을 기준으로 먼저 회전을 적용한 후, $y$ 축을 기준으로 회전을 적용한다면, 아래와 같이 표현할 수 있다.  

$$
\begin{aligned}
\begin{bmatrix}
\hat{x} \\
\hat{y} \\
\hat{z}
\end{bmatrix}
&=
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos 30^\circ & -\sin 30^\circ \\
0 & \sin 30^\circ & \cos 30^\circ
\end{bmatrix}
\begin{bmatrix}
\cos 45^\circ & 0 & \sin 45^\circ \\
0 & 1 & 0 \\
-\sin 45^\circ & 0 & \cos 45^\circ
\end{bmatrix}
\begin{bmatrix}x \\
y \\
z
\end{bmatrix} \\
&=
\begin{bmatrix}\cos 45^\circ & 0 & \sin 45^\circ \\
\sin 30^\circ \sin 45^\circ & \cos 30^\circ & -\sin 30^\circ \cos 45^\circ \\
-\cos 30^\circ \sin 45^\circ & \sin 30^\circ & \cos 30^\circ \cos 45^\circ
\end{bmatrix}
\begin{bmatrix}x \\
y \\
z
\end{bmatrix}
\end{aligned}
$$

하지만 $y$ 축을 기준으로 먼저 회전을 적용한 후, $x$ 축을 기준으로 회전을 적용한다면, 아래와 같이 표현할 수 있다.

$$
\begin{aligned}
\begin{bmatrix}
\hat{x} \\
\hat{y} \\
\hat{z}
\end{bmatrix}
&=
\begin{bmatrix}\cos 45^\circ & 0 & \sin 45^\circ \\
0 & 1 & 0 \\
-\sin 45^\circ & 0 & \cos 45^\circ
\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\
0 & \cos 30^\circ & -\sin 30^\circ \\
0 & \sin 30^\circ & \cos 30^\circ
\end{bmatrix}
\begin{bmatrix}x \\
y \\
z
\end{bmatrix} \\
&=
\begin{bmatrix}\cos 45^\circ & \sin 30^\circ \sin 45^\circ & \sin 30^\circ \cos 45^\circ \\
0 & \cos 30^\circ & -\sin 30^\circ \\
-\sin 45^\circ & \cos 30^\circ \sin 45^\circ & \cos 30^\circ \cos 45^\circ
\end{bmatrix}
\begin{bmatrix}x \\
y \\
z
\end{bmatrix}
\end{aligned}
$$

$x$ 축을 기준으로 회전을 적용한 후 $y$ 축을 기준으로 회전을 적용하는 변환 $R_{x \rightarrow y}$ 와 $y$ 축을 기준으로 회전을 적용한 후 $x$ 축을 기준으로 회전을 적용하는 변환 $R_{y \rightarrow x} = R_y R_x$ 는 서로 다르다. 회전 계산에서는 교환법칙이 성립하지 않는다.    

$$
\begin{aligned}
R_{x \rightarrow y} &\neq R_{y \rightarrow x} \\
\begin{bmatrix}\cos 45^\circ & 0 & \sin 45^\circ \\
\sin 30^\circ \sin 45^\circ & \cos 30^\circ & -\sin 30^\circ \cos 45^\circ \\
-\cos 30^\circ \sin 45^\circ & \sin 30^\circ & \cos 30^\circ \cos 45^\circ
\end{bmatrix}
&\neq
\begin{bmatrix}\cos 45^\circ & \sin 30^\circ \sin 45^\circ & \sin 30^\circ \cos 45^\circ \\
0 & \cos 30^\circ & -\sin 30^\circ \\
-\sin 45^\circ & \cos 30^\circ \sin 45^\circ & \cos 30^\circ \cos 45^\circ
\end{bmatrix}
\end{aligned}
$$

따라서 회전 순서는 항상 일관되도록 주의하여야 한다. 유니티에서는 회전 순서를 $z$ 축, $x$ 축, $y$ 축 순으로 적용, ZXY 회전을 사용한다. 따라서 유니티에서 $(30, 45, 0)$ 의 오일러각을 적용한다면, $z$ 축을 기준으로 먼저 회전을 적용한 후, $x$ 축을 기준으로 회전을 적용한 후, $y$ 축을 기준으로 회전을 적용하는 변환이 적용된다.  

$$
\begin{aligned}
A_\text{final} &= R_y(\phi) \cdot (R_x(\theta) \cdot (R_z(\psi) \cdot A_\text{initial})) \\
&= R_y(\phi) R_x(\theta) R_z(\psi) \cdot A_\text{initial} \\
\end{aligned}
$$

$$
R = R_y(\phi) R_x(\theta) R_z(\psi)
$$

## 짐벌 구조로 표현하기

![](./vr-rotation-in-3d-space/xyz-gimbal.jpg)  

이렇게 고정 축에 대해서 회전을 정의할 때, 각 축을 짐벌로 표현하여, Pitch를 $x$ 짐벌, Roll을 $y$ 짐벌, Yaw를 $z$ 짐벌로 간주한다. 이렇게 표현하는 데에는, 계산 순서에 따라, 회전이 반영되는 범위가 다르기 때문이다.  

짐벌은 계산 순서에 따라 위 그림과 같이, 먼저 계산되는 축이 가장 안쪽, 마지막 계산되는 축이 가장 바깥쪽에 위치한다. 유니티의 계산 순서와 같이 회전 행렬 $R$ 이 정의된다면, $R$ 은 다음과 같이 정의된다.  

$$
\begin{aligned} 
R &= R_y(\phi) \cdot (R_x(\theta) \cdot (R_z(\psi) \cdot A_\text{initial})) \\
&= R_y(\phi) R_x(\theta) A_{z \text{-rotated}} \\
\end{aligned}
$$

유니티에서는 $R_z(\psi)$ 에 의한 변환이 적용된 후, $R_x(\theta)$ 에 의한 변환이 적용된다. $R_z(\psi)$ 의 변환분이 이후에 적용되는 $R_x(\theta)$ 의 변환분의 영향을 받는다고 이해할 수 있다. 때문에 위 사진과 같이 짐벌 구조로 나타난다.  

## 짐벌락

![](./vr-rotation-in-3d-space/gimbal-lock.jpg)

짐벌 구조에서 Pitch($x$)가 $90^\circ$ 가 되면, Roll($y$)과 Yaw($z$) 축이 일치하면서, 두 회전축이 같은 방향을 바라보게 된다. 이렇게 되면 3차원 공간에서, 3개의 회전 자유도 중 1개를 잃고 2개의 축으로만 회전할 수 있는 상태가 되는데, 이 상태를 짐벌락(Gimbal Lock) 이라고 한다.

<br />

$R = R_y(\phi) R_x(\theta) R_z(\psi)$ 에서 $x$ 축 회전각 $\theta$ 가 $90^\circ$ 가 되면, $R_x(\theta)$ 는 다음과 같이 표현된다.

$$
R_x(90^\circ) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & -1 \\
0 & 1 & 0
\end{bmatrix}
$$

$$
\begin{aligned}
R &= R_y(\phi) R_x(90^\circ) R_z(\psi) \\
&=
\begin{bmatrix}
\cos \phi & 0 & \sin \phi \\
0 & 1 & 0 \\
-\sin \phi & 0 & \cos \phi
\end{bmatrix}
\begin{bmatrix}1 & 0 & 0 \\
0 & 0 & -1 \\
0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}\cos \psi & -\sin \psi & 0 \\
\sin \psi & \cos \psi & 0 \\
0 & 0 & 1
\end{bmatrix} \\
&=
\begin{bmatrix}\cos \phi \cos \psi + \sin \phi \sin \psi & -\cos \phi \sin \psi + \sin \phi \cos \psi & 0 \\
0 & 0 & -1 \\
-\sin \phi \cos \psi + \cos \phi \sin \psi & \sin \phi \sin \psi + \cos \phi \cos \psi & 0
\end{bmatrix} \\
&= \begin{bmatrix}\cos (\phi - \psi) & \sin (\phi - \psi) & 0 \\
0 & 0 & -1 \\
- \sin (\phi - \psi) & \cos (\phi - \psi) & 0
\end{bmatrix}
\end{aligned}
$$

정리된 마지막 행렬에서, $y$ 축 회전값 $\phi$ 와 $z$ 축 회전값 $\psi$ 가 하나의 회전값 $\phi - \psi$ 로 표현되고 있다. 따라서 $y$ 축 회전값 $\phi$ 를 조정하여 달성할 수 있는 회전을 $z$ 축 회전값 $\psi$ 를 조정하여서도 달성할 수 있다. $y$ 축과 $z$ 축은 종속 관계가 되었다.  

## 쿼터니언

짐벌락 문제를 해결하기 위해서, 쿼터니언을 사용해 회전을 처리할 수 있다.  

$$
q = w + x\mathbf{i} + y\mathbf{j} + z\mathbf{k}
$$

- $w$ : 실수부, 회전의 각도와 관련된 스칼라 값
- $x$, $y$, $z$ : 허수부, 회전의 축과 관련된 벡터 값
- $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ : 허수 단위, 서로 직교하는 3차원 공간의 단위 벡터

$$
q = (w, x, y, z)
$$

쿼터니언은 단위 벡터 $\mathbf{u}$ 의 임의의 축을 기준으로 $\theta$ 만큼 회전한다고 표현할 수 있는데, 이것을 축-각도 표현(axis-angle representation) 이라고 한다.  

$$
\begin{aligned}
q &= (cos \frac{\theta}{2}, sin \frac{\theta}{2} \mathbf{u}) \\
&= (cos \frac{\theta}{2}, sin \frac{\theta}{2} u_x, sin \frac{\theta}{2} u_y, sin \frac{\theta}{2} u_z)
\end{aligned}
$$

$q$ 는 $\left| q \right| = 1$ 인 단위 쿼터니언이다. 3차원 벡터 $\mathbf{v}$ 를 쿼터니언을 이용해 회전시킬 때 $q \mathbf{v} q^{-1}$ 로 처리하므로, $\theta$ 만큼의 회전에 대해서 $\theta / 2$ 로 계산한다.  

$$
R = q \mathbf{v} q^{-1}
$$

$q$ 의 역 쿼터니언 $q^{-1}$ 은 켤레(conjugate) 쿼터니언이다. 쿼터니언의 허수부가 오일러각의 회전축을 나타내고 있으므로 Conjugate 쿼터니언은 회전축의 방향을 반전하는 것으로 이해할 수 있다. 회전축이 반전되므로, $q^{-1}$ 은 $q$ 가 표현하는 회전의 역방향 회전을 표현한다.  

$$
q^{-1} = q^{*} = (w, -x, -y, -z)
$$

<br />

렌더링 파이프라인에서는 $3 \times 3$ 혹은 $4 \times 4$ 회전 행렬을 요구하므로, 쿼터니언을 회전 행렬로 변환하여야 한다. $q = (w, x, y, z)$ 에 대해서, $3 \times 3$ 회전 행렬 $R$ 는 다음과 같이 표현할 수 있다.  

$$
R(q) = \begin{bmatrix}
1 - 2(y^2 + z^2) & 2(xy - wz) & 2(xz + wy) \\
2(xy + wz) & 1 - 2(x^2 + z^2) & 2(yz - wx) \\
2(xz - wy) & 2(yz + wx) & 1 - 2(x^2 + y^2)
\end{bmatrix}
$$

> 위 식에서 쿼터니언 계산의 장점을 하나 더 확인할 수 있다. 회전 행렬에서는 $\theta$ 만큼의 회전을 표현하는 데 있어, 매 처리마다 삼각함수 연산을 수행했다. 쿼터니언에서는 이미 쿼터니언의 정의 식에서 계산된 삼각함수 값에 근거해 회전 행렬을 계산한다. 쿼터니언을 사용한 회전 행렬의 처리 과정은, 삼각함수 계산 소요가 상대적으로 적다.  

