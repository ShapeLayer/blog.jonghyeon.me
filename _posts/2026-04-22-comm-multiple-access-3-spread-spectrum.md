---
layout: post
title: Spread Spectrum (대역 확산)
date: 2026-04-22
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## 배경

디지털 통신 시스템에서 데이터 전송 속도(채널 용량)은 섀넌의 채널 용량 공식에 의해 결정된다.  

$$
C = W \cdot \log_2(1 + \text{SNR})
$$  
_$C$ 는 채널 용량(bits/sec), $W$ 는 채널 대역폭(Hz)_  

<br />

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/bandwidth.png)  

어떤 네트워크에서 10Mbps의 전송 속도를 달성하고자 할 때, 대역폭이 1MHz인 채널을 사용하려고 한다면 SNR이 1000(30dB) 이상이어야 한다. 반면 대역폭이 10MHz인 채널을 사용하려고 한다면 SNR이 1배(0dB)여도 10Mbps의 전송 속도를 달성할 수 있다.  

따라서 송신 전력이 제한된 환경에서는 신호 대 잡음비를 한도 없이 높일 수 없기 때문에, 대역폭을 넓혀 데이터 전송 속도를 확보해야 한다.  

Spread Spectrum으로 대역폭을 넓혀 데이터 전송 속도를 확보할 수 있다. 특정 대역폭을 가진 신호에 Spreading Code(확산 코드)를 곱하여 주파수 영역에서 훨씬 더 넓은 대역에 신호를 확산시킬 수 있다.    

## DSSS: Direct Sequence Spread Spectrum (직접 시퀀스 대역 확산)

비트 주기 $T$ 를 가지는 원본 데이터 신호를 DSSS하려고 한다. 원본 신호의 주파수 영역에서의 대역폭은 $1/T$ 이다. DSSS에서는 원본 신호에 Spreading Code(확산 코드)를 곱하여 대역폭을 넓힌다.  

$$
T_c \ll T
$$

DSSS를 적용하기 위해 원본 신호에 Spreading Code를 곱한다. 이 코드는 훨씬 짧은 칩 주기<sup>1</sup> $T_c$ 를 가진다. 곱한 결과 신호는, 확산된 신호로서 원본 신호보다 훨씬 넓은 대역폭 $1/T_c$ 를 가지게 된다. 이와 같이 대역폭이 확장되어 획득한 이득을 처리 이득(Processing Gain)이라고 한다.  

\* 1. 칩 주기: Spreading Code의 각 요소가 지속되는 시간

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/apply-dsss.png)  

Tx에서는 수신된 확산 신호에 동일한 확산 코드를 다시 곱한다. 동일한 코드를 두 번 곱하면 $c^2(t) = 1$ 이 되어 원본 신호가 복원된다.  

<br />

DSSS는 의도적인 재밍이나 다른 사용자의 간섭에 강한 특성을 가진다. Tx에서 원하는 사용자의 확산 코드로 역확산을 수행하면, 사용한 코드와 일치하는 코드만 좁은 대역폭으로 복원되고, 다른 코드를 사용한 신호들은 넓은 대역으로 확산되어 버리기 때문이다. 이렇게 획득한 코드에 필터를 적용하면 확산된 간섭 성분은 대부분 제거된다.  

처리 이득 $G_p$(혹은 $T/Tc$) 가 클수록 간섭 제거 성능은 더욱 향상된다.  

<br />

또한 도청도 어렵다. 협대역 신호는 특정한 주파수 스펙트럼에 전력이 집중되어, 도청 장치가 쉽게 탐지할 수 있다. 반면에 DSSS 신호는 신호 전력이 매우 넓은 주파수 대역에 걸쳐 분산되어 있어, 잡음 레벨 아래에 묻히는 수준의 낮은 전력 밀도를 보인다. 때문에 확산 코드를 모르는 제 3자는 이 신호를 파악하기 어렵다. 이 특성을 LPI(Low Probability of Intercept)라고 한다.  

## RAKE 수신기

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/rake-recv.png)  

무선 통신 환경에서는 송신된 신호가 건물, 지형 등 다양한 장애물에 반사되어, 서로 다른 지연 시간을 가진 여러 경로를 거쳐 수신기에 도달한다. RAKE 수신기는 이러한 다중 경로 신호를 이득으로 활용한다.  

송신 신호 $s(t)$, 다중경로의 개수 $L$로 표현된 수신 신호 $r(t)$ 에 대해서, Spreading Code의 직교성을 이용해서 지연된 각 신호를 분리할 수 있다.  

$$
\begin{aligned}
s(t) &= \sqrt{P} d(t) c(t) \cos(2\pi f_c t) \\

\end{aligned}
$$

De-spreading후의 각 출력 신호 $y_k$ ($k$ 는 경로의 인덱스) 는 다음과 같이 표현된다.  

$$
\begin{aligned}
y_k &= \int r(t) \cdot c(t - \tau_k) dt \\
&= \int \left( \sum_{i=0}^{L - 1} \alpha_i s(t - \tau_i) \right) \cdot c(t - \tau_k) dt + n_k \\
&= \alpha_k \sqrt{P} d(t) R_c (0) + \sum_{i \ne k}^{L - 1} \alpha_i \sqrt{P} d(t - \tau_i) R_c(\tau_k - \tau_i) + n_k \\
\end{aligned}
$$

만약 $\vert\tau_k - \tau_i\vert > T_c$ 라면, $R_c(\tau_k - \tau_i) \approx 0$ 이 되어, $y_k$ 는 $\alpha_k \sqrt{P} d(t) R_c (0) + n_k$ 와 같이 표현된다. 즉, 다른 경로의 간섭이 제거되고, 원하는 신호가 복원된다.  

<br />

각 경로별로 분리된 신호들은 Correlator를 사용하여 독립적으로 복조한다. 이후에 Maximum Ratio Combining(MRC) 방법으로 가중 합산한다.  

$$
y = \sum_{k=0}^{L-1} \alpha_k^* y_k
$$

<br />

Baseband 신호를 기준으로 DSSS의 각 단계에서의 신호는 다음과 같이 표현된다.  

| 항목 | 값(시간 영역) | 값(주파수 영역) |
| :-: | :-- | :-- |
| 메시지 데이터 <br /> Message Data | $b(t) \in {1, -1}$ <br/> Bit Period: $T_b \text{[sec]}$ | $b(t) = \sum_{i} b_i p_{T_b} (t - i T_b)$ <br /> \* $p_{T_b}(t)$: Bit Period의 Pulse Function <br /> $S_b(f) = T_b sinc^2(f T_b)$ <br /> Bandwidth: $B \approx 1/T_b$ |
| 확산 코드 <br /> Spreading Code | $c(t) \in {1, -1}$ <br/> Chip Period: $T_c \text{[sec]}$ | $c(t) = \sum_{n} c_n p_{T_c} (t - n T_c)$ <br /> $S_c(f) = T_c sinc^2(f T_c)$ <br /> Bandwidth: $B \approx 1/T_c$ |
| 확산 신호 <br /> Spread Signal | $x(t) = b(t) \cdot c(t)$ <br/> Signal Period: $T_c \text{[sec]}$ | $S_x(f) = S_b(f) * S_c(f)$ <br /> Bandwidth: $W \approx 1/T_c$ |
| 복조된 신호 <br /> De-spread Signal | $b(t) = x(t) \cdot c(t)$ <br/> $c^2(t) = 1$ |  |
| 처리 이득 <br /> Processing Gain |  | $G_p = \frac{\frac{1}{T_c}}{\frac{1}{T_b}} = \frac{T_b}{T_c}$ <br /> $\frac{1}{T_c}$ 는 확산 대역 $W$, $\frac{1}{T_b}$ 는 원본 대역 $B$ |

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/dsss-time-domain.png)  
_시간 영역에서의 DSSS 신호 그래프_  

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/dsss-freq-domain.png)  
_주파수 영역에서의 DSSS 신호 그래프_  

## BPSK 시스템에서의 DSSS

### 송신 측

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/bpsk-tx.jpg)

$$
s(t) = A \cdot b(t) \cdot c(t) \cdot \cos(2\pi f_c t)
$$

BPSK 시스템에서는 RF 대역에 신호를 송신할 때, 기저대역 확산 신호 $x(t) = b(t) \cdot c(t)$ 에 Carrier(반송파) $\cos(2\pi f_c t)$ 를 곱하여 전송한다. 반송파는 반송파 주파수 $f_c$ 를 가지는 파형이다.  

$$
\text{Carrier} = \cos(2\pi f_c t)
$$

### 수신 측 (w/o 지연, w/o 잡음)

Rx 측 $r(t)$ 에서 지연이나 잡음이 없다면, 신호는 Tx에서의 역과정으로 복조할 수 있다.  

$$
r(t) = s(t) = A \cdot b(t) \cdot c(t) \cdot \cos(2\pi f_c t)
$$

$$
r_d(t) = r(t) \cdot \cos(2\pi f_c t) \approx b(t)c(t)
$$  
_복조 결과 $r_d(t)$ 의 계산: $b(t)$ 는 원본 데이터 신호, $c(t)$ 는 확산 코드_  

<br />

$$
\hat{b} = r_d(t) c(t) = b(t)
$$  
_역확산된 신호 $\hat{b}$_  

### 수신 측 (w/ 지연, w/ 잡음)

Rx에 지연, 잡음이 존재하는 경우, Rx 측 $r(t)$ 는 다음과 같이 표현된다. $s(t - \tau)$ 는 $\tau$ 만큼 지연된 신호, $n(t)$ 는 잡음이다.  

$$
\begin{aligned}
r(t) &= s(t - \tau) + n(t) \\
&= A \cdot b(t - \tau) \cdot c(t - \tau) \cdot \cos(2\pi f_c (t - \tau)) + n(t) \\
&= A \cdot b(t - \tau) \cdot c(t - \tau) \cdot \cos(2\pi f_c t - \theta) + n(t)
\end{aligned}
$$

Tx에서 신호를 복조하려면 $\tau$ 를 정확히 알고 있어야 한다. 그래서 Symbol Timing Recovery(심볼 타이밍 복구), Carrier Recovery(반송파 복구), PN Signal Synchronization(PN 신호 동기화) 처리가 수행된다.  

<br />

PN 신호 동기화 처리를 수행하여 신호를 복조 시도하였을 때, 로컬의 PN 코드와 수신된 신호가 정확히 정렬되어 있다면, 판정 변수 $z_i$ 는 다음과 같이 표현된다. $A$ 는 신호의 진폭, $T_b$ 는 비트 주기, $n_0$ 는 잡음이다.  

$$
z_i = \pm(A \cdot T_b / 2) + n_0
$$

$$
\begin{aligned}
z_i &= \int_{t_i}^{t_i + T_b}{(s(t - \tau) + n(t)) \cdot c(t - \tau) \cos(2\pi f_c t + \theta) dt} \\
&= \int_{t_i}^{t_i + T_b}{s(t - \tau) \cdot c^2(t - \tau) \cdot \cos^2(2\pi f_c t + \theta) dt} + n_0 \\
&= \frac{b_i A T_b}{2} + n_0 \\
&= \pm(A \cdot T_b / 2) + n_0
\end{aligned}
$$

만약 지연을 동기화했는데도, 예측 지연값과도 차이가 발생했거나, 정렬에 오류가 있을 수 있다. 이 때 얼마나 오차가 발생했는지에 따라 신호의 품질이 달라진다. 이 때의 판정 변수 $z_i$ 는 산출(예측)한 지연값과의 오차 $\Delta\tau$ 에 대해 확산 코드의 자기상관 함수 $R_c(\Delta\tau)$ 가 고려된다.  

$$
z_i = \pm(A \cdot T_b / 2) \cdot R_c(\Delta\tau) + n_0
$$

$$
\begin{aligned}
z_i &= \int_{t_i}^{t_i + T_b}{(s(t - \tau) + n(t)) \cdot c(t - \tau) \cos(2\pi f_c t + \theta) dt} \\
&= \int_{t_i}^{t_i + T_b}{s(t - \tau) \cdot c(t - \tau) \cdot c(t - \tau + \Delta\tau) \cdot \cos^2(2\pi f_c t + \theta) dt} + n_0 \\
&= \frac{b_i A}{2} \int_{t_i}^{t_i + T_b}{c(t - \tau) \cdot c(t - \tau + \Delta\tau) dt} + n_0 \\
&= \pm(A \cdot T_b / 2) \cdot R_c(\Delta\tau) + n_0
\end{aligned}
$$

자기상관 함수 $R_c(\Delta\tau)$ 는 $\Delta\tau$ 가 0에 가까울수록 1에 가까운 값을 가지며, $\Delta\tau$ 가 커질수록 0에 가까운 값을 가진다. 따라서 $\Delta\tau$ 가 작을수록 판정 변수 $z_i$ 의 절대값이 커져서 신호 품질이 향상된다.  

- $\vert\Delta\tau\vert < T_c$: $R_c(\Delta\tau)$ 가 1에 인접, 신호의 신뢰성이 높음
- $\vert\Delta\tau\vert > T_c$: $R_c(\Delta\tau)$ 가 0에 인접, 신호 검출 불가
- $T_c$ 는 칩 주기

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/r_c-d_tau.png)  
_자기상관 함수 $R_c(\Delta\tau)$ 의 그래프_  

따라서 동기화 오차 $\Delta \tau$ 는 칩 주기 $T_c$ 이내에 있어야 신호를 검출할 수 있다. 따라서 칩 주기가 작으면 Processing Gain을 높일 수 있으나, PN 코드 동기를 찾기 어려워질 수 있다.    

## FHSS: Frequency Hopping Spread Spectrum (주파수 도약 대역 확산)

![](/static/posts/2026-04-22-comm-multiple-access-3-spread-spectrum/hopping.png)

FHSS는 Tx에서 반송파 주파수를 빠르게 랜덤하게 도약시키면서 신호를 송신한다.  

Tx 측에서는 확산 코드를 사용하여 주파수를 변경한다. 따라서 Rx 측에서도 동일한 코드로 호핑 패턴을 알고 있어야 신호를 복조할 수 있다.  

이 신호는 한 순간에는 특정한 주파수만을 사용하고 있으므로 협대역 신호로 탐지될 수 있지만, 주파수를 계속 변경하므로 전체 시간에 걸쳐 확인하면 넓은 유효 대역폭을 점유함을 확인할 수 있다.  

또한 신호가 주파수를 계속해서 바꾸므로, 도청이나 재밍으로 특정한 주파수가 집중적으로 공격받더라도, 공격받는 주파수를 곧 벗어나므로 신호가 안전할 수 있다.  

이러한 이유로 DSSS에 비교해 넓은 대역폭 확산에 유리해, 군사 통신이나 블루투스 등에서 사용된다.  
