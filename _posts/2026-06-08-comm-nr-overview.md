---
layout: post
title: NR의 개요
date: 2026-06-08
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

![](/static/posts/2026-06-08-comm-nr-overview/comm-model.png)

_좌측의 작은 도형이 LTE의 목표, 큰 도형이 NR의 목표_  

## NR의 도입

| Feature | LTE | NR |
| :-: | :-: | :-: |
| Waveform | DL: CP-OFDM<br />UL: DFT-s-OFDM | DL: CP-OFDM<br />UL: CP-OFDM or DFT-s-OFDM |
| Modulation | QPSK, <br /> 16QAM, <br />  64QAM | pi/2-BPSK<sup>1bit/sym</sup>, <br /> QPSK<sup>2bit/sym</sup>, <br /> 16QAM<sup>4bit/sym</sup>, <br /> 64QAM<sup>6bit/sym</sup>, <br /> 256QAM<sup>8bit/sym</sup> |
| MIMO Max Layers | 4(DL) | 16(DL), 8(UL) |

MIMO Layer는 MIMO 시스템에서 동시에 전송할 수 있는 데이터 스트림의 개수이다. DFT-s-OFDM은 1랭크 MIMO 시스템이라고 하는데, 이 때의 랭크가 1개의 UE가 가질 수 있는 MIMO Layer의 개수를 의미한다.  

## Fixed Numerology

LTE에서는 Subcarrier Spacing이 15kHz로 고정되어있었지만, NR에서는 $15 \times 2^\mu \text{kHz}$ 로 정의된 여러 개의 Subcarrier Spacing을 지원한다.  

FR 1 밴드에서는 $\mu = 0, 1, 2$ (15kHz, 30kHz, 60kHz)를, FR 2 밴드에서는 $\mu = 2, 3, 4$ (60kHz, 120kHz, 240kHz)를 사용한다.  

<br />

![](/static/posts/2026-06-08-comm-nr-overview/rb-tables-in-freq.png)  

저주파 대역인 FR 1 밴드에서 $\mu = 2$ 라면 Extended Cyclic Prefix를 사용하는 것이 권장되는데, SCS가 증가함에 따라 심볼 기간이 짧아져, CP가 짧아지는 상황에서 ISI의 영향이 커지기 때문이다.  

mmWave 등이 사용하는 고주파 대역, FR 2 밴드에서는 경로 손실이 커서 다중경로로부터 유발되는 ISI의 영향은 상대적으로 작아, Extended Cyclic Prefix는 사용되지 않는다. 

## Frame Structure

1개의 라디오 프레임은 10개의 서브프레임으로 나누어지는데, 각 서브프레임은 고정된 기간 1ms를 갖는다. 서브프레임은 numerology $\mu$ 에 따라 10, 20, 40, 80, 160개의 슬롯으로 나누어질 수 있다.  

나누어진 1개 슬롯은 일반적으로는 14개의 OFDM 심볼로 구성된다. 1 OFDM 심볼은 $1/(15 \times 2^\mu) \text{ ms}$ 의 유효 심볼과 CP로 구성된다. 심볼 길이는 $\mu$ 가 증가함에 따라 절반씩 줄어든다.  

480kHz 대역에서 FFT 기반의 Tx/Rx 구현은 4096 크기의 FFT를 사용하여, 기본 시간 유닛 $T_c$ 는 $1 / (480 \times 10^3 \times 4096) \approx 0.51 \text{ }\mu\text{s}$ 이다.  

![](/static/posts/2026-06-08-comm-nr-overview/frame-structure.png)  

### 프레임 구성 예시

#### 사례 \#1

SCS가 15kHz이고 FFT 크기가 4096인 경우, 1 OFDM 심볼의 유효 심볼 시간은 $T_u = 1/(15 \times 10^3) = 66.7 \text{ }\mu\text{s}$ 이다. 

CP가 짧은 사이즈라면 FFT 크기가 288이고 CP 길이는 $T_{CP}^S = 288 / (15 \times 10^3 \times 4096) \approx 4.7 \text{ }\mu\text{s}$ 이다. 

CP가 긴 사이즈라면 FFT 크기가 320이고 CP 길이는 $T_{CP}^L = 352 / (15 \times 10^3 \times 4096) \approx 5.7 \text{ }\mu\text{s}$ 이다.

이때 OFDM의 반 슬롯을 7개의 유효 심볼과 1개의 긴 CP, 6개의 짧은 CP로 구성하여 아래와 같이 0.5ms 길이에 근사하게 구성한다.

$$
\begin{aligned}
T_u + T_{CP}^L + 6 \times T_{CP}^S =& 7 \times 1/15 \text{ ms} \\
+& 1 \times 352/(15 \times 10^3 \times 4096) \text{ ms} \\
+& 6 \times 288/(15 \times 10^3 \times 4096) \text{ ms} \\
\approx & 0.5 \text{ ms}
\end{aligned}
$$

#### 사례 \#2: LTE의 경우

SCS가 15kHz이고 FFT 크기가 2048<sup>LTE</sup>인 경우, 1 OFDM 심볼의 유효 심볼 시간은 $T_u = 1 / 15 \text{ kHz} = 66.7 \text{ }\mu\text{s}$ 이다.

CP가 짧은 사이즈라면 $N_{CP}^S = 144$ 이고 CP 길이는 $T_{CP}^S = 144 / (15 \times 2048) \approx 4.7 \text{ }\mu\text{s}$ 이다. 

CP가 긴 사이즈라면 $N_{CP}^L = 160$이고 CP 길이는 $T_{CP}^L = 160 / (15 \times 2048) \approx 5.2 \text{ }\mu\text{s}$ 이다.  

이때 OFDM의 반 슬롯을 7개의 유효 심볼과 1개의 긴 CP, 6개의 짧은 CP로 구성하여 아래와 같이 0.5ms 길이에 근사하게 구성한다.

$$
\begin{aligned}
T_u + T_{CP}^L + 6 \times T_{CP}^S =& 7 \times 1/15 \text{ ms} \\
+& 1 \times 160/(15 \times 2048) \text{ ms} \\
+& 6 \times 144/(15 \times 2048) \text{ ms} \\
\approx & 0.5 \text{ ms}
\end{aligned}
$$

#### 사례 \#3: NR에서 SCS가 30kHz인 경우

SCS가 30kHz이고 FFT 크기가 1024인 경우, 1 OFDM 심볼의 유효 심볼 시간은 $T_u = 1 / 30 \text{ kHz} = 33.3 \text{ }\mu\text{s}$ 이다.

CP가 짧은 사이즈라면 $N_{CP}^S = 72$ 이고 CP 길이는 $T_{CP}^S = 72 / (30 \times 1024) \approx 2.34 \text{ }\mu\text{s}$ 이다. 

CP가 긴 사이즈라면 $N_{CP}^L = 80$이고 CP 길이는 $T_{CP}^L = 80 / (30 \times 1024) \approx 2.60 \text{ }\mu\text{s}$ 이다.  

이때 OFDM의 반 슬롯을 7개의 유효 심볼과 1개의 긴 CP, 6개의 짧은 CP로 구성하여 아래와 같이 0.25ms 길이에 근사하게 구성한다.

$$
\begin{aligned}
T_u + T_{CP}^L + 6 \times T_{CP}^S =& 7 \times 1/30 \text{ ms} \\
+& 1 \times 80/(30 \times 1024) \text{ ms} \\
+& 6 \times 72/(30 \times 1024) \text{ ms} \\
\approx & 0.25 \text{ ms}
\end{aligned}
$$

## 대역폭

### LTE에서의 DC 서브캐리어 회피와 NR에서의 변화

LTE에서 DC 근처의 서브캐리어는 높은 간섭, 잡음, 왜곡이 문제가 되어, 취약해져 사용을 회피했다.

RF와 아날로그 경로에서 발생하는 DC 오프셋, LO feedthrough, I/Q 불균형, 저주파(플리커) 잡음 등 여러 비이상 현상이 중심주파수 위치에서 직접적으로 스펙트럼 성분을 만들어내거나 증폭하기 때문이며, 이로 인해 해당 서브캐리어가 다른 서브캐리어보다 상대적으로 높은 간섭과 왜곡을 받기 쉽다.

NR에서는 구현 기술과 신호 처리 성능이 향상되어, DC 서브캐리어의 간섭 문제를 완화할 수 있게 되었다. 구현적으로 충분히 보상할 수 있다면 규격적으로 제한할 필요가 없어, NR에서는 DC 서브캐리어도 사용할 수 있게 되었다.

또한 LTE 기기는 대역폭의 중심이 항상 DC에 위치되도록 설계되어 있는 반면, NR 기기는 대역폭의 중심 위치가 어디에 있든 상관없이 서브캐리어가 배치될 수 있다. 이러한 유연한 배치 방식으로 인해 DC 성분의 영향을 더욱 효과적으로 분산시킬 수 있게 되었다.

### Bandwidth Part

LTE에서는 설계상 모든 디바이스(UE)가 최대 캐리어인 20MHz를 항상 처리한다고 가정하여, DC 서브캐리어 처리를 위한 문제들을 회피하고 제어 채널이 전체 대역에 퍼질 수 있었다. 

하지만 NR의 지원 대역폭이 매우 넓어, 모든 장치가 최대 대역폭을 항상 수신할 수 있다고 가정할 수 없게 되었다. 이들 대역폭을 수신하는 것은 좁은 대역폭을 수신하는 것보다 많은 전력을 요구하기 때문에, 장치 측의 부담도 더 증가한다.  

그래서 NR에서는 수신기의 대역폭을 필요에 따라 조정한다. 제어 채널을 모니터링하거나 적은 규모의 데이터 전송에는 좁은 대역폭을 사용하고, 대량의 데이터 전송에는 전체 대역폭을 개방해 사용한다.  

## 참조

- [Smart Telecom Edu "5G: Bandwidth Part"](https://5g.smarttelecomedu.com/5g-bandwidth-part/)
