---
layout: post
title: 안테나 구성하기
date: 2026-06-07
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

## Single Input Single Output (SISO)

무선 통신 시스템에서 가장 기본적인 안테나 구성으로 한 개의 Tx 안테나(Single Input)와 한 개의 Rx 안테나(Single Output)를 사용하는 구성이다. SISO 시스템에서는 Tx에서 전송된 신호가 하나의 채널을 통해 Rx로 전달된다. SISO 시스템은 구현이 간단하고 비용이 저렴하지만, 다중 경로 효과와 같은 채널 왜곡에 취약할 수 있다.  

무선 채널 $h$, Tx에서 전력 $P = \mathbb{E}[|x|^2]$ 로 전송된 심볼 신호 $s$, AWGN 채널 노이즈 $z$ 가 존재하는 SISO 시스템에서, Rx에서 수신된 신호 $y$ 는 다음과 같이 표현할 수 있다.  

$$
y = h s + z
$$

이 때 달성할 수 있는 data rate $R$ 는 Shannon-Hartley theorem에 의해 다음과 같이 표현할 수 있다.  

$$
R = \log_2(1 + \gamma) = \log_2(1 + \frac{|h|^2 P}{N_0}) \text{ bits/s/Hz}
$$  

## 채널 용량 확보하기

![](/static/posts/2026-06-07-comm-antenna-configuration/div-mul.png)  

채널 용량을 확보하기 위해서 Diversity와 Multiplexing을 활용할 수 있다. Diversity는 여러 개의 안테나를 사용해, 다중 경로 효과로 발생하는 신호 왜곡을 보완하는 방법이다. Multiplexing은 여러 개의 안테나를 사용해, 동시에 여러 개의 데이터 스트림을 전송하는 방법이다. 이 방법을 사용하여 채널 용량을 증가시킬 수 있다.  

<br />

$$
R = \log_2(1 + N \times \text{SNR}) \text{ bits/s/Hz}
$$

_Diversity에서 채널 용량 $R$_

Diversity 전략으로는 통신의 안정성을 높일 수 있다.  

<br />

$$
R = N \log_2(1 + \text{SNR}) \text{ bits/s/Hz}
$$

_Multiplexing에서 채널 용량 $R$_

Multiplexing 전략으로는 통신의 데이터 전송량을 높일 수 있다.

## Single Input Multiple Output (SIMO)

$$
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_M \\
\end{bmatrix}
=
\begin{bmatrix}
g_1 \\
g_2 \\
\vdots \\
g_M \\
\end{bmatrix}
x +
\begin{bmatrix}
n_1 \\
n_2 \\
\vdots \\
n_M \\
\end{bmatrix}
$$

$$
\mathbf{y} = \mathbf{g} x + \mathbf{n}
$$

<br />

한 개의 Tx, 여러 개의 Rx로 구성하는 SIMO 시스템에서는 MRC(Maximal Ratio Combining), SC(Selection Combining)등의 방법을 사용해 여러 개의 신호를 가중 합산하여 신호를 처리한다.  

<br />

Selection Combining

여러 개 채널에 다 동일한 신호를 전송할 때, 가장 SNR이 높은 채널을 선택해 신호를 처리할 수 있다. 이 방법을 SC(Selection Combining)이라고 한다.

$$
\gamma_\text{sc} = \max_l\gamma_l = \max_l \frac{P_s \vert h_l \vert^2}{N_0} = \frac{P_s}{N_0} \max_l \vert h_l \vert^2
$$

이 시스템의 성능 지표로서 장애 확률(Outage Probability)을 사용할 수 있다. 장애 확률 $\mathbb{P} [\text{SNR} < \gamma_\text{th}]$ 은 SNR이 특정 임계값 $\gamma_\text{th}$ 이하로 떨어질 확률이다.  

$$
P_o = \text{Pr} \left[ \gamma_\text{sc} < \gamma_\text{th} \right] = \text{Pr} \left[ \max_l \vert h_l \vert^2 < \gamma'_\text{th} \right] = \text{Pr} \left[ \vert h_l \vert^2 < \gamma'_\text{th} \right]
$$

\* $l$ 은 Diversity order

## Multiple Input Single Output (MISO)

여러 개의 Tx, 한 개의 Rx로 Multiple Input Single Output(MISO) 시스템을 구성할 수도 있다. Rx 측에서 수신하는 신호 $y$ 는 아래와 같이 모델링할 수 있다.  

$$
y = \begin{bmatrix} h_1 & h_2 & \cdots & h_M \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_M \end{bmatrix} + n = \mathbf{h}^T \mathbf{x} + n
$$

<br />

이렇게 Tx 측에서 여러 개의 신호를 사용할 때는 신호들이 엉키지 않도록 사전에 신호를 적절하게 가공해야 한다. 이 때 CSI를 어느 측에서 알고 있는지에 따라 전략을 다르게 사용할 수 있다.  

### CSIT: Tx 측에서 CSI를 알고 있는 경우

여러 경로를 사용하는 Tx 측에서 CSI를 알고 있다면, 어느 경로로 신호를 더 적극적으로 송신할 지 결정할 수 있다.

대표적으로는 최대비 송신 방법(MRT; Maximum Ratio Transmission)이 있다. 이 방법은 각 송신 안테나 신호에 가중치를 두어 결합 효율을 극대화하는 데 목표를 둔다. Rx 측의 최대비 결합(MRC)의 Tx 측 사용법이다.  

$$
\sum_{l=1}^L \vert w_l \vert^2 = 1
$$

$$
\max_{w_l} \gamma_l = \max_{w_l} \frac{P_s \sum_{l=1}^L |h_l|^2}{N_0} = \sum_{l=1}^L \gamma_l
$$


위 식에서는 $L$ 개 송신 안테나에 각각 가중치 $w_l$ 을 곱하여 송신 신호의 SNR을 최대화하려고 하고 있다. 이 때 가중치 $w_l$ 의 제곱 합(전력의 합)을 1로 규제하여 전체 송신 전력을 키우지 않고, 주어진 전력 내에서 가중치 배분만으로 SNR을 최대화하는 것이 목표이다.  

채널이 $r_c$ 와 같이 결합된다고 할 때, 가중치가 반영되는 수신 SNR 식은 다음의 과정을 거쳐 전개된다. 각 채널을 거치는 신호 $r_l$ 에 가중되는 $w_l$ 은 일종의 증폭기로서 작용한다. SNR이 높은 채널에 더 큰 가중치를 주어 이득을 취할 수 있으므로, 다음와 과정을 거쳐 가중치 $w_l$ 을 결정할 수 있다.    

$$
r_c = \sum_{l=1}^L r_l w_l = \sum_{l=1}^L (h_l s + z) w_l
$$

$$\text{SNR} = \frac{P_s \vert \sum_{l=1}^L h_l w_l \vert^2}{N_0 \sum_{l=1}^L \vert w_l \vert^2}$$

이어서 코시-슈바르츠 부등식에 의해 $w_l$ 의 최대치를 구할 수 있다.  

$$
\vert \sum_{l=1}^L h_l w_l \vert^2 \leq \sum_{l=1}^L \vert h_l \vert^2 \sum_{l=1}^L \vert w_l \vert^2
$$

$$
\sum_{l=1}^L \vert w_l \vert^2 = 1
$$

$$
c = \frac{1}{\sqrt{\sum_{l=1}^L \vert h_l \vert^2}}
$$

$$
w_l = c \cdot h_l^* = \frac{h_l^*}{\sqrt{\sum_{l=1}^L \vert h_l \vert^2}}
$$

### CSIR: Rx 측에서 CSI를 알고 있는 경우

Tx 측에서 채널 상황을 제대로 알고 있지 못하다면, Tx 측에서는 앞의 시나리오에서 살펴본 전처리 방법을 사용할 수 없다. 때문에 신호를 추가적인 방법으로 부호화하여 Rx 측에 전송한다.

어떤 안테나(공간)으로 언제(시간) 신호를 보낼지 부호화한 매트릭스를 사용하는데, 이것을 시공간 부호화(Space-time Coding)라고 한다. 

## Multiple Input Multiple Output (MIMO)

SIMO와 MISO 시스템은 full diversity를 달성할 수 있다. 하지만 MISO는 전력 손실이 발생할 수 있고, SIMO는 multiplexing gain을 달성할 수 없다. 그래서 Tx와 Rx 양측에서 여러 개의 안테나를 사용하는 MIMO 구성으로 이 문제를 보완할 수 있다.  

<br />

$$
R = N \log_2(1 + \text{SNR})
$$

\* $N = \min(N_t, N_r)$ : 병렬 채널의 수

MIMO 시스템은 Tx, Rx 양측에서 여러 개의 안테나를 사용하여 spatial multiplexing한다. MIMO 채널은 다수의 독립적이고 병렬적인 채널을 생성할 수 있고, 덕분에 안테나 개수에 선형적으로 비례해 증가하는 채널 용량을 달성할 수 있다. 안테나 개수에 logarithmic하게 증가하는 SIMO와 MISO 시스템과 구분되는 특징이다.    

만약 SIMO 시스템에서 15배의 채널 용량을 달성하려면 극단적인 SNR 값이 필요($2^{15}$) 하지만, MIMO 시스템에서는 $N$ 이 15배 증가하는 것만으로도 달성할 수 있다.  

<br />

MIMO의 병렬 채널 용량 $C$ 는 다음과 같이 표현할 수 있다.  

$$
C = \sum_{i=1}^{n_\text{min}} \log_2(1 + \lambda_i P^*_i / \sigma^2)
$$

\* $n_\text{min} = \min(N_t, N_r)$ : 병렬 채널의 수 (=Multiplexing gain)  
\*\* $\lambda_i$ : 병렬 채널 $i$ 의 채널 퀄리티

### 단일 유저 MIMO(point-to-point MIMO)

![](/static/posts/2026-06-07-comm-antenna-configuration/ch-mat-h.jpeg)  
각 개별 유저에 대해서 MIMO 시스템은 Tx 신호 $\mathbf{x}$와 Rx 신호 $\mathbf{y}$ 사이의 채널 매트릭스 $\mathbf{H}$를 모델링할 수 있다. $\mathbf{H}$는 Tx 안테나와 Rx 안테나 사이의 채널 이득을 나타내는 매트릭스이다. 수신 안테나 개수가 $N_r$, 송신 안테나 개수가 $N_t$일 때, 채널 매트릭스 $\mathbf{H}$의 크기는 $N_r \times N_t$이며 다음과 같이 표현된다.

$$
\mathbf{H} = \begin{bmatrix}
h_{11} & h_{12} & \cdots & h_{1N_t} \\
h_{21} & h_{22} & \cdots & h_{2N_t} \\
\vdots & \vdots & \ddots & \vdots \\
h_{N_r1} & h_{N_r2} & \cdots & h_{N_rN_t} \\
\end{bmatrix}
$$

<br />

MIMO 채널 행렬에 특잇값 분해(SVD)를 적용하면 $\mathbf{H} = \mathbf{U} \mathbf{\Lambda} \mathbf{V}^*$로 나타낼 수 있다. 이때 송신단 프리코딩으로 $\mathbf{x} = \mathbf{V}\tilde{\mathbf{x}}$를 적용하여 신호를 전송하면, 수신단으로 전달되는 과정은 다음과 같이 전개된다.

$$
\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{w} = (\mathbf{U} \mathbf{\Lambda} \mathbf{V}^*)(\mathbf{V}\tilde{\mathbf{x}}) + \mathbf{w} = \mathbf{U} \mathbf{\Lambda} \tilde{\mathbf{x}} + \mathbf{w}
$$

<br />

수신단에서 변환 행렬 $\mathbf{U}^*$를 곱하는 포스트코딩(Postcoding)을 수행하면, 유니터리 행렬의 성질($\mathbf{U}^*\mathbf{U} = \mathbf{I}$)에 의해 다음과 같이 복잡한 간섭이 제거된 독립 병렬 채널을 얻을 수 있다.

$$
\begin{aligned}
\mathbf{U}^*\mathbf{y} &= \mathbf{U}^* \mathbf{U} \mathbf{\Lambda} \tilde{\mathbf{x}} + \mathbf{U}^*\mathbf{w} \\
&= \mathbf{\Lambda} \tilde{\mathbf{x}} + \mathbf{U}^*\mathbf{w}
\end{aligned}
$$

$$
\mathbf{\Lambda} = \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_{n_\text{min}} \\
\end{bmatrix}
$$

<br />

각 수신 신호와 잡음 벡터를 $\tilde{\mathbf{y}} = \mathbf{U}^*\mathbf{y}$, $\tilde{\mathbf{w}} = \mathbf{U}^*\mathbf{w}$로 치환하면 최종적으로 다음과 같은 병렬화 채널 식이 완성된다.

$$
\tilde{\mathbf{y}} = \mathbf{\Lambda}\tilde{\mathbf{x}} + \tilde{\mathbf{w}}
$$

### Multi-user MIMO 상황에서 전통적 접근법

![](/static/posts/2026-06-07-comm-antenna-configuration//multi-user-mimo.png)  

개별 유저에 대한 MIMO(point-to-point MIMO) 시스템에서는 양 측이 여러 개의 안테나로 구성된 단일 Tx와 단일 Rx에 대해서만 고려되었으나, 실제 통신 환경에서는 여러 개의 Tx와 여러 개의 Rx가 상호작용한다.(Multi-user MIMO)

다중 유저에 대해서도 diversity를 달성하기 위한 전통적인 접근법 중 하나로, 평탄화 전략이 있다. 평탄화를 사용하면 채널 이득이 낮아도 신호를 안정적으로 관리할 수 있다.  

![](/static/posts/2026-06-07-comm-antenna-configuration/equation.png)  

무선 채널은 주변의 건물이나 장애물에 반사되어 들어오는 다중 경로 신호들 때문에, 수신 감도가 순간적으로 현저히 낮아질 수 있다.(Deep fading) 하지만 모든 신호가 동시에 딥 페이딩에 빠질 확률은 극히 낮기 때문에 시간, 주파수, 공간 차원에서 평탄화하여 딥 페이딩의 영향을 완화한다.  

### 사용자 기회주의적 스케줄링

만약 각 스케줄링 타이밍마다 좋은 채널을 갖고 있는 유저에 대해서만 스케줄링한다면, 시스템 전체 시각에서는 시스템의 안정성이 증가하는 것처럼 보인다. 일종의 눈속임처럼 보일 수 있어도, 대개는 특정한 유저만 모든 타이밍에서 나쁜 채널을 갖는 상황은 드물기 때문에, 실제로도 시스템의 안정성이 증가할 수 있다.  

이 방식에서 기지국은 매 순간 채널의 상태를 모니터링하면서, 채널이 가장 좋은 사용자를 파악한다. 이 과정 중에 스케줄링 타이밍이 되면, 채널이 가장 좋은 사용자에게 시스템의 자원을 몰아주어 그 사용자에게 높은 데이터 전송률을 제공한다.  
