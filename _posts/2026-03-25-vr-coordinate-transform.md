---
layout: post
title: 동차좌표계를 도입한 좌표계 변환
date: 2026-03-25
category: [virtual-reality]
---

_〈가상현실〉 수업 노트_

가상 세계를 시뮬레이션하는 데 있어, 좌표계 변환은 매우 유용하다. 오피스의 그룹화 기능처럼 특정한 오브젝트나 계를 중심으로 지역 좌표계를 설정하여 한 번에 여러 개 오브젝트를 움직이도록 하거나, 다양한 방법으로 물리 시뮬레이션을 수행하도록 할 수 있다.  

## 동차좌표계

좌표계 변환은 주로 동차좌표계(Homogeneous Coordinates)를 활용하여 구현한다.  

동차좌표계는 원래의 좌표에 새로운 축을 추가하여 $N$ 차원의 값을 $N + 1$ 차원으로 다루는 좌표계이다. 만약 어떤 3차원 좌표 $P(x, y, z)$ 가 있다면, 이 좌표의 동차 좌표는 $\tilde{P}(x, y, z, 1)$ 이다.  

동차좌표를 형성하면서, 새 축에 $1$ 을 추가했다. 이 값은 의도와 목적에 따라 다른 값이 도입될 수 있으나, 좌표계 변환에서 동차좌표계를 사용하는 목적을 고려하면 대개는 $1$ 을 도입한다. (점은 보통 마지막 성분을 $1$로, 방향 벡터는 평행 이동의 영향을 받지 않도록 마지막 성분을 $0$으로 설정한다.)  

## 좌표계 변환에서 동차좌표계의 사용

3차원 좌표계에 대해서 좌표계 변환은 다음과 같이 작업될 수 있다.  

1.  크기 변환 (Scaling):
    $$
    \begin{aligned}
    \begin{bmatrix} x_1 \\ y_1 \\ z_1 \end{bmatrix} &= \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} \\
    &= \begin{bmatrix} s_x x \\ s_y y \\ s_z z \end{bmatrix}
    \end{aligned}
    $$
2.  회전 변환 (Rotation, Z축 기준):
    $$
    \begin{aligned}
    \begin{bmatrix} x_2 \\ y_2 \\ z_2 \end{bmatrix} &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ y_1 \\ z_1 \end{bmatrix} \\
    &= \begin{bmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \\ z_1 \end{bmatrix}
    \end{aligned}
    $$
3.  이동 변환 (Translation):
    $$
    \begin{aligned}
    \begin{bmatrix} x_{final} \\ y_{final} \\ z_{final} \end{bmatrix} &= \begin{bmatrix} x_2 \\ y_2 \\ z_2 \end{bmatrix} + \begin{bmatrix} t_x \\ t_y \\ t_z \end{bmatrix} \\
    &= \begin{bmatrix} x_2 + t_x \\ y_2 + t_y \\ z_2 + t_z \end{bmatrix}
    \end{aligned}
    $$

이 세 변환 계산을 항상 모두 거친다고 가정하고, $S \rightarrow R \rightarrow T$ 의  변환 수식을 다음과 같이 정리할 수 있다.

$$
\begin{cases} 
x_{final} = (s_x x \cos\theta - s_y y \sin\theta) + t_x \\
y_{final} = (s_x x \sin\theta + s_y y \cos\theta) + t_y \\
z_{final} = s_z z + t_z 
\end{cases}
$$

위 계산 과정에서, 행렬의 덧셈 연산과 곱셈 연산이 혼재되어있다.  

만약 이동 변환이 없는 경우, 즉 $t_x = t_y = t_z = 0$ 이라면, 위 수식에서 덧셈 부분이 사라질 수 있다. 이 경우에도 여전히 곱셈 연산이 존재하기 때문에, 코드에서는 "이동 변환이 있는가?"를 판단하는 분기 처리를 도입할 것을 검토할 수도 있다.  

분기 처리 측면에서 보지 않더라도, 덧셈 계산과 곱셈 계산의 혼재는 다소 일관적이지 못하다.  

<br />

동차좌표를 사용하면, 이동 변환도 곱셈 연산으로 표현할 수 있다.  

1.  크기 변환 (Scaling):
    $$
    \begin{aligned}
    \begin{bmatrix} x_1 \\ y_1 \\ z_1 \\ 1 \end{bmatrix} &= \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} \\
    &= \begin{bmatrix} s_x x \\ s_y y \\ s_z z \\ 1 \end{bmatrix}
    \end{aligned}
    $$
2.  회전 변환 (Rotation, Z축 기준):
    $$
    \begin{aligned}
    \begin{bmatrix} x_2 \\ y_2 \\ z_2 \\ 1 \end{bmatrix} &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ y_1 \\ z_1 \\ 1 \end{bmatrix} \\
    &= \begin{bmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \\ z_1 \\ 1 \end{bmatrix}
    \end{aligned}
    $$
3.  이동 변환 (Translation):
    $$
    \begin{aligned}
    \begin{bmatrix} x_{final} \\ y_{final} \\ z_{final} \\ 1 \end{bmatrix} &= \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_2 \\ y_2 \\ z_2 \\ 1 \end{bmatrix} \\
    &= \begin{bmatrix} x_2 + t_x \cdot 1 \\ y_2 + t_y \cdot 1 \\ z_2 + t_z \cdot 1 \\ 1 \end{bmatrix} \\
    &= \begin{bmatrix} x_2 + t_x \\ y_2 + t_y \\ z_2 + t_z \\ 1 \end{bmatrix}
    \end{aligned}
    $$


이 세 변환 계산을 항상 모두 거친다고 가정하고, 변환 수식을 다음과 같이 정리할 수 있다.

$$
\begin{bmatrix} x_{final} \\ y_{final} \\ z_{final} \\ 1 \end{bmatrix} = \begin{bmatrix} s_x\cos\theta & -s_y\sin\theta & 0 & t_x \\ s_x\sin\theta & s_y\cos\theta & 0 & t_y \\ 0 & 0 & s_z & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

$$
\begin{cases} 
x_{final} = s_x x \cos\theta - s_y y \sin\theta + t_x \\
y_{final} = s_x x \sin\theta + s_y y \cos\theta + t_y \\
z_{final} = s_z z + t_z 
\end{cases}
$$

<br />

동차좌표계를 이용하여 좌표계 변환을 구현하면, 위 과정과 같이 변환 연산을 최적화하여 일련의 변환 처리를 한 번의 행렬곱으로 구현할 수 있다. 동차좌표계를 사용하지 않은 상황에서는 회전과 크기 변환은 단일한 행렬곱으로 표현하는 것이 가능했지만, 이동 변환을 별개로 더 계산해야 했다.  

한 회의 변환 처리를 두 단계로 나누어 처리하면 변환을 연속적으로 적용해야 하는 상황에서 계산 처리가 매우 복잡해진다.  

<br />

어떤 변환을 10회 연달아 처리해야 하는 상황을 가정한다. 일반 좌표계에서는 단계마다 덧셈 항이 누적되어 수식이 기하급수적으로 복잡해지지만, 동차좌표계에서는 단순한 행렬 곱셈으로 완결할 수 있다.  

1. 1단계: $P_1 = M_1 P_0 + T_1$
2. 2단계: $\begin{aligned}P_2 &= M_2 (M_1 P_0 + T_1) + T_2 \\ &= (M_2 M_1) P_0 + (M_2 T_1 + T_2)\end{aligned}$
3. 3단계: $\begin{aligned}P_3 &= M_3 (M_2 M_1 P_0 + M_2 T_1 + T_2) + T_3 \\ &= (M_3 M_2 M_1) P_0 + (M_3 M_2 T_1 + M_3 T_2 + T_3)\end{aligned}$

이 표현을 동차좌표계의 도입으로 이와 같이 표현할 수 있다.

- $P_{final} = (M_{10} \cdot M_9 \cdot \dots \cdot M_2 \cdot M_1) \cdot P_0$

<br />

변환을 연달아 수행하는 상황은 하나의 대상에만 변환을 수행하는 것만을 의미하지 않는다. 각 객체가 부모-자식 관계의 계층 구조를 갖는 복잡한 객체의 경우, 부모의 움직임은 자식에게 자동으로 전파되어야 한다.  

변환의 전파는 연쇄적인 행렬곱으로 쉽게 구현할 수 있다. 인체 모델에서 어깨, 팔꿈치, 손목, 손가락으로 이어지는 변환을 처리하고자 할 때 다음과 같이 작성할 수 있다.  

$$
M_{global, 손가락} = M_\text{어깨} \cdot M_\text{팔꿈치} \cdot M_\text{손목} \cdot M_\text{손가락}
$$

이렇게 하여, $M_\text{어깨}$ 가 회전하는 상황에서는, 그 하위의 팔꿈치, 손목, 손가락이 추가적인 계산 없이, 곱셈 결과에 의해 자동으로 어깨를 축으로 함께 회전할 수 있다.  

만약 동차좌표계를 쓰지 않고 일반 좌표계에서 덧셈(이동)과 곱셈(회전)을 섞어서 이 계층 구조를 구현하려 한다면, 부모가 회전할 때마다 자식의 이동 경로를 매번 새로 계산해야 할 것이다.  

## 복합 변환

![](/static/posts/2026-03-25-vr-coordinate-transform/complex_transform.png)  

동차좌표계를 이용해 이동, 회전, 크기 변환을 하나의 행렬로 수행할 수 있다. 다만 이들 처리를 수행할 때, 변환의 대상이 어떤 계에 속한 일부 객체인지, 혹은 계 전체인지에 따라 복합 변환의 적용 과정이 조금 다르다.  

<br />

계(System) 안의 특정한 정점이 변환의 대상인 경우는 물체 변환(Object Transformation)이라고 한다. 고정된 기준 좌표계에서 물체의 점이나 형상을 직접 이동, 회전, 확대한다.  

$$
\begin{aligned}
P_\text{world} &= T \cdot (R \cdot (S \cdot P_\text{local})) \\
&= T \cdot R \cdot S \cdot P_\text{local} \\
&= M \cdot P_\text{local}
\end{aligned}
$$

변환은 크기 변환 $S$, 회전 $R$, 이동 $T$ 순서로 적용된다.  

회전 $R$ 과 크기 변환 $S$ 는 원점 $(0, 0, 0)$ 을 기준으로 정의되어있다. 때문에 이동 $T$ 가 회전과 크기 변환보다 먼저 적용되면, 이동이 회전과 크기 변환의 축과 원점에 영향을 주게 된다. 이동 $T$ 의 영향으로 원점으로부터 떨어지게 되면, 나머지 두 변환은 "원래의 원점을 중심으로 하는 거대한 궤도 회전", 혹은 "원점으로부터의 거리 확대"가 되므로, 의도한 변환과는 다른 결과가 나올 수 있다.  

<br />

계 전체가 변환의 대상인 경우에는 좌표계 변환(Coordinate Transformation)을 사용한다. 점을 직접 움직이는 대신, 그 점이 표현되는 로컬 좌표계의 축과 원점을 변환한다. 각 단계의 다음 변환은 이전 단계에서 이미 변형된 로컬 좌표계를 기준으로 적용된다.  

변환은 이동 $T$, 회전 $R$, 크기 변환 $S$ 순서로 적용된다. 이동이 회전보다 먼저 적용되면, 이동이 회전에 의해 영향을 받지 않고, 이동이 회전의 축과 원점에 영향을 주지 않기 때문이다.  

$$
\begin{aligned}
P_\text{world} &= S \cdot (R \cdot (T \cdot P_\text{local})) \\
&= S \cdot R \cdot T \cdot P_\text{local} \\
&= M \cdot P_\text{local}
\end{aligned}
$$

## 예시 상황 \#1

로컬 좌표계의 정점 $P_\text{local} (2, 1)$ 에 대해서, 세 가지 변환을 순서대로 적용할 때, 최종 월드 좌표 $P_\text{world}$ 는 다음과 같이 구할 수 있다.  

1. 모든 축으로 2배 확대
2. 반시계 방향으로 90도 회전
3. $x$ 축으로 3, $y$ 축으로 2 만큼 이동

이 문제는 점 자체를 절대 좌표계에서 직접 변환하는 것이 아니라, 로컬 좌표계가 순차적으로 이동, 회전, 확대되며 정의되는 상황으로 해석할 수 있으므로 좌표계 변환으로 처리한다. 따라서 각 변환 행렬 $S$, $R$, $T$ 가 다음과 같을 때, $P_\text{world}$ 는 $S \cdot R \cdot T \cdot P_\text{local}$ 로 구할 수 있다.

$$
\begin{aligned}
S &= \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \\
R &= \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \\
T &= \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}
\end{aligned}
$$

$$
\begin{aligned}
P_\text{world} &= S \cdot R \cdot T \cdot P_\text{local} \\
&= \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix} \\
&= \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 5 \\ 3 \\ 1 \end{bmatrix} \\
&= \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} -3 \\ 5 \\ 1 \end{bmatrix} \\
&= \begin{bmatrix} -6 \\ 10 \\ 1 \end{bmatrix}
\end{aligned}
$$

## 예시 상황 \#2

좌표계 $\{A\}$ 는 전역 좌표계 $\{W\}$ 에 대해서 $x_\text{W}$ 방향으로 $+3$, $y_\text{W}$ 방향으로 $+2$, 반시계 방향으로 $90 ^\circ$ 회전한 상태이다.  

$$
^W T _A = \begin{bmatrix} 0 & -1 & 3 \\ 1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}
$$

전역 좌표계의 어떤 점 $p$ 가 $(5, 6)$ 일 때, 좌표계 $\{A\}$ 에서의 점 $p_A$ 는 다음과 같이 구할 수 있다.  

$$
^W p = \begin{bmatrix} 5 \\ 6 \end{bmatrix}
$$

$$
\begin{aligned}
^A p &= ^A T _W \cdot ^W p \\
&= (^W T _A)^{-1} \cdot ^W p \\
&= \begin{bmatrix} 0 & 1 & -2 \\ -1 & 0 & 3 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 5 \\ 6 \\ 1 \end{bmatrix} \\
&= \begin{bmatrix} 4 \\ -2 \\ 1 \end{bmatrix}
\end{aligned}
$$

$$
\therefore \  ^A p = (4, -2)
$$

## 마무리

정리해서, 동차좌표계의 도입으로 결합 법칙을 사용하여, 정점 $P_0$ 에 변환을 적용하기 전에 여러 단계의 변환 처리를 미리 하나의 변환행렬로 압축해낼 수 있다.  

이렇게 압축한 변환 행렬은 어떤 정점에 사용하든, 한 번의 행렬 곱셈으로 변환을 적용하여 계산량을 줄일 수 있다.  

부모-자식 관계가 있는 복잡한 계층 구조의 모델을 구현할 때, 상위 단계의 변환이 하위 단계의 변환으로 전파되므로, 그 구현이 직관적이고 단순해진다.  
