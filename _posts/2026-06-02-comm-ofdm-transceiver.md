---
layout: post
title: OFDM 송수신기의 구성과 송수신 과정
date: 2026-06-01
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

참고: [ShapeLayer/simulate-ofdm-tx-rx](https://github.com/ShapeLayer/simulate-ofdm-tx-rx) - OFDM 송수신 시뮬레이션의 C 구현

![](/static/posts/2026-06-02-comm-ofdm-transceiver/overview.jpeg)

## 송신부
### Symbol Mapping

$$
b_n \Rightarrow \text{Symbol Mapping} \Rightarrow s_n
$$

<br />

Symbol Mapping은 비트스트림을 변조된 심볼로 변환하는 과정이다.  

QPSK의 경우에는 아래와 같이 비트를 그룹화하여 심볼로 매핑한다:

$$
b_n = [b_0, b_1], \quad b_i \in \{0, 1\}
$$

$b_0$ 은 실수부, In-phase component $I$, $b_1$ 은 허수부, Quadrature component $Q$

![](/static/posts/2026-06-02-comm-ofdm-transceiver/iq-graph.jpeg)  

<br />

$$
S_n = M(b_0, b_1) = \frac{1}{\sqrt{2}} \left[ (1 - 2b_0) + j(1 - 2b_1) \right]
$$

$$
\begin{aligned}
(b_0, b_1) = (0, 0) &\Rightarrow \frac{1}{\sqrt{2}} (1 + j) \\
(b_0, b_1) = (0, 1) &\Rightarrow \frac{1}{\sqrt{2}} (1 - j) \\
(b_0, b_1) = (1, 0) &\Rightarrow \frac{1}{\sqrt{2}} (-1 + j) \\
(b_0, b_1) = (1, 1) &\Rightarrow \frac{1}{\sqrt{2}} (-1 - j)
\end{aligned}
$$

### Time-domain으로 전환

이렇게 생성된 심볼 스트림은 주파수 도메인에서 표현된 것이므로, 이를 시간 도메인으로 변환하여 전송해야 한다. OFDM 시스템에서는 iDFT(Inverse Discrete Fourier Transform)를 사용하여 주파수 도메인에서 시간 도메인으로 변환한다.  

전환 처리를 효율적으로 처리하기 위해 심볼 스트림을 병렬 스트림으로 변환하여 iDFT 후 다시 Serial 스트림으로 변환한다.  

#### Serial to Parallel Converter

$$
S \Rightarrow \text{Serial to Parallel Converter} \Rightarrow X_m[k]
$$

<br />

![](/static/posts/2026-06-02-comm-ofdm-transceiver/sp-conv.jpeg)  

앞에서 생성한 심볼 스트림은 심볼이 시간 순서대로 나열된 직렬(Serial) 데이터이다. OFDM 시스템에서는 이 고속의 단일 스트림을 여러 개의 저속 병렬 스트림으로 나누어 처리한다.

시스템의 subcarrier 개수인 $N$에 맞추어 직렬 데이터를 한 번에 $N$개씩 묶어 병렬로 변환한다. 이렇게 분할된 $N$개의 복소 심볼은 주파수 도메인 상의 데이터로 취급되며, 이후 iDFT 연산의 병렬 입력으로 사용되어 $N$개의 부반송파에 각각 할당됨으로써 시간 도메인에서 동시에 전송된다.  

$$
S = \{S_0, S_1, \ldots, S_{N-1}\}, \quad S_n \in \mathbb{C}
$$  
Serial Stream $S$ 의 구성

$$
X_m[k] = S_{mN + k}, \quad m = 0, 1, \ldots, M-1, \quad k = 0, 1, \ldots, N-1
$$
병렬 스트림 $X_m[k]$ 의 구성, $m$ 은 OFDM symbol index, $k$ 는 subcarrier index, $N$ 은 FFT size(이 크기만큼 병렬 스트림으로 구성함)

이렇게 함으로써, 심볼 duration $T_X$ 는 $N T_S$ 로 늘어나 ISI를 줄이는 효과가 있다. 또한 subcarrier가 flat fading 채널로 간주되어 $T_S$ 에 대해 ISI 구간이 크다고 하더라도 $T_X$ 에 대해서는 상대적으로 작아지는 효과가 있다.  

#### iDFT

$$
X_m[k] \Rightarrow \text{iDFT} \Rightarrow x_m[n]
$$

<br />

주파수 도메인의 복소 변조 심볼을 iDFT를 사용해 시간 도메인으로 변환한다. 실제로는 고속 푸리에 변환(FFT)를 iDFT 처리에 사용한다. OFDM 심볼 인덱스 $m$, subcarrier 인덱스 $k$, FFT 크기 $N$ 에 대해 복소 변조 심볼 $X_m$ 은 다음과 같이 표현된다.  

$$
X_m = \{X_m[0], X_m[1], \ldots, X_m[N-1]\}
$$

$$
x_m[n] = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} X_m[k] e^{j \frac{2\pi k n}{N}}, \quad n = 0, 1, \ldots, N-1
$$

$m$ 번째 OFDM 심볼의 $n$ 번째 샘플 $x_m[n]$, $e^{j \frac{2 \pi k n}{N}}$ 은 basis function, Orthogonal 특성은 서로 다른 basis function에 의해 유지된다.  

#### Parallel to Serial Converter

$$
x_m \Rightarrow \text{Parallel to Serial Converter} \Rightarrow x[n]
$$

<br />

iDFT를 거친 병렬 시간 도메인 샘플을 Serial 스트림으로 되돌린다.  

병렬 스트림 $x_m[n]$, OFDM 심볼 인덱스 $m$, 샘플 인덱스 $n$ 에 대해, Serial 스트림 $x[n]$ 은 다음과 같이 표현된다.  

$$
x_m = \{x_m[0], x_m[1], \ldots, x_m[N-1]\}
$$

$$
x[n] = \sum_{k=0}^{N-1} x_m[k] \delta(n - k)
$$

OFDM 심볼 인덱스 $m$, 샘플 인덱스 $n$ 에 대해, 각 심볼 블록 $x_m[]$ 을 시간 순서로 이어 붙여 시리얼 스트림 $x[n]$ 을 구성한다. $x[n]$ 은 $m$ 번째 OFDM 심볼의 $n$ 번째 샘플이 된다.

### Cyclic Prefix 추가

$$
x[n] \Rightarrow \text{Add Cyclic Prefix} \Rightarrow \tilde{x}_m[n]
$$

<br />

OFDM 심볼의 끝 부분 신호를 시작 부분에 복사하여 추가한다.  

$$
\begin{aligned}
\tilde{x}_m[n] &= \begin{cases}
x_m[n + N - N_\text{CP}], & n = 0, 1, \ldots, N_\text{CP}-1 \quad \text{(CP)}\\
x_m[n - N_\text{CP}], & n = N_\text{CP}, N_\text{CP}+1, \ldots, N + N_\text{CP} - 1 \quad \text{(data)}\\
\end{cases}\\
&= x_m[(n - N_\text{CP}) \mod N], \quad 0 \le n \lt N + N_\text{CP}
\end{aligned}
$$

### Digital to Analog Converter

$$
\tilde{x}_m[n] \Rightarrow \text{Digital to Analog} \Rightarrow \tilde{x}_{BB}(t)
$$

<br />

디지털 타임 도메인 신호를 RF 전송을 위해 연속적인 아날로그 신호로 변환한다.  

$$
s_\delta (t) = \sum_{n = 0}^{N + N_\text{CP} - 1} \tilde{x}_m[n] \delta(t - nT_s)
$$

\* $s_\delta (t)$ 는 $t$ 에서 샘플링된 신호, $T_s$ 는 샘플링 duration

$$
s_{BB}(t) = s_\delta (t) * p(t) = \sum_{n=0}^{N + N_\text{CP} - 1} \tilde{x}_m[n] p(t - nT_s)
$$

\* $p(t)$ 는 sinc 함수 등의 펄스 함수이다.  

### IQ Modulation & Up-conversion

$$
s_{BB}(t) \Rightarrow \text{IQ Modulation / Up-conversion} \Rightarrow s(t)
$$

<br />

baseband 디지털 데이터를 RF 대역 신호로 변환한다.  

I/Q Modulation은 In-phase component $I(t)$ 와 Quadrature component $Q(t)$ 를 사용하여 복소 신호를 표현한다.  

$$
I(t) = \Re\{s_{BB}(t)\}, \quad Q(t) = \Im\{s_{BB}(t)\}
$$

이들 신호를 Up-conversion하여 RF 대역으로 변환한다. ($f_c$ 는 carrier frequency)  

$$
s(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)
$$

$$
s(t) = \Re\{s_{BB}(t) e^{j 2\pi f_c t}\}
$$

## 채널

$$
\text{Tx } s(t) \Rightarrow \text{Channel} \Rightarrow \text{Rx } y(t)
$$

생성된 RF 신호는 무선 채널을 겪는다. 채널에 의해 신호가 감쇠되고, 다중 경로로 인해 지연과 페이딩이 발생하며, 잡음이 추가된다.  

신호가 겪는 채널을 수학적으로 모델링하여 전송 과정을 시뮬레이션할 수 있는데, 일반적으로 선형 시불변 시스템으로 모델링한다. 채널의 impulse response $h(t)$ 와 입력 신호 $s(t)$ 에 대해, 수신 신호 $y(t)$ 는 다음과 같이 표현된다.

$$
\begin{aligned}
y(t) &= s(t) * h(t) + n(t) \\
&= \int_{-\infty}^{\infty} s(\tau) h(t - \tau) d\tau + n(t)
\end{aligned}
$$

$$
s(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)
$$

## 수신부

수신부에서는 채널을 거쳐 수신된 신호 $y(t)$ 를 처리하여 원래의 비트스트림 $b_n$ 을 복원한다. 수신 과정은 송신 과정의 역과정으로 구성된다.

### Down-conversion & IQ Demodulation

$$
y(t) \Rightarrow \text{Down-conversion / IQ Demodulation} \Rightarrow s_{BB}(t)
$$

<br />

고주파 아날로그 RF 신호를 baseband 디지털 신호로 변환한다.  

Down-conversion은 수신된 RF 신호를 낮은 주파수로 변환하는 과정이다.

$$
\begin{aligned}
y_{I}(t) &= y(t) \cos(2\pi f_c t) \\
y_{Q}(t) &= y(t) (-\sin(2\pi f_c t))
\end{aligned}
$$

이어서 Low-pass filter를 적용하여 baseband 신호 $s_{BB}(t)$ 를 얻는다.

$$
s_{BB}(t) = I_\text{rec}(t) + j Q_\text{rec}(t)
$$

$$
\begin{aligned}
I_\text{rec}(t) &= \text{LPF}\{y_I(t)\} \approx I(t) \\
\quad Q_\text{rec}(t) &= \text{LPF}\{y_Q(t)\} \approx Q(t)
\end{aligned}
$$

### Analog to Digital Converter

$$
s_{BB}(t) \Rightarrow \text{Analog to Digital} \Rightarrow y[n]
$$

<br />

아날로그 baseband 신호를 디지털 샘플로 변환한다.  

샘플링 기간 $T_s$, baseband 대역폭 $W_{BB}$ 에 대해 $f_s = \frac{1}{T_s} \ge 2W_{BB}$ 의 관계를 가질 때, 샘플링 신호 $s_{BB}(t)$ 는 다음과 같이 표현된다.

$$
s_{BB}[n] = s_{BB} (nT_s) = I_\text{rec}(nT_s) + j Q_\text{rec}(nT_s)
$$

이어서 양자화 과정과 디지털 프론트엔드 처리를 거쳐 디지털 샘플 $y[n]$ 을 얻는다. 디지털 프론트엔드 처리에서 양자화 오류를 억제하고 DC 성분을 제거한다.  

$$
y[n] = \mathcal{Q}\{s_{BB}[n]\}
$$

$$
y[n] = \text{DFE}\{y[n]\}
$$

### Cyclic Prefix 제거

$$
y[n] \Rightarrow \text{Remove Cyclic Prefix} \Rightarrow \tilde{y}[n]
$$

<br />

$N_\text{CP}$ 개의 샘플로 구성된 cyclic prefix를 제거하여 $N$ 개의 샘플로 구성된 OFDM 심볼을 얻는다. 심볼 인덱스 $m$, 샘플 인덱스 $n$, cyclic prefix 길이 $N_\text{CP}$, FFT 크기 $N$ 에 대해, 수신된 샘플 스트림 $y[n]$ 과 CP가 제거된 샘플 스트림 $\tilde{y}[n]$ 는 다음과 같다.  

$$
y_m[n], \quad n = 0, 1, \ldots, N + N_\text{CP} - 1
$$

$$
\tilde{y}_m[k] = y_m[k + N_\text{CP}], \quad k = 0, 1, \ldots, N - 1
$$

### DFT

#### Serial to Parallel Converter

$$
\tilde{y}_m[n] \Rightarrow \text{Serial to Parallel Converter} \Rightarrow y_m
$$

시간 도메인의 고속 시리얼 스트림을 병렬 스트림으로 변환한다. 병렬 스트림 $y_m$ 은 OFDM 심볼 인덱스 $m$, FFT 크기 $N$ 에 대해 표현된다.  

$$
y_m = \begin{bmatrix}
\tilde{y}_m[0] \\
\tilde{y}_m[1] \\
\vdots \\
\tilde{y}_m[N-1]
\end{bmatrix}
$$

#### DFT

$$
y_m \Rightarrow \text{DFT} \Rightarrow Y_m[k]
$$

<br />

수신한 시간 도메인 신호를 DFT를 사용하여 주파수 도메인으로 변환한다. 실제로는 고속 푸리에 변환(FFT)을 DFT 처리에 사용한다. OFDM 심볼 인덱스 $m$, subcarrier 인덱스 $k$, FFT 크기 $N$ 에 대해, DFT 결과인 주파수 도메인 신호 $Y_m[k]$ 는 다음과 같이 표현된다.  

$$
\begin{aligned}
Y_m[k] &= \frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} \tilde{y}_m[n] e^{-j \frac{2\pi k n}{N}}, \quad k = 0, 1, \ldots, N-1 \\
&= (\mathbf{W}_N \mathbf{y}_m)_k
\end{aligned}
$$

$\exp(-j \frac{2\pi k n}{N})$ 는 subcarrier에 대한 상관기 역할이다.

### Equalization

$$
Y_m[k] \Rightarrow \text{Equalization} \Rightarrow \hat{X}_m[k]
$$

<br />

채널 왜곡을 보상하여 전송 심볼을 복원한다. 

Zero-forcing equalizer의 경우, 채널의 주파수 응답 $H[k]$ 에 대해 다음과 같이 표현된다. DFT를 통과한 수신 신호 $Y_m[k]$, Zero-forcing Equalizer의 출력 $\hat{X}_m[k]$ 는 다음과 같다.  

$$
Y_m[k] = H_m [k] X_m[k] + N_m[k]
$$

$$
\hat{X}_m[k] = G_\text{ZF}[k] Y_m[k] = X_m[k] + \frac{N_m[k]}{H_m[k]}
$$

만약 $G_\text{ZF}[k] = \frac{1}{H_m[k]}$ 라면, 채널 왜곡이 완전히 보상되어 $X_m[k]$ 가 복원된다. 하지만, 채널 응답이 작은 경우에는 잡음이 증폭될 수 있다.  

### Symbol Demapping

$$
\hat{X}_m[k] \Rightarrow \text{Symbol Demapping} \Rightarrow \hat{b}_m[k]
$$

<br />

Demodulated된 복소 점을 원래의 비트로 매핑하는 과정이다.  

Equalization 단계에서 Zero-forcing equalizer를 사용해 점 $\hat{X}_m[k]$ 를 얻었다면, Symbol Demapping은 이 점을 가장 가까운 constellation point로 매핑하여 원래의 비트 $b_n$ 을 복원한다.

$$
\hat{X}_m[k] = G_\text{ZF}[k] Y_m[k] = X_m[k] + \frac{N_m[k]}{H_m[k]}
$$

만약 QPSK로 심볼이 변조되었다면, $S_n$ 의 constellation point는 다음과 같이 표현된다.  

$$
S_n = \frac{1}{\sqrt{2}} \left[ (1 - 2b_0) + j(1 - 2b_1) \right]
$$

점을 결정하는 방법에 따라 Hard Decision 또는 Soft Decision이 사용될 수 있다. Hard Decision에서는 가장 가까운 constellation point로 매핑하여 비트를 결정한다. Soft Decision에서는 점과 constellation point 간의 거리를 기반으로 비트의 신뢰도를 계산하여 복원한다.  

<br />

Hard Decision의 경우, $S_n$ 의 constellation point에 대해 다음과 같이 표현된다. 임계점을 설정하여 0, 1을 결정한다.  

$$
\Re\{\hat{X}_m[k]\} \ge 0 \Rightarrow b_0 = 0, \quad \Re\{\hat{X}_m[k]\} < 0 \Rightarrow b_0 = 1
$$

$$
\Im\{\hat{X}_m[k]\} \ge 0 \Rightarrow b_1 = 0, \quad \Im\{\hat{X}_m[k]\} < 0 \Rightarrow b_1 = 1
$$

<br />

Soft Decision의 경우, $S_n$ 의 constellation point에 대해 다음과 같이 표현할 수 있다. 아래 식에서는 Real part 값의 크기를 Noise로 나누어 $\sigma$ 를 획득해 사용한다.  

$$
\text{LLR}(b_0) = 2 \Re\{\hat{X}_m[k]\} / \sigma^2, \quad \text{LLR}(b_1) = 2 \Im\{\hat{X}_m[k]\} / \sigma^2
$$

### Parallel to Serial Converter

$$
\mathbf{b}_m[k] \Rightarrow \text{Parallel to Serial Converter} \Rightarrow \mathbf{B}
$$

<br />

이렇게 획득한 비트는 실수부와 허수부 두 개의 비트가 하나의 심볼로 그룹화되어있다. 따라서 병렬 비트를 연속된 시리얼 비트로 변환해야 한다.  

subcarrier 인덱스 $m$, 비트 인덱스 $k$ 에 대한 병렬 비트 스트림 $\mathbf{b}_m [k]$ 는 이 과정을 거치며 Serial 비트 스트림 $\mathbf{B}$ 로 변환된다. $N$ 은 OFDM Symbol의 subcarrier 수이다.    

$$
\mathbf{B} = \begin{bmatrix}
\mathbf{b}_0, \mathbf{b}_1, \ldots, \mathbf{b}_{N-1}
\end{bmatrix}
$$
