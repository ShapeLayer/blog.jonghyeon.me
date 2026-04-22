---
layout: post
title: 직교코드
date: 2026-04-22
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## Matched Filter (정합 필터)

CDMA Rx 신호 $r(t)$ 는 Tx 신호 $s(t)$, 잡음 $n(t)$ 의 합으로 표현된다. 보통 $s(t)$ 는 $T$ 동안 지속되는 신호이고, $n(t)$ 는 평균 0, 전력 스펙트럼 밀도 $N_0/2$ 인 가우시안 분포를 따른다고 가정한다.

$$
r(t) = s(t) + n(t)
$$

이 때 Matched Filter의 출력 $y(t)$ 는 $r(t)$ 와 필터 $h(t)$ 의 컨볼루션이다.  

$$
y(t) = r(t) * h(t) = \int_{-\infty}^{\infty} r(\tau) h(t - \tau) d\tau = s_0(t) + n_0(t)
$$

신호는 $T$ 동안 지속되므로, $t = T$ 일 때, 샘플링된 출력 $y(T)$ 는 SNR을 최대화하는 최적 샘플링 지점이 된다.  

<br />

$t = T$ 일 때, Matched Filter의 출력 $y(T)$ 는 다음과 같이 표현되고, 코시-슈바르츠 부등식에 의해 상한이 결정된다.  

$$
\gamma = \frac{\|s_0(T)\|^2}{\mathbb{E}[\|n_0(T)\|^2]}
$$

$$
\| \int A(t) B(t) dt \|^2 \leq \int \|A(t)\|^2 dt \cdot \int \|B(t)\|^2 dt
$$  

코시-슈바르츠 부등식에 의한 상한 $\gamma^*$ 는 다음과 같이 표현된다.  

$$
\begin{aligned}
\gamma &= \frac{\|s_0(T)\|^2}{\mathbb{E}[\|n_0(T)\|^2]} \\ &= \frac{\| \int_0^T s(\tau) h(T - \tau) d\tau \|^2}{\frac{N_0}{2}\int_0^T \|h(\tau)\|^2 d\tau} \\
&\leq \frac{\int_0^T \|s(\tau)\|^2 d\tau \cdot \int_0^T \|h(T-\tau)\|^2 d\tau}{\frac{N_0}{2}\int_0^T \|h(\tau)\|^2 d\tau}
\end{aligned}
$$

$$
\gamma^* = \frac{\int_0^T \|s(\tau)\|^2 d\tau}{\frac{N_0}{2}} = \frac{2E_s}{N_0}
$$

- $E_s$ = 신호의 에너지

최적의 필터 $h(t)$ 는 $h(t) = k s^* (T - t)$ 이다. 즉, $h(t)$ 는 송신 신호 $s(t)$ 의 시간 역전된 복소수 켤레(conjugate) 이다.  

## Correlator (상관기)

Correlator는 Matched Filter와 수학적으로 동일한 결과를 내는 수신기 구조이다. Correlator는 $r(t)$ 와 $s(t)$ 의 내적을 계산하여, $s(t)$ 가 $r(t)$ 에 포함되어 있는지를 판단한다.  

$$
y(T) = \int_0^T r(\tau) \cdot k \cdot s(\tau) d\tau
$$

$t = T$ 일 때 Correlator의 출력 $y(T)$ 는 Matched Filter의 출력과 동일하다. 다시 말해, 구현이 다른 동일 수신기 구조이다.  

## Orthogonality

기지국이 여러 사용자의 신호를 동시에 수신하면, 각 사용자의 신호를 간섭 없이 분리할 수 있어야 한다. 이를 위해 Matched Filter와 Correlator를 이용하여 각 사용자의 신호가 서로 직교(Orthogonal)하도록 설계한다.  

$$
\int_0^T s_n(t) \cdot s_m(t) dt = \begin{cases}
k & \text{if } n = m \\
0 & \text{if } n \neq m
\end{cases}
$$

- $k$ = 신호의 에너지

<br />

아래와 같은 두 개의 시퀀스가 있을 때, 이들 시퀀스는 자기 자신과의 내적에서 8이 되고, 서로 다른 시퀀스와의 내적에서 0이 된다. 즉, 이 시퀀스들은 서로 직교한다.  

- Code \#1: `[1, 1, 1, 1, -1, -1, -1, -1]`
- Code \#2: `[1, 1, -1, -1, 1, 1, -1, -1]`

$$
C_1 \cdot C_1 = 8, \quad C_2 \cdot C_2 = 8, \quad C_1 \cdot C_2 = 0
$$

<br />

Code \#1을 사용하는 사용자가 데이터 `1`을, Code \#2를 사용하는 사용자가 데이터 `-1`을 같은 순간에 전송한다면, 공중에서 생성된 두 신호가 합쳐진다.  

$$
\begin{aligned}
S_1(t) &= 1 \times \text{Code \#1} = [1, 1, 1, 1, -1, -1, -1, -1] \\
S_2(t) &= -1 \times \text{Code \#2} = [-1, -1, 1, 1, -1, -1, 1, 1] \\
S_1 + S_2 &= [0, 0, 2, 2, -2, -2, 0, 0]
\end{aligned}
$$

이후에 수신 측에서 Code \#1을 역확산하면 `[0, 0, 2, 2, -2, -2, 0, 0]`과 Code \#1의 내적이 계산되고, 이 값은 `8`이 된다. 즉, Code \#1을 사용하는 사용자의 데이터가 `1`로 검출된다.  

$$
\begin{aligned}
(S_1 + S_2) \cdot \text{Code \#1} &= [0, 0, 2, 2, -2, -2, 0, 0] \cdot [1, 1, 1, 1, -1, -1, -1, -1] \\
&= 0 \cdot 1 + 0 \cdot 1 + 2 \cdot 1 + 2 \cdot 1 + (-2) \cdot (-1) + (-2) \cdot (-1) + 0 \cdot (-1) + 0 \cdot (-1) \\
&= 8
\end{aligned}
$$

Code \#2를 역확산하면 `[0, 0, 2, 2, -2, -2, 0, 0]`과 Code \#2의 내적이 계산되고, 이 값은 `-8`이 된다. 즉, Code \#2를 사용하는 사용자의 데이터가 `-1`로 검출된다.  

$$
\begin{aligned}(S_1 + S_2) \cdot \text{Code \#2} &= [0, 0, 2, 2, -2, -2, 0, 0] \cdot [1, 1, -1, -1, 1, 1, -1, -1] \\
&= 0 \cdot 1 + 0 \cdot 1 + 2 \cdot (-1) + 2 \cdot (-1) + (-2) \cdot 1 + (-2) \cdot 1 + 0 \cdot (-1) + 0 \cdot (-1) \\
&= -8
\end{aligned}
$$

## Auto Correlation(자기상관)과 Cross Correlation(상호상관)

자기상관은 서로 다른 두 시간에서의 신호가 얼마나 유사한지 표현하는 지표이다. 무선 통신에서 동일한 신호는 $\tau$ 만큼 시간 지연된 후에도 수신될 수 있으므로, 낮은 자기상관이 선호된다.  

$$
R_{ss}(\tau) = \int_{-\infty}^{\infty} s(t) s(t - \tau) dt
$$

- $\tau$ = 시간 지연
- $\tau = 0$ 일 때, 시간은 지연되지 않으므로, 자기상관은 최대이다.  

상호상관은 서로 다른 두 독립된 신호가 시간 지연된 후에도 얼마나 유사한지 표현하는 지표이다. 무선 통신에서 서로 다른 신호는 $\tau$ 만큼 시간 지연된 후에도 수신될 수 있으므로, 낮은 상호상관이 선호된다.  

$$
R_{s_1 s_2}(\tau) = \int_{-\infty}^{\infty} s_1(t) s_2(t - \tau) dt
$$

만약 $R_{s_1 s_2}(\tau)$ 가 크면 두 신호는 서로 유사하다. $R_{s_1 s_2}(\tau)$ 가 작으면 두 신호는 서로 독립적이다.  

## Orthogonal Code와 Pseudo-Noise(PN) Code

CDMA에서는 서로 직교하는 코드(Orthogonal Code)를 사용하여 여러 사용자가 동시에 통신할 수 있도록 한다. 하지만 실제 환경에서는 완벽한 직교성을 유지하기 어려울 수 있다. 따라서, 완벽한 직교성을 가지는 코드 대신에, 낮은 상호상관을 가지는 Pseudo-Noise(PN) Code를 사용하기도 한다. PN Code는 무작위처럼 보이는 시퀀스이지만, 생성 알고리즘에 의해 결정되는 시퀀스이다. PN Code는 낮은 자기상관과 낮은 상호상관을 가지도록 설계되어, CDMA 시스템에서 효과적으로 사용된다.  

| 특성 | Orthogonal Code | Pseudo-Noise Code |
| --- | --- | --- |
| 직교성 | 완벽함, 내적 = 0 | 직교성이 보장되지 않음 |
| 간섭 | 간섭이 없어야 함 | 간섭이 있을 수 있음 |
| 동기화 | 시간 동기화 필수 | 비동기 환경에서도 사용 가능 |
| 용도 | 다운링크 | 업링크, 셀 구분 등 |

## Walsh Code

Walsh 코드는 Hadamard 행렬로부터 유도된 코드로, 원소로 +1과 -1만을 갖는다. 서로 다른 행끼리의 상호 상관이 0이어서 서로 직교한다.  

$$
H \cdot H^T = n \cdot I
$$  
_$n$ 은 행렬의 차원_

$$
\begin{aligned}
H_1 &= \begin{bmatrix} -1 & -1 \\ -1 & 1 \end{bmatrix} \\
H_2 &= \begin{bmatrix} -1 & -1 & -1 & -1 \\ -1 & 1 & -1 & 1 \\ -1 & -1 & 1 & 1 \\ -1 & 1 & 1 & -1 \end{bmatrix} = \begin{bmatrix} H_1 & H_1 \\ H_1 & \bar{H_1} \end{bmatrix} \\
\vdots \\
H_k &= \begin{bmatrix} H_{k-1} & H_{k-1} \\ H_{k-1} & \bar{H_{k-1}} \end{bmatrix}
\end{aligned}
$$

<table>
  <tbody>
    <tr>
      <td>$H_{2, 0}$</td>
      <td>$-1$</td>
      <td>$-1$</td>
      <td>$-1$</td>
      <td>$-1$</td>
    </tr>
    <tr>
      <td colspan="5" style="text-align: center;">$\cdots$</td>
    </tr>
    <tr>
      <td>$H_{2, 1}$</td>
      <td>$-1$</td>
      <td>$1$</td>
      <td>$-1$</td>
      <td>$1$</td>
    </tr>
    <tr>
      <td>$H_{2, 0} \cdot H_{2, 1}$</td>
      <td>$1$</td>
      <td>$-1$</td>
      <td>$1$</td>
      <td>$-1$</td>
    </tr>
    <tr>
      <td>$\sum$</td>
      <td colspan="4">$0$ (Orthogonal)</td>
    </tr>
  </tbody>
</table>

Walsh 는 완벽한 직교성을 가지지만, 시간 동기화가 필요하다. 동기 상태가 깨지면, 상호상관이 급격히 증가하여 심각한 간섭이 발생한다. 따라서 Walsh 코드는 시간 동기화가 어려운 업링크에서는 사용되지 않는다.  

## Bi-Orthogonal Code

$$
B_k = \begin{bmatrix}H_{k-1} \\ \bar{H_{k-1}} \end{bmatrix}
$$

$$
B_3 = \begin{bmatrix}
-1 & -1 & -1 & -1 \\
-1 & 1 & -1 & 1 \\
-1 & -1 & 1 & 1 \\
-1 & 1 & 1 & -1 \\
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
$$

Bi-Orthogonal 코드는 Walsh 코드에 추가로 Walsh 코드의 부호를 반전시킨 코드를 포함하는 코드이다. 이렇게 하면 음수의 상호 상관 값도 발생할 수 있어, Coherent 시스템에서 활용할 수 있다. Coherent 시스템은 신호 검출에 있어서 신호의 위상 정보까지 활용하는 시스템이다. (대조적으로 비 Coherent 시스템은 진폭과 주파수만 활용한다.)

$$
\begin{aligned}
z_{i, j} = \begin{cases}
\frac{M}{2} & \text{if } i = j \\
-\frac{M}{2} & \text{if } i \neq j, \|i - j\| = \frac{M}{2} \\
0 & \text{otherwise}
\end{cases}
\end{aligned}
$$

## Pseudo-Noise Code

Pseudo-Noise(PN) Code는 랜덤 시퀀스로 보이지만, 실제로는 결정적으로 생성되는 시퀀스이다. 이 코드는 세 가지의 핵심 성질을 갖는다.  

- 균형(Balanced Property): 한 주기 내에서 `1`과 `-1`의 개수가 거의 같다. (등장 횟수 차이가 0 또는 1이다.)
- 상관(Correlation Property): 자기상관이 낮아 타이밍 검출에 유리하다. 
- 런(Run Property): 연속 동일 심볼의 길이(런)가 특정한 분포를 따른다. (= `1`과 `-1`이 연속해서 나타나는 횟수가 일정하다.) 길이 1인 런이 50%, 길이 2인 런이 25%, 길이 $n$인 런이 $1/2^n$ 의 비율로 나타난다.  

## Maximal Length Sequence

![](/static/posts/2026-04-22-comm-multiple-access-2-orthogonality/shift-register.jpeg)  
_LFSR의 계산 그래프_  

Maximal Length Sequence(최대 길이 시퀀스)는 선형 피드백 시프트 레지스터(Linear Feedback Shift Register, LFSR)를 이용하여 생성되는 PN Code의 한 종류이다. LFSR은 여러 개의 플립플롭과 피드백 경로로 구성된 회로로, 초기 상태에 따라 결정적으로 시퀀스를 생성한다. $m$ 개의 시프트 레지스터를 사용하면 $2^m - 1$ 길이의 시퀀스를 생성할 수 있다.  

이 시퀀스의 자기상관은 매우 뚜렷한 특성을 보인다. 시퀀스의 0을 -1로 치환하면 자기상관이 다음과 같이 표현된다.  

- $\tau = 0$ 일 때, 자기상관은 $N$ ($N$ = 시퀀스의 길이)
- $\tau \neq 0$ 일 때, 자기상관은 $-1$

| | |
| :-: | :--: |
| $m(0)$ | `1 1 1 1 0 0 0 1 0 0 1 1 0 1 0` |
| $m(1)$ | `0 1 1 1 1 0 0 0 1 0 0 1 1 0 1` |
| $m(0) \cdot m(1)$ | `0 1 1 1 0 0 0 0 1 0 0 1 1 0 1` |
| $m'(0) \cdot m'(1)$ | `-1 1 1 1 -1 -1 -1 -1 1 -1 -1 1 1 -1 1` |
| $m'(0) \cdot m'(0)$ | `1 1 1 1 1 1 1 1 1 1 1 1 1 1 1` |

\* $m'(\tau)$ 는 $m(\tau)$ 의 `0`을 `-1`로 치환한 시퀀스

- $\sum m'(0) \cdot m'(1) = -1$ (낮은 상관)
- $\sum m'(0) \cdot m'(0) = 15$ (높은 상관)

Maximal Length Sequence를 시간 지연 $\tau$ 와 자기상관에 대해서 그래프를 그렸을 때, Maximal Length Sequence의 길이 $N$ 을 사이클로 -1을 유지하다가 $N$ 의 정수배에서 갑자기 $N$ 으로 피크가 발생한다. 이 때, 피크의 높이는 시퀀스의 길이 $N$ 이다.  

![](/static/posts/2026-04-22-comm-multiple-access-2-orthogonality/auto-corr-of-mls.png)  

이와 같이 뚜렷한 날카로운 피크를 가지는 자기상관 특성으로, 타이밍 검출과 동기화에 유리하다.  

## Gold Sequence

![](/static/posts/2026-04-22-comm-multiple-access-2-orthogonality/gold-sequence.jpeg)

Maximal Length Sequence는 낮은 자기상관을 보이지만, 다른 시퀀스와의 상호상관은 잠재적으로 높을 수 있다. Gold Sequence는 상호상관 특성을 개선하기 위해 두 개의 Maximal Length Sequence을 선택해 XOR 연산을 수행한다.  

$$
\| R_{S_1 S_2} \| = 1 \text{ or } 2^{(m+2)/2} + 1 \text{ or } 2^{(m+1)/2} + 1
$$

Gold Sequence는 비동기 이벤트에서도 낮은 상호상관을 유지하여, 간섭이 적게 발생한다. 이러한 특성으로 CDMA 시스템에서 업링크에 주로 사용된다.  
