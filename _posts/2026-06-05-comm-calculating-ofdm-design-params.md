---
layout: post
title: OFDM 시스템 설계 파라미터 계산
date: 2026-06-05
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

OFDM 시스템을 구성하는 주요한 파라미터 몇 개를 알고 있다면, 이 시스템의 스펙을 확인할 수 있다.  

## 사례 \#1

- FFT 크기 $N = 2048$
- 서브캐리어 간격(SCS) $\Delta f = 15$ kHz
- CP 길이 $L_{CP} = 144$ 샘플

<br />

이 사례에서 useful OFDM 심볼의 주기, 주기성을 갖는 신호의 주기는 subcarrier 간격에서 계산해낼 수 있다.  

$$
T_u = \frac{1}{\Delta f} = \frac{1}{15 \text{ kHz}} \approx 66.67 \text{ μs}
$$

<br />

ISI를 견딜 수 있는 시스템을 설계하기 위해서, CP 기간을 길게 설정해야 하는지 시스템 설계 과정 중에 결정해야 한다. 설정할만한 최소한의 CP 길이 $L_{CP}$, 혹은 최대 delay spread는 샘플 주기 $T_s$ 를 사용한 계산으로 구할 수 있다.  

$$
T_s = T_u \times \frac{1}{N} = \frac{66.67 \text{ μs}}{2048} \approx 32.55 \text{ ns}
$$

$$
\begin{aligned}
T_{CP} &= T_s \times L_{CP} \\
&= T_u \times \frac{1}{N} \times L_{CP} \\
&= \frac{L_{CP}}{N \Delta f} \\
&= \frac{144}{2048 \times 15 \text{ kHz}} \approx 4.69 \text{ μs}
\end{aligned}
$$

<br />

이때 CP에 의해 발생하는 오버헤드는 전체 OFDM 심볼 기간에서 CP가 차지하는 비율로 계산한다.  

$$
\text{CP overhead} = \frac{T_{CP}}{T_u + T_{CP}} \approx 6.59 \%
$$

## 사례 \#2

- 서브캐리어 간격 $\Delta f = 15$ kHz
- 최대 delay spread $T_{CP} = 4.7$ μs
- CP 길이 $L_{CP} = 144$ 샘플

<br />

FFT 크기 $N = 256$ 일 때, CP 오버헤드는 다음의 과정을 거쳐 계산할 수 있다.

$$
T_u = \frac{1}{\Delta f} = \frac{1}{15 \text{ kHz}} \approx 66.67 \text{ μs}
$$

$$
T_s = T_u \times \frac{1}{N} = \frac{66.67 \text{ μs}}{256} \approx 260.42 \text{ ns}
$$

$$
T_{CP} = T_s \times L_{CP} = 260.42 \text{ ns} \times 144 \approx 37.5 \text{ μs}
$$

$$
\text{CP overhead} = \frac{T_{CP}}{T_u + T_{CP}} \approx 36.36 \%
$$

## 사례 \#3

- 대역폭 20 MHz
- 가드밴드 2 MHz
- 서브캐리어 간격 $\Delta f = 15$ kHz

<br />

Effective 대역폭은 가드밴드를 제외한 18 MHz이다. 이 대역폭에서 사용할 수 있는 서브캐리어의 개수는 다음과 같이 계산할 수 있다.

$$
N = \frac{B_{eff}}{\Delta f} = \frac{18 \text{ MHz}}{15 \text{ kHz}} = 1200
$$

만약 이 시스템이 LTE 시스템이라면 1RB(Resource Block) 당 12개의 서브캐리어가 할당되므로, 이 시스템에서 할당할 수 있는 RB의 개수는 100개이다.

<br />

FFT는 2의 거듭제곱에 대해서 효율적으로 계산할 수 있으므로, 이 시스템에서의 FFT 크기는 2048로 설정할 수 있다.  

$$
N_{FFT} = 2^{\lceil \log_2 N \rceil} = 2^{\lceil \log_2 1200 \rceil} = 2048
$$

1200개의 서브캐리어를 2048 크기의 FFT에 매핑하고, 남은 848개 항목에 대해서 제로 패딩하는 방법 등으로 시스템을 설계할 수 있다.  

## 사례 \#4

- FFT 크기 $N = 2048$
- QPSK 변조 사용(심볼 에너지 $E_s = 1$)

<br />

CP-OFDM에서 최악의 PAPR은 FFT에 투입되는 $N$ 개의 심볼이 모두 같은 위상을 가지는 경우에 발생할 수 있다. 2048개 심볼이 모두 피크이고, 평균이 1인 경우, PAPR은 다음과 같이 계산할 수 있다.

$$
10 \log_{10} \left( \frac{N}{1} \right) = 10 \log_{10} N \approx 33.11 \text{ dB}
$$

<br />

PAPR의 하한 구하기

DFT-s-OFDM의 송신 신호 시간 샘플 $x_n$ 은 $M$ 개의 IDFT와 $N$ 개의 DFT의 결합으로 나타난다. Parseval 정리에 의해 주파수 영역에서 제로 패딩을 하더라도, 시간 영역에서 평균 전력은 투입된 QPSK 심볼의 평균 전력 $E_s$ 와 같도록 정규화된다. QPSK의 모든 심볼은 크기 1로 일정하므로, 다음이 성립한다.  

$$
\mathbb{E}[|x_n|^2] = E_s = 1
$$

PAPR이 최소가 되려면 시간 영역 신호에서 최대 피크 전력 $\max(\vert x_n \vert^2)$ 이 가장 낮아지는 조건을 찾아야 한다. $N = M$ 이고 모든 DFT 입력 심볼이 같은 위상을 가지는 경우, 시간 영역의 모든 샘플 크기는 $\vert x_n \vert = 1$ 으로 일정해질 수 있다.

$$
\max(\vert x_n \vert^2) = 1
$$

PAPR은 최대 전력과 평균 전력의 비율이므로, $\mathbb{E}[|x_n|^2] / \max(\vert x_n \vert^2)$ 이다. 따라서 $1 / 1 = 1$ 이므로, PAPR의 하한은 1, 즉 0 dB이다.

<br />

PAPR의 상한 구하기

DFT-s-OFDM에서 DFT point $M$에 대해서 $N=M$ 일 때, 2048개 만큼 똑같이 Pivot하고 FFT한다. 따라서 PAPR은 다음과 같이 계산할 수 있다.

$$
N = M \Rightarrow P_{t_1} = P_{t_2} = P_{t_3} = \cdots = P_{t_N}
$$

만약 $N > M$ 이라면, $N - M$ 의 전력이 손실된다. 실제로 전력차이는 존재하므로, $33.11 \text{ dB} > \text{PAPR} > 0 \text{ dB}$ 이다.
