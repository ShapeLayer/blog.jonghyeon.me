---
layout: post
title: 자유공간에서의 전파
date: 2026-04-12
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## 등방형 방사기

무선통신시스템에서는 모든 방향으로 똑같은 이득을 가지고 전력을 방사하는 이상형 안테나, 등방형 방사기(isotropic radiator)를 가정하여 전파의 세기를 가정한다.  

등방형 안테나의 전파 범위는 구면으로 간주되어 송신전력 $P_t$ (W)와 안테나로부터의 거리 $d$ (m)에 대해서 다음과 같이 표현된다.  

$$
P_D = P_t / 4 \pi d^2 (W/ m^2)
$$

### 예시 계산

만약 송신전력 100와트의 등방형 방사기가 방사하는 신호를 10km 떨어진 점에서 수신한다면, 수신되는 신호의 세기는 다음과 같이 계산된다.  

![](/static/posts/2026-04-12-comm-propagation-in-free-space/isotropic-radiator.png)

$$
\begin{aligned}
P_D &= \frac{100}{4 \pi \times (10 \times 10^3 m)^2} \\
&\approx 7.96 \times 10^{-8} W/m^2 \\
&= 79.6 nW/m^2
\end{aligned}
$$

## 안테나 이득 $G_t$

안테나에서 전파를 송수신하면서 안테나의 송수신 감도를 확인하기 위해 안테나 이득을 정의한다. 안테나 이득은 어떠한 레퍼런스 안테나 전력 밀도를 기준으로, 실제로 어떠한 지향성 안테나의 전력 밀도가 얼마나 더 큰지를 나타내는 지표이다. 이 때 레퍼런스 안테나는 등방형 방사기를 기준으로 한다.  

안테나 이득 $G_t$ 는 실제 안테나로부터 주어진 방향에서의 전력 밀도 $P_{DA}$, 동일한 전력을 가진 등방성 안테나로부터 같은 거리에서의 전력 밀도 $P_{DI}$ 의 비율로 정의된다.  

$$
G_t = \frac{P_{DA}}{P_{DI}}
$$

* $P_{DA}$: 실제 안테나로부터 주어진 방향에서의 전력 밀도
* $P_{DI}$: 동일한 전력을 가진 등방성 안테나로부터 같은 거리에서의 전력 밀도

이와 같이 정의함으로써, "이득이 1인 등방성 안테나에 비해 내가 사용하는 안테나가 특정 방향으로 몇 배나 더 강한 전력을 보내는가"를 평가한다.  

<br />

안테나 이득도 신호의 세기와 마찬가지로 로그 스케일로 표현하는 것이 더 편할 때가 있다. 그래서 안테나 이득도 데시벨을 이용해서 정의할 수 있다. dBi(Decibel relative to isotropic)로 다음과 같이 표현한다.

$$
G_t \left[\text{dBi}\right] = 10 \log_{10} \left(\frac{P_{DA}}{P_{DI}}\right)
$$

<br />

안테나 이득은 결국 등방형 안테나와 지향성 안테나의 전력 밀도의 비율이므로, 지향성을 가지는 안테나에 대해 수신 전력 밀도를 계산할 때 $G_t$ 를 안다면, $G_t$ 를 곱하여 계산한다. 

$$
P_{DA} = G_t \times P_{DI}
$$

$$
\begin{aligned}
P_D &= P_{DA} = G_t \times P_{DI} \\
&= G_t \cdot \frac{P_t}{4 \pi d^2} \\
&= \frac{P_t G_t}{4 \pi d^2}
\end{aligned}
$$

수신 전력 밀도 $P_D$ 는 실제 안테나로부터 주어진 방향에서의 전력 밀도이므로, 지향성 안테나의 수신 전력 밀도 $P_{DA}$ 와 같다고 가정하고, 안테나 이득 $G_t$ 와 송신 전력 $P_t$ 의 곱으로 표현, $P_D$ 와 $P_t$, $G_t$ 의 관계를 확인할 수 있다.  

## EIRP: 최대 송신 전력, ERP: 실효 송신 전력

이렇게 $P_t$ 와 $G_t$ 를 구했을 때, 전파가 특정 방향으로 얼마나 강하게 방사되는지 평가할 수 있다.  

최대송신전력(EIRP; Effective Isotropic Radiated Power)이라고 정의되는 지표가 있는데, 송신되는 전력 $P_t$ 와 안테나 이득 $G_t$ 를 곱한 값이다.  

$P_t$ 와 $G_t$ 는 앞서 $P_D$ 와의 관계에서 확인한 바와 같으므로 다음과 같이 정리할수 있기도 하다.  

$$
\begin{aligned}
\text{EIRP} &= P_t \cdot G_t \\
&= P_D \cdot 4 \pi d^2
\end{aligned}
$$

<br />

실효 송신 전력(ERP; Effective Radiated Power)은 등방성 안테나가 아니라 지향성을 갖는 반파장 다이폴 안테나(half-wave dipole antenna)를 기준으로 하는 지표이다. 일반적으로 등방성 안테나보다 약 1.64배(2.15dB)의 지향성 이득을 가진다.  

$$
\begin{aligned}
\text{ERP} \text{[dBm]} &= \text{EIRP} \text{[dBm]} - G_d \text{[dB]} \\
&= P_t \cdot G_t - 2.15 \text{\text{[dB]}}
\end{aligned}
$$

ERP는 반파장 다이폴 안테나를 기준으로 하는 지표이므로, 로그 스케일 표현에서 조금 다른 단위를 사용한다. 다이폴 안테나에 대한 상대적 데시벨 dBd(Decibel relative to dipole)은 다음과 같은 관계를 갖는다.  

$$
G_t \left[\text{dBd}\right] = G_t \left[\text{dBi}\right] - 2.15 \text{\text{[dB]}}
$$

### 예시 계산

5dBi의 이득을 가진 안테나가 송신전력 100W의 신호를 방사할 때, 10km 떨어진 점에서의 EIRP와 전력 밀도는 다음과 같이 계산한다.  

우선 처음 전력비에 대한 이득을 획득하기 위해 5dBi를 선형 스케일로 변환한다.  

$$
G_t = \log^{-1}(\frac{5}{10}) = 10^{\frac{5}{10}} \approx 3.16
$$

혹은 dBi로 표현된 관계식을 사용한다. 

$$
\begin{aligned}
G_t \left[\text{dBi}\right] &= 10 \log_{10} \left(\frac{P_{DA}}{P_{DI}}\right) \\
5 &= 10 \log_{10} \left(\frac{P_{DA}}{P_{DI}}\right) \\
\frac{P_{DA}}{P_{DI}} &= 10^{\frac{5}{10}} \approx 3.16
\end{aligned}
$$

이렇게 획득한 값은 주어진 방향에서 EIRP가 실제 송신 전력의 약 3배임을 의미한다. 따라서 EIRP는 다음과 같이 계산된다.  

$$
\begin{aligned}
\text{EIRP} &= G_t P_t = \frac{P_{DA}}{P_{DI}} \cdot P_t \\
&= 3.16 \cdot 100 \text{W} \\
&= 316 \text{W}
\end{aligned}
$$

전력밀도는 EIRP로부터 도출할 수 있다.  

$$
\begin{aligned}
P_D &= \frac{\text{EIRP}}{4 \pi d^2} = \frac{316}{4 \pi \times (10 \times 10^3)^2} \\
&\approx 2.51 \times 10^{-7} W/m^2 \\
&= 251 nW/m^2
\end{aligned}
$$

## 전자장 강도

전자장 강도(electric field strength)는 전자기파의 세기를 표현하는 또 다른 지표이다. 단위는 V/m(볼트/미터)로 표현된다.  

미터 당 전자장 강도 $\epsilon$ 는 전력 밀도 $P_D$ 와 다음과 같은 관계를 갖는다. 이 관계는 전력 $P$, 전압 $V$, 저항 $R$의 관계를 전자 혹은 자기장 단위로 표현한 것이다.  

$$
P_D = \frac{\epsilon^2}{Z}
$$

$$
P = \frac{V^2}{R}
$$

자유공간의 임피던스 특성 $Z_0$ 은 약 377 $\Omega$ 이다. 따라서 자유공간에서의 전자장 강도 $\epsilon$ 는 다음과 같이 표현된다.  

$$
\begin{aligned} 
\epsilon &= \sqrt{Z_0 P_D} = \sqrt{377 \cdot P_D} \\
&= \sqrt{377 \cdot \frac{\text{EIRP}}{4 \pi d^2}} \approx \frac{\sqrt{30 \text{EIRP}}}{d} \\
\end{aligned}
$$

### 예시 계산

만약 위에서 구했던, EIRP가 316W인 신호가 10km 떨어진 점에서 수신된다면, 전자장 강도는 다음과 같이 계산된다.  

$$
\begin{aligned}
\epsilon &= \sqrt{377 P_D} = \sqrt{377 \times 251.5 \times 10^{-9}} \\
&= \sqrt{9.48 \times 10^{-5}} \\
&\approx 9.74 \times 10^{-3} V/m \\
&= 9.74 mV/m
\end{aligned}
$$

혹은 

$$
\begin{aligned}
\epsilon &= \frac{\sqrt{30 \text{EIRP}}}{d} = \frac{\sqrt{30 \times 316}}{10 \times 10^3} \\
&= \frac{\sqrt{9480}}{10^4} \\
&\approx \frac{97.4}{10^4} \\
&= 9.74 \times 10^{-3} V/m \\
&= 9.74 mV/m
\end{aligned}
$$

## 안테나의 유효면적

안테나의 유효면적(effective area)은 안테나가 수신하는 전력을 표현하는 지표이다. 안테나의 유효면적 $A_\text{eff}$ 는 다음과 같이 정의된다.  

$$
A_\text{eff} \text{[m}^2\text{]} = \frac{P_r \left[\text{W}\right]}{P_D \left[\text{W/m}^2\right]}
$$

이 관계를 이용하여 수신전력, 안테나의 이득과의 관계를 표현하거나 Friis 전송 방정식을 활용할 수 있다.  

$$
\begin{aligned}
P_r &= A_\text{eff} P_D \\
&= A_\text{eff} \cdot \frac{P_t G_t}{4 \pi d^2}
\end{aligned}
$$

\* 이 관계에서 안테나의 면적이 클 수록 더 많은 에너지를 흡수한다는 것을 알 수 있다.  

자유 공간에서 두 안테나 사이의 송수신 전력 관계를 나타내는 데 있어 Friis 전송 공식을 사용할 수 있다. Friis 공식은 수신 전력 $P_r$ 가 송신 전력 $P_t$, 송신 안테나 이득 $G_t$, 수신 안테나 이득 $G_r$, 그리고 송수신 간의 거리 $d$ 와 파장 $\lambda$ 의 관계로 정의된다.  

$$
P_r = P_t G_t G_r \left(\frac{\lambda}{4 \pi d}\right)^2
$$

Friis 공식을 활용해 안테나의 유효면적을 파장과 송신 안테나 이득으로 표현할 수 있다.  

$$
\begin{aligned}
\frac{P_t G_t}{4 \pi d^2} A_\text{eff} &= P_t G_t G_r \frac{\lambda^2}{(4 \pi)^2 d^2} \\
\frac{\cancel{P_t G_t}}{\cancel{4 \pi d^2}} A_\text{eff} &= \cancel{P_t G_t} G_r \frac{\lambda^2}{4 \pi\cdot \cancel{4 \pi d^2}} \\
A_\text{eff} &= \frac{\lambda^2 G_r}{4 \pi}
\end{aligned}
$$

따라서 수신 안테나의 이득 $G_r$ 도 안테나의 유효면적 $A_\text{eff}$ 와 파장 $\lambda$ 의 관계로 표현할 수 있다.  

$$
G_r = \frac{4 \pi A_\text{eff}}{\lambda^2}
$$

## 송신기로부터 거리가 $d$ 떨어진 수신기의 수신전력

지금까지 도출된 관계를 정리하면 다음과 같다.

$$
\begin{aligned}
P_r &= A_\text{eff} P_D \\
&= A_\text{eff} \cdot \frac{P_t G_t}{4 \pi d^2} \\
&= \frac{\lambda^2 G_r}{4 \pi} \cdot \frac{P_t G_t}{4 \pi d^2} \\
&= P_t G_t \cdot G_r \left(\frac{\lambda}{4 \pi d}\right)^2 \\
&= \text{EIRP} \cdot G_r \left(\frac{1}{4 \pi d / \lambda}\right)^2 \\
&= \text{EIRP} \cdot G_r \frac{1}{L_{fs}}
\end{aligned}
$$

- $P_r$: 수신 전력 [dBm]
- $P_t$: 송신 전력 [dBm]
- $G_t$: 송신 안테나 이득 [dBi]
- $G_r$: 수신 안테나 이득 [dBi]
- $d$: 송수신 간의 거리 [km]
- $f$: 주파수 [MHz]
- $L_{fs}$: 자유공간 손실

수신 전력 $P_r$ 은 송신측의 유효 출력인 EIRP와 수신측의 수집 능력인 $G_r$ 의 곱을 기준으로 정의된다. 하지만 전파는 자유 공간을 통과하며 에너지 분산(손실)을 겪게 되는데, EIRP와 $G_r$ 의 곱을 제외한 나머지 항을 손실에 관한 설명으로 간주하고 자유공간 손실(free space loss) $L_{fs}$ 라고 정의한다.  

$$
L_{fs} = \left(\frac{4 \pi d}{\lambda}\right)^2 = \left(\frac{4 \pi d f}{c}\right)^2
$$

dB 단위에서는 위의 관계를 다음과 같이 표현할 수 있다.

$$
\begin{aligned}
P_r \left[\text{dBm}\right] &= P_t \left[\text{dBm}\right] + G_t \left[\text{dBi}\right] + G_r \left[\text{dBi}\right] - L_{fs} \left[\text{dB}\right] \\
&= \text{EIRP} \left[\text{dBm}\right] + G_r \left[\text{dBi}\right] - L_{fs} \left[\text{dB}\right] \\
&\approx \text{EIRP} \left[\text{dBm}\right] + G_r \left[\text{dBi}\right] - (32.44 + 20 \log_{10}d + 20 \log_{10}f)
\end{aligned}
$$

\* 자유공간 손실 $L_{fs}$ 가 $32.44 + 20 \log_{10}d + 20 \log_{10}f$ 로 표현되는 이유는, $c = f \lambda$ 식으로부터 도출할 수 있다.  

$$
c = f \lambda
$$

$$
\begin{aligned}
\frac{c^2}{f^2 (4 \pi d)^2} &= \frac{(3 \cdot 10^8) ^2}{f^2 (4 \pi d)^2} \\
&= \left(\frac{(3 \cdot 10^8)}{4 \pi}\right)^2 \left(\frac{1}{f}\right)^2 \left(\frac{1}{d}\right)^2 \\
&= (\frac{3}{40 \pi})^2 (\frac{10^6}{f})^2 (\frac{10^3}{d})^2
\end{aligned}
$$
