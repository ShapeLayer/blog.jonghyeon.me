---
layout: post
title: RF 전송 시스템
date: 2026-04-18
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_


![](/static/posts/2026-04-18-comm-radio-frequency-system//rf-system-overview.png)  

RF(Radio Frequency) 전송 시스템은 무선 통신에서 신호를 전송하는 데 사용되는 시스템이다. 시스템은 기본적으로 안테나, 증폭기, 필터, 믹서, 오실레이터 등으로 구성된다. 이 시스템은 다양한 주파수 대역에서 작동하며, 각 대역은 특정한 용도와 특성을 가지고 있다.  

## 안테나

![](/static/posts/2026-04-18-comm-radio-frequency-system//dipole-monopole.png)  

안테나는 보통 파장의 1/2 또는 1/4 길이로 설계된다. 역으로, 안테나를 짧게 설계하고자 한다면 높은 주파수의 전파를 통신에 이용한다.  

<br />

사람의 음성을 3000Hz로 가정할 때, 음성을 멀리서 알아듣기 위한 안테나의 길이는 50km로 계산할 수 있다.  

$$
\lambda = \frac{3 \times 10^8 \text{ m/s}}{3000 \text{ Hz}} = 100 \text{ km}
$$

$$
\lambda/2 = 50 \text{ km}
$$

비슷하게, 셀룰러 휴대폰이 사용하는 900MHz 대역에서 안테나의 길이는 16.7cm로, 1.8GHz 대역을 사용하는 PCS에 대응하는 안테나의 길이는 8.3cm로 계산할 수 있다.  

$$
\lambda_\text{900MHz} = \frac{3 \times 10^8 \text{ m/s}}{900 \times 10^6 \text{ Hz}} = 0.33 \text{ m}
$$

$$
\lambda_\text{1.8GHz} = \frac{3 \times 10^8 \text{ m/s}}{1.8 \times 10^9 \text{ Hz}} = 0.17 \text{ m}
$$

$$
\lambda/2_\text{900MHz} = 0.17 \text{ m}
$$

$$
\lambda/2_\text{1.8GHz} = 0.08 \text{ m}
$$

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//dipole-graph.png)  

파장의 1/2 길이인 안테나는 반파장 다이폴 안테나(Half-wave Dipole Antenna)라고한다. 에너지를 가장 효율적으로 전파로 바꾸어 낼 수 있다.   

$\lambda/2$ 다이폴 안테나에 교류 신호가 인가되면 전압과 전류는 위 사진과 같이 분포된다. 안테나의 양 끝단은 전자가 더 이상 이동할 수 없으므로, 전류가 0, 전압이 최대가 된다. 반대로 안테나의 중앙은 전류가 최대가 된다. 전류가 최대일 때 자기장이 가장 강하게 형성되어, 전파가 가장 잘 방사된다.  

<br />

파장이 1/4 길이인 안테나는 모노폴 안테나(Monopole Antenna)라고한다. 넓은 접지면(Ground Surface) 위에 $\lambda/4$ 길이의 안테나를 세우면, 땅 아래에 거울에 비친 것처럼 가상의 $\lambda/4$ 길이의 안테나가 있는 것과 같은 효과가 발생한다.  

이상적으로 모노폴 안테나가 다이폴 안테나보다 게인이 높다고 판단된다. 다이폴 안테나는 허공에 떠서 위 아래 360도의 구형으로 에너지를 방사하지만, 모노폴 안테나는 접지면이 아래쪽으로 가는 전파를 막고 위로 반사하기 때문이다.  

## 안테나의 종류

안테나는 크게 무지향성 안테나와 지향성 안테나로 나뉜다. 무지향성 안테나는 모든 방향, 수평면 기준 360도로 균일하게 전파를 방사한다. 반면 지향성 안테나는 특정 방향으로 전파를 집중적으로 방사한다.  

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//antenna-vert.jpeg)  
_수직 안테나의 모습과 방사 패턴_  

수직 안테나인 Whip 안테나, 해리컬 안테나 등은 무지향성 안테나의 대표 사례이다. 이들 안테나는 코일을 사용하여 물리적인 길이를 전기적으로 조절한다. 이렇게 단축, 혹은 연장하여 최적의 송수신 상태를 만들 수 있다.  

주로 휴대용 무전기, 초단파 통신, 일반 상업 방송용 송신 안테나 등에 사용한다.  

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//antenna-gp.jpeg)  
_G.P 안테나의 모습과 방사 패턴_  

G.P 안테나(Ground Plane Antenna)는 수직 안테나의 일종이나, 수직 안테나보다 더 높은 위치에 설치할 때 사용된다. 안테나 하단에 지향성을 보완하거나 접지 효과를 주기 위해 수평으로 뻗은 금속판을 설치한다.  

주로 단파 통신에 사용된다.  

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//antenna-8.png)  
_8자 지향성 안테나의 모습과 방사 패턴_

지향성 안테나의 대표 사례로는 8자 지향성, 단일 지향성 안테나 등이 있다. 8자 지향성 안테나는 보통 낮은 주파수에서, 군용, 단파 통신용으로 사용된다.  

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//antenna-yagi-uda.png)  

야기-우다 안테나(Yagi-Uda Antenna)는 단일 지향성 안테나의 대표 사례이다. 1926년 일본의 야기 히데키(Yagi Hideki)와 우다 쇼지(Uda Shoji)가 개발한 안테나로, 높은 이득과 좁은 빔폭을 제공한다. 주로 텔레비전 방송 수신, 무선 통신, 레이더 시스템 등에 사용된다.  

<br />

![](/static/posts/2026-04-18-comm-radio-frequency-system//antenna-parabolic.png)

파라볼라 안테나(Parabolic Antenna)는 매우 높은 이득과 좁은 빔폭을 제공하는 지향성 안테나의 한 종류이다. 접시 모양의 반사판을 사용해, 반사면이 포물선 형태로 형성된다. 이러한 반사면 구성으로, 송신된 신호가 반사면에서 집중되어 수신기로 향하게 된다. 주로 위성 통신, 라디오 망원경, 레이더 시스템 등에 사용된다.  

## 이동통신에서의 기지국 안테나

![](/static/posts/2026-04-18-comm-radio-frequency-system//sector-rf-propagation.jpeg)  
_120도로 나눈 섹터_

통화량이 많은 대도시 지역에서 사용하는 섹터 기지국은 120도의 지향성 안테나를 사용한다. 일반적으로 섹터 당 송신 안테나 1개, 수신 안테나 2개로 구성된다.  

이 구조에서는 동일한 섹터 안에 있는 모든 사용자에게 동일한 신호가 전달되어, 사용자가 많아지면 효율이 떨어지고 간섭이 발생한다.  

최근에는 Massive MIMO 방법을 사용하는데, 위와 같이 120도의 섹터로 나누어 전파를 넓게 뿌리는 것이 아니라, 수만 개의 안테나 소재를 사용해 개별 사용자에게 각각 다른 신호를 보내는 방법이다. 이렇게 하면 간섭이 줄어들고, 효율이 높아진다. (더 알아보기: [Samsung Newsroom "Samsung Shares Massive MIMO Roadmap in New Whitepaper"](https://news.samsung.com/global/samsung-shares-massive-mimo-roadmap-in-new-whitepaper))  

## 안테나 이득

안테나 이득은 안테나의 효율과 방향성에 의해 결정된다. 방향성 $d$ 는 안테나 이득 $G_t$로 고려하고, 안테나 효율 $e$ 는 송신 전력 $P_t$로 고려했을 때, 안테나 이득 $g$ 는 이 둘의 곱으로 계산한다.  

$$
g = d \times e
$$

$$
G = 10 \log{e} + D (\text{[dB]})
$$

<br />

안테나의 효율은 안테나로 공급된 전력과 방사된 전력의 비율로 표현된다. 공급 전력 $P_t$, 방사 전력 $P_r$ 에 대해 효율 $e$ 는 다음과 같다.  

$$
e = \frac{P_r}{P_t}
$$

만약 다이폴 안테나가 85% 효율을 가질 때, 안테나 이득을 데시벨로 표현하면 아래와 같다.  

$$
\begin{aligned}
d &= \log^{-1}\left(\frac{G - 10 \log e}{10}\right) \\
&\approx \log^{-1}\left(\frac{2.14}{10}\right) = 1.64 \\
\end{aligned}
$$

$$
g = d \times e = 1.64 \times 0.85 = 1.40
$$

$$
G \text{[dBi]} = 10 \log g = 10 \log{1.40} \approx 1.43 \text{ dBi}
$$

<br />

지향성 안테나로 수신한 전력이 $80\mu\text{W}$, 등방형 안테나로 수신한 전력이 $20\mu\text{W}$ 라고 가정한다. 이 때 다이폴 안테나의 게인과 안테나의 방향성을 구할 수 있다.  

$$
G \text{[dBi]} = 10 \log{e} + D \text{[dB]}
$$

$$
\begin{aligned}
G_r &= 10 \log{\frac{P_\text{R1}}{P_\text{R2}}} \\
&= 10 \log{\frac{80 \mu\text{W}}{20 \mu\text{W}}} = 6 \text{ dB}
\end{aligned}
$$

$$
\begin{aligned}
D &= G_r - 10 \log{e} \\
&= 6 \text{ dB} - 10 \log{0.85} \approx 6.7 \text{ dB}
\end{aligned}
$$

## 전후방비와 반치각

![](/static/posts/2026-04-18-comm-radio-frequency-system//Sidelobes_en.jpeg)  
[_source: wikipedia_](https://en.wikipedia.org/wiki/Front-to-back_ratio)  

안테나가 단일 지향 특성일 때, 전계 강도(major lobe)의 최대치와 후방의 부계 강도(minor lobe)의 최대치의 비율을 전후방비(Front-to-Back Ratio)라고 한다. 지향성 안테나는 전후방비가 클 수록 좋은 것으로 판단한다.  

<br />

Major lobe의 최대 방사 방향에 대해, 전력값이 반으로 떨어지는(-3dB) 지점에서의 각도를 반치각(Half-Power Beamwidth)이라고 한다.  

반치각은 안테나 지향성의 정밀도를 나타내는 중요한 지표로, 서비스 영역을 결정하는 중요한 요인이다. 반치각이 작을수록 안테나의 지향성이 높다고 판단할 수 있고, 인접 안테나로부터의 간섭의 영향을 줄이는 데 도움이 된다.  

## 예시 계산

![](/static/posts/2026-04-18-comm-radio-frequency-system//major-lobe-beamwidth.jpeg)  

안테나 이득이 $G = 13.95 \text{dBi} = 11.8 \text{dBd}$ 인 안테나의 전후방비가 $15 \text{dB}$ 일 때, Major lobe beamwidth 는 $344^\circ$ ~ $16^\circ$ (= $-16^\circ$ ~ $16^\circ$), $32^\circ$ 를 가진다.  

<br />

[등방형 안테나에 대한 EIRP는 $P_{EIRP} = P_t + G$ 로, ERP는 반파장 다이폴 안테나 이득과 전송 전력의 곱](/posts/2026-04-12-comm-propagation-in-free-space/)으로 정의되었다.  

만약 송신단의 ERP가 주어진 방향에서 17W로 확인된다면, dBm 단위의 EIRP는 다음과 같이 계산할 수 있다.  

$$
\begin{aligned}
\text{ERP [dBm]} &= 10 \log\frac{\text{ERP}}{1 \text{mW}} \\
&= 10 \log(17 \times 10^3) \approx 42.3 \text{ dBm} \\
\end{aligned}
$$

$$
\begin{aligned}
\text{EIRP [dBm]} &= \text{ERP [dBm]} + 2.15 \text{ dB} \\
&= 42.3 \text{ dBm} + 2.15 \text{ dB} = 44.45 \text{ dBm}
\end{aligned}
$$

## 편파, 극성

![](/static/posts/2026-04-18-comm-radio-frequency-system/polarization.png)

안테나의 지향성과 관련하여, 전기장 벡터의 지향성을 나타내는 전기량으로, 전기장은 마치 극성과 비슷한 특성을 갖는데, 이것을 편파(polarization)라고 한다. 안테나는 각자 고유의 극성 특성을 가지고 있다. 송수신 안테나끼리 극성 방향을 맞추지 않으면, 신호가 제대로 전달되지 않아 통신 품질이 저하될 수 있다.  

![](/static/posts/2026-04-18-comm-radio-frequency-system/vert-polarization.jpeg)  
_송신 안테나와 수신 안테나가 서로 90도로 엇갈린(직교하는) 선형 편파 관계에서는 이론적으로 신호를 전혀 받을 수 없어 수신 전력이 0이 될 수 있다._  
