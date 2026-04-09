---
layout: post
title: 카이제곱분포와 카이제곱 확률변수
date: 2026-04-09
category: [probability-and-statistics]
---

〈빅데이터의과학적탐구〉 수업 노트

<br />

카이제곱($\chi^2$)분포는 $k$ 개의 서로 독립적인 표준 정규 확률변수를 각각 제곱하여 합해 획득할 수 있는 확률변수의 분포이다.  

## 카이제곱 확률변수 $U$ 의 정의

서로 독립이면서 표준정규분포 $N(0, 1)$ 을 따르는 $v$ 개의 확률변수 $Z_1, Z_2, \cdots, Z_v$ 가 있다면, 카이제곱 확률변수 $U$는 다음과 같이 정의된다.  

$$
\displaystyle U = \sum_{i=1}^v {Z_i}^2
$$

만약 $v=5$ 라면, $U = Z_1^2 + Z_2^2 + Z_3^2 + Z_4^2 + Z_5^2$ 로 정의된다. 이 확률변수 $Z_i$ 가 실제로 관측되었다고 가정하고, $Z_1 = 0.5$, $Z_2 = -1.0$, $Z_3 = 1.5$, $Z_4 = -0.5$, $Z_5 = 0.0$ 라고 하면, 카이제곱 확률변수 $U$ 는 다음과 같이 계산된다.

$$
\begin{aligned}
\displaystyle U &= 0.5^2 + (-1.0)^2 + 1.5^2 + (-0.5)^2 + 0.0^2 \\
&= 0.25 + 1.0 + 2.25 + 0.25 + 0.0 \\
&= 3.75
\end{aligned}
$$

## 정규분포 $N(\mu, \sigma^2)$ 를 따르는 경우

조금 더 확장해서, 정규분포 $N(\mu, \sigma^2)$ 을 따르는 $v$ 개의 확률변수 $X_1, X_2, \cdots, X_v$ 가 있다면, 표준화된 확률변수 $Z_i$와 카이제곱 확률변수 $U$는 다음과 같이 정의된다.

$$
\displaystyle Z_i = \frac{X_i - \mu}{\sigma}
$$

$$
\displaystyle U = \sum_{i=1}^v Z_i^2 = \sum_{i=1}^v \left( \frac{X_i - \mu}{\sigma} \right)^2
$$

## 그 외의 특성

$\chi^2$ 확률변수 $U$ 는 제곱의 합으로 정의되기 때문에 항상 $0$ 이상의 값을 갖는다. 또한 자유도 $v$ 와 평균 $E(U)$ 는 같고, 분산 $Var(U)$ 는 $2v$ 이다. 자유도 $v$ 가 증가할수록 카이제곱 분포는 정규분포에 가까워지는 경향이 있다.

$$
U \geq 0
$$

$$
\quad E(U) = v
$$

$$
\quad Var(U) = 2v
$$

이렇게 나타나는 이유는 아래의 증명을 통해 확인할 수 있다.

<br />

$$
\begin{aligned}
E(U) &= E\left( \sum_{i=1}^v Z_i^2 \right) \\
&= \sum_{i=1}^v E(Z_i^2) \\
&= \sum_{i=1}^v Var(Z_i) \quad \text{(since } E(Z_i) = 0 \text{)} \\
&= \sum_{i=1}^v 1 \quad \text{(standard normal variance)} \\
&= v
\end{aligned}
$$

$\sum_{i=1}^v E(Z_i^2)$ 에서 $E(Z_i^2)$ 는 $0$ 이므로 $Var(Z_i)$ 와 같다. $Var(Z_i)$ 는 표준정규분포의 분산이므로 $1$ 이다. 따라서 $\sum_{i=1}^v Var(Z_i) = \sum_{i=1}^v 1 = v$ 가 된다.

<br />

$$
\begin{aligned}
Var(U) &= Var\left( \sum_{i=1}^v Z_i^2 \right) \\
&= \sum_{i=1}^v Var(Z_i^2) \\
&= \sum_{i=1}^v 2 \\
& = 2v
\end{aligned}
$$

$Var\left( \sum_{i=1}^v Z_i^2 \right)$ 에서 $Z_i$ 는 독립이므로 $\sum_{i=1}^v Var(Z_i^2)$ 와 동치이다.  

$\sum_{i=1}^v Var(Z_i^2)$ 에서 $Var(Z_i^2)$ 는 자유도가 1인 카이제곱 분포의 분산이므로 $2$ 이다. 따라서 $\sum_{i=1}^v Var(Z_i^2) = \sum_{i=1}^v 2 = 2v$ 가 된다.
