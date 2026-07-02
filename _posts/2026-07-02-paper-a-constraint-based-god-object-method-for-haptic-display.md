---
layout: post
title: A constraint-based god-object method for haptic display 리뷰
date: 2026-07-02
categories: [paper]
tags: [paper, ieee/rsj, vr, haptic]
---

[Zilles, Craig B., and J. Kenneth Salisbury. "A constraint-based god-object method for haptic display." Proceedings 1995 ieee/rsj international conference on intelligent robots and systems. Human robot interaction and cooperative robots. Vol. 3. IEEE, 1995.](https://ieeexplore.ieee.org/document/525876)

〈가상현실〉 수업 참고자료

## 햅틱 시스템

햅틱 시스템은 데이터를 인간의 촉각이 수용할 수 있게 입출력하는 시스템이다. 최근에는 스마트폰의 발달로 햅틱 자체가 휴대폰의 진동 모터, 그리고 이 진동 모터를 응용하는 키보드 입력 피드백, UI/UX 상의 진동 피드백 등으로 한정되어 생각되는 경향이 있는데, 실제로는 더 광의의 의미를 가진다.  

햅틱 시스템도 다른 입출력 시스템과 마찬가지로 입력 장치와 출력 장치로 구성된다. 입력 장치는 사용자의 손이나 팔, 혹은 다른 신체 부위의 움직임을 감지하는 햅틱 센서, 그리고 출력 장치는 사용자의 손이나 팔, 혹은 다른 신체 부위에 힘을 가하는 햅틱 디스플레이로 명칭된다.  

## 연구 배경

가상의 물체를 햅틱 시스템을 통해 인간이 느낄 수 있게, '만질 수 있게' 하려면, 햅틱 시스템은 현실의 허공에 가상의 물체를 물리적인 힘으로서 표현해야 한다.  

현실에서는 인간이 어떤 물체를 누르면 작용-반작용 법칙에 따라 물체가 신체에게 역방향으로 힘을 가하고, 인간은 그 힘을 느끼면서 물체의 존재를 인식할 수 있다.  

이 반작용 힘을 가상 세계에서도 재현하려면, 햅틱 시스템이 이 반작용 힘을 출력할 수 있도록 힘 정보를 결정해야 한다.  

<br />

이전 연구에서는 햅틱 시스템이 현실에서 받아들인 값을 바탕으로, 현실의 입력 점이 가상 물체에 얼마나 깊게 침투했는지를 계산하고, 이 침투 상황을 원래대로 복원하기 위한 수준으로 반작용 힘을 결정했다.  

다시 말해서, 가상 물체가 강체인지 연성체인지와 관계없이, 이 방법에서는 상호작용을 위해서라면 항상 물체에 입력 점이 침투한다.  

<br />

이 연구에서는 이전 방법에 대해 세 가지 문제를 지적했다.  

1. 입력 점이 물체 안에 침투했을 때, 어떤 표면을 기준으로 반작용 힘을 결정해야 하는지 모호했다.  
    ![](/static/posts/2026-07-02-paper-a-constraint-based-god-object-method-for-haptic-display/surface-where.png)  
    _입력 점이 a)와 같을 때, 위 방향에서 침투한 것인지, 오른쪽 방향에서 침투한 것인지 파악해야 한다._  

2. 입력 점이 모서리, 꼭짓점과 같은 경계를 지날 때, 반작용 힘이 불연속적으로 변화한다.  

3. 물체가 작고 얇다면, 입력 점이 물체를 통과해버릴 수 있다.  
    ![](/static/posts/2026-07-02-paper-a-constraint-based-god-object-method-for-haptic-display/thin-obj-passing.png)  
    _c)의 파란색 화살표 방향으로 힘을 주었을 때, a), b), c) 과정을 거쳐 물체를 통과한 것으로 피드백될 수 있다._

## The God-object Algorithm

그래서 이 연구에서는 god-object를 정의해 사용하였다. god-object는 입력 점이 물체에 침투했을 때, 입력 점이 침투한 물체의 표면 위에 위치하도록 하는 가상의 점이다.  

> The god-object is placed where the haptic interface point would be if the haptic interface and object were infinitely stiff. Because the god-object remains on the surface of objects, ...  
>  
> God-object는 물체가 무한히 단단하다고 가정했을 때, 햅틱 인터페이스 점이 위치할 지점에 배치됩니다. God-object는 물체의 표면 위에 남아있기 때문에, ...  

_실제로는 물체의 강성이 무한하다고 가정하여 물체의 표면 위에 god-object가 위치한다고 전개된다._  

<br />

그래서 자유 공간에서는 햅틱 인터페이스 포인트와 god-object는 같은 위치에 있지만, 입력 점이 물체에 침투하면 god-object는 물체의 표면에 머무른다.  

## 출력 힘 계산

God-object의 위치가 결정되었다면, 햅틱 인터페이스 점과 god-object 사이에 강성, 감쇠를 적용해 출력을 계산할 수 있다.  

### 평면 한 중간에서 상호작용

우선 시뮬레이션하는 물체의 어떤 표면을 기준으로 god-object와 햅틱 인터페이스 사이의 힘을 계산할지 결정한다.  

이 방법에서도 여전히 햅틱 인터페이스가 물체에 침투해야 반작용 힘을 계산할 수 있다. 따라서 어떤 표면에 대해서, God-object가 표면에 위치하고, 햅틱 인터페이스 점이 표면을 기준으로 물체 방향으로 침투한다면, 이 표면을 기준으로 반작용 힘을 계산할 수 있다.  

> ...we will denote the surface as active if the old god-object is located a positive (in the direction of the surface normal) distance from the surface and the haptic interface point has a negative distance to the surface (i.e. on the other side).  
>  
> ... God-object가 표면으로부터 양의 거리(표면 법선 방향)에 위치하고 햅틱 인터페이스 점이 표면에 대해 음의 거리(반대 방향)에 위치한다면 해당 표면을 활성 상태로 간주합니다.  

<br />

여기서 표면을 활성 상태로 간주한다는 것은, 이 표면을 햅틱 계산에 사용하겠다는 의미이다. 활성 상태의 표면은 반작용 힘을 구하는 과정에서 제약조건(constraint)으로서 계산된다.  

### 경계에서 상호작용

하지만 만약 계산하는 표면이 모서리, 꼭짓점 등의 경계라면, 연구 배경의 문제상황에서 파악하였듯 반작용 힘이 불연속적으로 변화할 수 있다.  

앞서 반작용 계산은 물체의 표면이 사실상 무한 평면인 것처럼 계산하였기 때문에, 입력하는 점이 이 표면 바깥으로 나가더라도, 계속 표면에 붙어있는 것으로 오류를 낼 수 있다.  

<br />

우선 이 상황에서는 god-object와 햅틱 인터페이스 점 사이에 선을 그어, 이 선이 통과하는 표면을 찾는다. (앞서 평면 한 중간에서 상호작용했을 때와는 달리 선을 그어 표면을 찾으므로 조금 더 많은 컴퓨팅 비용이 투입된다.) 이렇게 하면 모서리나 꼭짓점에서도 표면을 찾을 수 있다.  

볼록한 모서리를 공유하는 두 표면 사이에서 god-object가 전환되는 과정은 두 단계를 거친다.  

첫 단계에서는 이전 첫 번째 표면을 활성 상태로 유지시키고, god-object의 위치를 두 번째 표면으로 이동시킨다. 이어서 두 번째 단계에서 첫 번째 표면을 비활성 상태로 바꾸고 두 번째 표면을 활성 상태로 바꾼다. 이렇게 하면 god-object가 두 표면 사이를 이동할 때, 소요되는 시간과 거리가 최소화되어 왜곡을 거의 감지할 수 없게 만들 수 있다.  

<br />

오목한 부분에서는 두 평면의 교차점에 닿을 때, god-object의 움직임은 두 평면의 교차선인 직선 상으로 제한된다. 만약 세 평면의 교차점에 접촉한다면 god-object의 움직임은 세 평면의 교차점인 한 점으로 제한된다. 이때 god-object는 세 평면의 교차점에 위치하게 된다.  

## God-object의 위치 계산

God-object는 앞 단계에서 찾은 활성 표면, 제약 조건을 바탕으로 위치가 결정된다. 입력 점의 현재 위치와 가장 가까우면서 제약 조건을 벗어나지 않는 지점을 찾는다. 여기에 라그랑주 승수법을 적용할 수 있다.  

<br />

God-object와 햅틱 인터페이스 점 사이의 제약조건은 god-object의 좌표 $x$, $y$, $z$ 와 햅틱 인터페이스 점의 좌표 $x_p$, $y_p$, $z_p$ 에 대해서, 이 두 점을 가상의 스프링으로 연결해 끌어당기는 상황으로 반작용 힘을 모델링한다. $Q$ 는 단위 강성을 가진 가상 스프링의 에너지로 생각할 수 있다.  

$$
Q = \frac{1}{2}(x - x_p)^2 + \frac{1}{2}(y - y_p)^2 + \frac{1}{2}(z - z_p)^2
$$

이 제약조건은 3자유도 상황에서 $x$, $y$, $z$ 좌표를 찾는 문제로 아래와 같이 정리할 수 있다. ($x$, $y$, $z$ 에 대해 1차식, 평면 방정식이 된다.)   

$$
A_n x + B_n y + C_n z - D_n = 0
$$

<br />

이 제약조건을 결합해 새로운 함수 $L$ 을 구성하면 라그랑주 승수법을 적용할 수 있다. $l_1$, $l_2$, $l_3$ 는 라그랑주 승수이다.  

$$
\begin{aligned}
L &= Q \\
& \quad + l_1(A_1 x + B_1 y + C_1 z - D_1) \\
& \quad + l_2(A_2 x + B_2 y + C_2 z - D_2) \\
& \quad + l_3(A_3 x + B_3 y + C_3 z - D_3) \\
&= \frac{1}{2}(x - x_p)^2 + \frac{1}{2}(y - y_p)^2 + \frac{1}{2}(z - z_p)^2 \\
& \quad + l_1(A_1 x + B_1 y + C_1 z - D_1) \\
& \quad + l_2(A_2 x + B_2 y + C_2 z - D_2) \\
& \quad + l_3(A_3 x + B_3 y + C_3 z - D_3) \\
\end{aligned}
$$

God-object의 새로운 위치는 $L$ 을 최소화하여 구한다. 각 변수 $x$, $y$, $z$, $l_1$, $l_2$, $l_3$ 에 대해 편미분하여 0이되는 지점을 찾으면, 아래와 같은 연립방정식으로 정리할 수 있다.   

$$
\begin{bmatrix}
1 & 0 & 0 & A_1 & A_2 & A_3 \\
0 & 1 & 0 & B_1 & B_2 & B_3 \\
0 & 0 & 1 & C_1 & C_2 & C_3 \\
A_1 & B_1 & C_1 & 0 & 0 & 0 \\
A_2 & B_2 & C_2 & 0 & 0 & 0 \\
A_3 & B_3 & C_3 & 0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z \\
l_1 \\
l_2 \\
l_3 \\
\end{bmatrix}
=
\begin{bmatrix}
x_p \\
y_p \\
z_p \\
D_1 \\
D_2 \\
D_3 \\
\end{bmatrix}
$$

## 마무리

이 연구에서는 god-object을 정의하고, god-object에 제약조건을 적용하여, 햅틱 피드백을 계산하는 방법을 제안하였다.  

이전 연구에서는 입력 점이 물체를 침투하면서 이 점이 물체를 관통할 수 있었고, 그 외에 경계면에서 피드백이 불연속적인 문제, 어떤 표면과 상호작용하는지 결정하는 문제를 해결하기 위해 많은 컴퓨팅 비용이 요구되었다.  

이 연구의 god-object 방법은 추가적인 계산 소요 없이도 햅틱 피드백을 더 적합한 방법으로 계산할 수 있게 했다는 점에서 의미가 있다고 할 수 있다.  
