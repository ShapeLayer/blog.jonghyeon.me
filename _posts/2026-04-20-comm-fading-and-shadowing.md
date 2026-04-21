---
layout: post
title: 페이딩(Fading)과 섀도잉(Shadowing)
date: 2026-04-20
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

_무선 통신에서의 채널 특성_

채널 특성은 무선 통신에서 전파가 전파되는 경로에 따라 수신 신호 강도가 어떻게 변화하는지 설명하는 개념들을 일컫는다. 이들 특성을 이해하고 현실에 적절히 적용함으로써, 통신 시스템을 설계하고 운용할 수 있다.  

## 페이딩(Fading)

페이딩은 어떠한 채널이 겪는 신호 강도의 변화를 의미한다. 구체적으로는 수신된 전파의 세기가, Tx와 Rx 사이의 채널 변동에 따라, 변동하는 현상이다. 페이딩은 크게 Large-scale fading과 Small-scale fading으로 나뉜다.  

<br />

Large-scale fading 은 초 단위에 걸쳐 느리게 변화하는 페이딩이다. 주로 경로 손실(pathloss)과 그림자 효과(shadowing)에 의해 발생한다. 경로 손실은 전파가 거리를 두고 전파될 때 신호 세기가 감소하는 현상이며, 그림자 효과는 건물이나 나무와 같은 장애물에 의해 신호가 차단되거나 약해지는 현상이다.  

### Log-distance Fading 모델

수신한 신호의 세기는 로그 스케일의 거리에 따라 감소하는 경향이 있다. 자유 공간에서의 손실 모델은 평가 위치 $d$, 기준 위치 $d_0$ 에 대해서 아래와 같이 정의된다.  

$$
\begin{aligned}
P_r &= \frac{P_t \cdot G_t \cdot G_r}{\left(\frac{4 \pi d}{\lambda}\right)^2} \\
\Rightarrow P_r(d) &= P_r (d_0) \left(\frac{d_0}{d}\right)^2
\end{aligned}
$$

이 모델에서 평균 경로손실 $\bar{PL}(d)$ 는 다음과 같이 표현된다. $n$ 은 경로 손실 지수(path loss exponent)로, 환경에 따라 다르게 설정된다.  

$$
\bar{PL}(d)\text{[dB]} = \bar{PL}(d_0) \text{[dB]} + 10 \log_{10} \left(\frac{d}{d_0}\right)^n
$$

| 환경 | 경로 손실 지수 $n$ |
| :-: | :-: |
| 자유 공간<br />Free Space | $2$ |
| 도시 지역의 셀룰러 전파<br />Urban Area Cellular Radio | $2.7$ ~ $3.5$ |
| 장애물이 많은 도시 지역의 셀룰러 전파<br />Shadowed Urban Area Cellular Radio | $3$ ~ $5$ |
| 빌딩 안에서의 목시선 전파<br />In building Line-of-Sight | $1.6$ ~ $1.8$ <sup>1</sup> |
| 장애물이 많은 빌딩 안에서의 전파<br />Obstructed in Buildings | $4$ ~ $6$ |
| 장애물이 많은 공장에서의 전파<br />Obstructed in Factories | $2$ ~ $3$ |

\*1 : 반사파의 위상이 잘 맞으면 이 경우와 같이 전파가 보강되기도 한다.  

## 그림자 효과(Shadowing)

그림자 효과는 건물이나 나무와 같은 장애물에 의해 신호가 차단되거나 약해지는 현상이다. 이 효과는 일반적으로 로그 정규 분포(log-normal distribution)로 모델링된다.  

### Log-normal Shadowing 모델

![](/static/posts/2026-04-20-comm-fading-and-shadowing/log-normal-shadowing-model-graph.png)  
_Log-normal Shadowing 모델에서의 Shadowing Model은 평균이 $0$ 이고 정규 분포를 따르는 모습을 보인다._

신호가 이동할 때, 건물이나 산과 같은 장애물에 가로막혀 발생하는 신호 세기가 변화하게 된다. Log-normal Shadowing 모델에서는 신호 감쇠량 $PL$ 이 평균이 $0$ 이고 분산이 $\sigma^2$ 인 가우시안 정규분포를 따르는 랜덤 변수라고 가정한다.  

$$
X_\sigma \sim \mathcal{N}(0, \sigma^2)
$$

$$
\begin{aligned}
PL \text{[dB]} &= \text{Path Loss \text{[dB]}} + X_\sigma \\
&= \bar{PL}(d_0) \text{[dB]} + X_\sigma \\

\end{aligned}
$$

랜덤 변수 $X_\sigma$ 는 그림자 효과로 인한 신호 감쇠량의 변동을 나타낸다. 장애물의 유무는 확률적인 요소로 간주되었기 때문에, 가우시안 정규분포를 따르는 랜덤 변수로 설정되었다.  

$$
\begin{aligned}
f_Y(y) &= \frac{1}{y \sigma \sqrt{2 \pi}} \exp\left(-\frac{(\ln y - \mu)^2}{2 \sigma^2}\right) \\
&= \frac{1}{y \sigma \sqrt{2 \pi}} \exp\left(-\frac{(\ln y)^2}{2 \sigma^2}\right)
\end{aligned}
$$
_로그 정규 분포의 확률 밀도 함수_

$$
\begin{aligned}
f_X(x) &= \frac{1}{\sigma \sqrt{2 \pi}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \\
&= \frac{1}{\sigma \sqrt{2 \pi}} \exp\left(-\frac{x^2}{2 \sigma^2}\right)
\end{aligned}
$$
_정규 분포의 확률 밀도 함수_

<br />

$$
X = \ln Y \Leftrightarrow Y = \exp(X)
$$

$$
\frac{dy}{dx} = \exp(X) = Y
$$

$$
\begin{aligned}
&f_X(x)dx = f_Y(y)dy \\
\Leftrightarrow &f_X(x) = f_Y(y) \frac{dy}{dx} \\
\end{aligned}
$$

$$
\begin{aligned}
f_X(x) &= f_Y(y) \frac{dy}{dx} \\
&= \frac{1}{e^x \sigma \sqrt{2 \pi}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \cdot e^x \\
&= \frac{1}{\sigma \sqrt{2 \pi}} \exp\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right)
\end{aligned}
$$

## 오쿠무라 모델(Okumura Model)

오쿠무라 모델은 도쿄에서 실제로 측정한 신호 강도에 기반해 만든 손실 모델이다. 이 모델은 지형적 특성, Tx와 Rx의 높이와 주파수 등을 고려하여 표현되었다.  

Tx, Rx 안테나의 높이가 변경되는 것과 같은 환경 변화는 기본 모델에서 Compensation factor를 조정하여 표현할 수 있다.  

![](/static/posts/2026-04-20-comm-fading-and-shadowing/okumura-model-variations.jpeg)  

$$
\begin{aligned}
\text{dB} = 20 \log_{10} \frac{h_1}{200} \quad (h_1 > 10 \text{m}) \\
\text{dB} = 10 \log_{10} \frac{h_2}{3} \quad (h_2 > 3 \text{m})
\end{aligned}
$$

## 하타 모델(Hata Model)

오쿠무라 모델은 실제 측정 데이터를 근거한 그래프 형태의 경로 손실 예측 모델이기 때문에, 수치 계산이 어려었다. 하타 모델은 오쿠무라 모델이 수치 해석이 가능하도록 표현한 모델이다.  

$$
L_p \text{[dB]} = 69.55 + 26.16 \log_{10} f_c - 13.82 \log_{10} h_t - a(h_r) + (44.9 - 6.55 \log_{10} h_t) \log_{10} d
$$

_도시 지역(urban)에서의 하타 모델_

- $f_c$: 중심 주파수 [MHz]
- $d$: 송수신 간의 거리 [km]
- $h_t$: 송신 안테나 높이 [m]
- $h_r$: 수신 안테나 높이 [m]
- $a(h_r)$: 수신 안테나 높이에 따른 보정 계수

<br />

$$
\begin{aligned}
L_p \text{[dB]} &= L_p(\text{urban}) - 2 \Big[ \log_{10} \left(\frac{f_c}{28}\right) \Big]^2 - 5.4
\end{aligned}
$$

_교외 지역(suburban)에서의 하타 모델_

<br />

$$
\begin{aligned}
L_p \text{[dB]} &= L_p(\text{urban}) - 4.78 \log_{10}(f_c)^2 - 18.33 \log_{10} f_c + 40.94
\end{aligned}
$$

_개방 지역(open)에서의 하타 모델_  

<br />

도심지에서 신호의 전파에 방해되는 요소가 더 많고, 지역이 개방적일수록 방해 요소가 적기 때문에, 모델링된 손실 값이 점차 감소하는 것을 확인할 수 있다.  

보정 계수 $a(h_r)$ (Compensation Factor)는 수신 안테나 높이와 주파수에 따라 달라진다.  

<style>
.center-aligned-table {
  margin-left: auto;
  margin-right: auto;
}
.center-aligned-table th, .center-aligned-table td {
  text-align: center;
}
</style>

<table class="center-aligned-table">
  <thead>
    <tr>
      <th>지역</th>
      <th>$f_c$ [MHz]</th>
      <th>$a(h_r)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">도심지(City)</td>
      <td>$f_c \leq 200$</td>
      <td>$a(h_r) = 8.29 \left(\log_{10} (1.54 h_r)\right)^2 - 1.1$</td>
    </tr>
    <tr>
      <td>$f_c > 200$</td>
      <td>$a(h_r) = 3.2 \left(\log_{10} (11.75 h_r)\right)^2 - 4.97$</td>
    </tr>
    <tr>
      <td colspan="2">마을(Town)</td>
      <td>$a(h_r) = (1.11 \log_{10} f_c - 0.7)h_r - (1.56 \log_{10} f_c - 0.8)$</td>
    </tr>
  </tbody>
</table>

## 실사례에서의 손실 모델 정의와 사용

![](/static/posts/2026-04-20-comm-fading-and-shadowing/3gpp-tr-38.901-pathloss-table.png)  
_3GPP TR 38.901에서 제안된 손실 모델의 구체적인 사례_  

![](/static/posts/2026-04-20-comm-fading-and-shadowing/3gpp-tr-36.777-pathloss-table.png)  
_무인 항공기의 통신 시나리오를 가정하여 제안된 3GPP TR 36.777에서의 손실 모델 사례_  

실제로 통신 시스템을 설계할 때, 이러한 손실 모델들은 중요한 역할을 한다. 다양한 주체가 이들 모델을 정의하여 3GPP에 제안하게 되는데, 3GPP에서는 제출된 모델들을 검증하여 표준화한다.  

## Small-scale fading

![](/static/posts/2026-04-20-comm-fading-and-shadowing/var-scale-fading-graph.png)

Small-scale fading은 수 밀리초 단위로 빠르게 변화하는 페이딩이다. 주로 다양한 요인에 부딪혀 반사되어 발생하는 다중 경로(multipath)에 의해 보강간섭, 상쇄간섭이 발생한다.  

신호 그래프 상에서 매우 빠르고 작은 규모로 흔들리는 형태로 나타나는데, 특정한 주파수에 따라 변화하거나(Frequency-selective fading) 시간의 흐름에 따라 변화하는(Time-selective fading) 형태로 나타날 수 있다.  

![](/static/posts/2026-04-20-comm-fading-and-shadowing/multipath-fading.png)  

### Rayleigh fading

송신기와 수신기 사이에 목시선(LOS)이 존재하지 않는 경우(= NLOS; No Line of Sight), 직접 신호보다 반사된 신호가 지배적인 역할을 하게 된다. 주로 건물이 빽빽한 도심이나 실내처럼 장애물이 많은 환경에서 발생한다.  

이 때 채널 이득 $g$ 는 Rayleigh 분포를 따르는 랜덤 변수로 모델링된다.  

$$
\begin{aligned}
g &\sim \text{Rayleigh}(\sigma) \\
g^2 &\sim \exp(\lambda)
\end{aligned}
$$

$$
f_h(h) = \frac{1}{\bar{h}} \exp\left(-\frac{h}{\bar{h}}\right)
$$

$h$ 는 채널 이득의 제곱, $\bar{h}$ 는 채널 이득의 평균값이다. Rayleigh fading에서는 채널 이득이 평균값보다 크게 보강되는 경우가 드물기 때문에, 신호가 약해지는 경우가 더 빈번하게 발생한다.

### Rician fading

직선 신호가 반사되는 신호보다 강해서, 직선 신호가 지배적인 경우에는 Rician Fading으로 파악할 수 있다. 채널 Fading의 이득은 비중심 카이제곱 분포(non-central chi-square distribution)를 따르는 랜덤 변수로 모델링된다.  

$\rho$ 는 직선 신호의 진폭, $\sigma$ 는 반사된 신호의 진폭의 표준편차이다. Rician factor $K$ 는 직선 신호가 반사된 신호보다 얼마나 강한지를 나타내는 지표로, $K$ 가 클수록 직선 신호가 더 지배적임을 의미한다.

\* Rician factor $K$ 는 직선 신호의 세기와 반사된 신호의 세기의 비율로 정의된다. $\rho$ 는 직선 신호의 진폭이므로, 직선 신호의 세기는 $\rho^2$ 로 표현된다. 반사된 신호의 세기는 반사된 신호의 진폭의 표준편차인 $\sigma$ 의 제곱인 $2 \sigma^2$ 로 표현된다. 따라서 Rician factor $K$ 는 다음과 같이 정의된다.

$$
K = \frac{\rho^2}{2 \sigma^2} = \frac{\text{LOS Component}}{\text{NLOS Component}}
$$

$$
f_h(h) = \frac{1 + K}{\bar{h}} \exp\left(-K - \frac{(1 + K)h}{\bar{h}}\right) I_0\left(2 \sqrt{\frac{K(1 + K)h}{\bar{h}}}\right)
$$

만약 $K$ 가 $0$ 이라면, LOS 신호가 존재하지 않는 상황이므로, Rayleigh fading과 동일한 모델이 된다.  
