---
layout: post
title: LTE의 개요
date: 2026-06-07
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## Why LTE?

| Feature | WCDMA | LTE |
| :-- | :-: | :-: |
| Multiple access scheme | CDMA | OFDMA, SC-FDMA |
| Frequency reuse | 100% | Flexible |
| Use of MIMO anntenas | Release 7부터(거의 고려되지 않음) | Yes |
| Bandwidth | 5MHz | 1.4, 3, 5, 10, 15, 20MHz |

4세대 이동통신 이래 보이스 서비스와 데이터 서비스가 통합된 엑세스 네트워크가 되었기 때문에, 3세대 이동통신보다 높은 데이터 전송률이 요구되었다. 3세대 WCDMA에서는 다운링크 14Mbps, 업링크 5.7Mbps의 데이터 전송률을 가졌으나, 4세대에서는 다운링크 1Gbps, 업링크 50Mbps의 데이터 전송률을 달성하는 것이 목표가 되었다.  

다만 이 목표는 WCDMA로는 달성하기 어려웠는데, Chip Rate를 올려야 데이터 전송률이 오르는 WCDMA 시스템에서, 전송률을 높이면 시스템이 지나치게 복잡해지기 때문이었다.  

<br />

그래서 4세대 이동통신에서는 다운링크에 OFDMA, 업링크에 SC-FDMA(single carrier에서는 FDMA)를 채택하고, 변조 방법도 64QAM을 추가로 지원하도록 해 전송률을 확보했다. 더 전송률이 높은 변조 방법을 사용하면 오류율도 더 높아질 수 있어, 전송률이 더 높은 변조 방법이 항상 전송률을 개선하는 것은 아니다. 그래서 SNR이 낮은 상황에서 QPSK, 높은 상황에서 64QAM을 사용한다.  

| Modulation scheme | 3G | 4G |
| :-: | :-: | :-: |
| QPSK 2bit/sym | O | O |
| 16QAM 4bit/sym | O | O |
| 64QAM 6bit/sym | X | O |

## LTE의 시간-주파수 구조

LTE가 사용하는 OFDM은 시간과 주파수를 모두 자원을 갖는다.  

### 주파수 영역에서 살펴보기

OFDM subcarrier 간격(SCS)은 다운링크와 업링크 모두 15kHz로 고정되어있다. 이 간격은 크면 Symbol duration이 낮아져 저지연 통신이 가능하지만 ISI의 영향이 커져 CP를 길게 설정해 주파수 효율이 낮아질 수 있다. 반대로 간격이 작으면 Symbol duration이 길어져 ISI의 영향이 줄어들지만, 긴 심볼 기간 때문에 통신 지연이 발생한다.  

샘플링 과정에서 사용하는 FFT는 기본적으로 2048 크기의 변환을 사용한다. 샘플링 주파수 $f_s$ 는 $Delta f \times N_\text{FFT} = 15 \text{ kHz} \times 2048 = 30.72 \text{MHz}$ 이다.  

LTE의 대역폭 20MHz 채널에서는 양 옆의 보호 대역을 제외하고 실제로 데이터를 전송하는 부반송파 개수는 1200개(100 Resource Block)이다. 이 때 실제로 차지하는 주파수, 유효 대역폭(Active Bandwidth)은 $1200 \times 15 \text{kHz} = 18 \text{MHz}$ 이다.  

<br />

| Bandwidth | Resource Block | Subcarrier (DL) | Subcarrier (UL) |
| :-: | :-: | :-: | :-: |
| 1.4MHz | 6 | 73 | 72 |
| 3MHz | 15 | 181 | 180 |
| 5MHz | 25 | 301 | 300 |
| 10MHz | 50 | 601 | 600 |
| 15MHz | 75 | 901 | 900 |
| 20MHz | 100 | 1201 | 1200 |

\* 주파수는 0Hz를 기준으로 양 옆으로 대칭적으로 할당됨

기지국이 쏘고 단말이 받는 다운링크에서는 단말기의 가격과 크기를 낮추기 위해 주로 Direct Conversion (Zero-IF) 수신기를 사용한다. 이 방식은 주파수를 기저대역(Baseband)으로 바로 낮추는 과정에서, 회로 자체의 누설 전류 등으로 인해 주파수 중심(0Hz 지점)에 원치 않는 큰 직류(DC) 성분의 노이즈가 발생하게 된다. 이것을 DC offset이라고 하는데, 이 중심 주파수 성분은 오염되어 데이터로 쓸 수 없다고 판단하고, 아무 데이터도 할당하지 않는 방식으로 해결한다. 그래서 표와 같이 다운링크의 subcarrier 개수는 업링크보다 1개 더 많다.  

### 시간 영역에서 살펴보기

LTE 전송 프레임은 10ms로 구성되어있고, 각 프레임은 길이 1ms의 서브프레임 1개로 나누어진다. 이 서브프레임들은 다시 두 개의 슬롯으로 균일하게 나뉘어 0.5ms의 길이를 갖는다. 

- $T_\text{frame} = 10ms$
- $T_\text{subframe} = 1ms$
- $T_\text{slot} = 0.5ms$

이들 각 슬롯은 OFDM 심볼로 구성되어있다. Useful symbol 시간 $T_s$ 는 $T_u = 2048 \times T_s$ 로부터 정의되어 약 66.7 $\mu s$, 기본 시간 유닛 $T_s = 1/(15kHz \times 2048) = 32.55 \mu s$ 이다.

$$
\begin{aligned}
0.5 \text{ms} &= 7 \times T_u + ?? \\
&= 7 \times 66.7 \mu s + ?? = 466.9 \mu s + ??
\end{aligned}
$$

<br />

LTE에서는 두 개 종류의 Cyclic Prefix, Normal cyclic prefix와 Extended cyclic prefix를 정의해 사용한다. 이들 두 CP는 응용 시나리오가 다르다. 통신 단말이 물리적으로 고속으로 이동하는 상황에서 심볼 간 간섭이 커지게 되는데, 이 때의 ISI 문제를 해결하기 위해 CP도 증가한 Extended cyclic prefix를 사용한다.  

다만, CP가 차지하는 시간이 길어지므로 1 Slot당 들어가는 심볼 개수는 7개에서 6개로 줄어들어 데이터 전송 효율은 희생된다.  

## Resource Grid

LTE에서는 주파수 축과 시간 축으로 이루어진 자원 할당 단위를 일종의 그리드 구조로 표현한다.  

Resource Element(RE)는 무선 자원에서 최소 물리 단위로, 주파수 축의 서브캐리어 1개와 시간 축의 OFDM 심볼 1개로 구성된다.

RE들은 그룹화되어 Resource Block(RB)을 형성한다. RB는 주파수 축에서 12개의 서브캐리어와 0.5ms의 슬롯 시간으로 구성된다. 앞에서 살펴보았듯, OFDM 심볼의 길이는 CP 프로파일에 따라 바뀐다. 시간 축의 OFDM 심볼이 7개인 Normal CP에서는 84개의 RE로 구성되고, OFDM 심볼이 6개인 Extended CP에서는 72개의 RE로 구성된다.

물리적인 RB는 1슬롯(0.5ms)을 기준으로 정의되지만, 기지국이 실제로 사용자에게 자언을 배정하는 최소 스케줄링 단위는 1 서브프레임(1ms)이다. 그래서 실제로는 시간 축으로 연속된 2개의 RB가 묶인 RB Pair가 스케줄링 단위이다.  

## Duplex Schemes

업링크와 다운링크 신호를 분리해 통신하는 데 있어서, LTE는 FDD와 TDD 두 방법을 모두 사용한다.

FDD는 업링크와 다운링크가 서로 다른 주파수 대역을 공유하므로, 시분할 없이 동시 송수신이 가능하다. 하지만 주파수 자원이 업링크 다운링크로 한 쌍이 필요하다.  

TDD는 업링크와 다운링크가 같은 주파수 대역을 공유하여 주파수 자원을 절약할 수 있다. 하지만 시분할로 송수신이 이루어지므로, 업링크와 다운링크가 동시에 이루어질 수 없다.

### TDD의 시분할 과정에서의 Special Subfraem의 등장

TDD는 같은 주파수를 쓰기 때문에 기지국이 다운링크를 보내다가 업링크로 전환할 때, 스위칭 시간이 요구된다. 이 전환 시간 동안 신호가 뒤엉키지 않도록 Special Subframe이 사용된다.

$$
\text{Special Subframe} = \text{DwPTS} \Rightarrow \text{GP} \Rightarrow \text{UpPTS}
$$

Special Subframe은 세 파트로 구성된다. DwPTS는 다운링크 전송이 끝나고 업링크로 전환하기 위한 시간으로, 기지국이 다운링크를 보내다가 업링크로 전환할 때, 스위칭 시간이 요구되는데, 이 전환 시간 동안 신호가 뒤엉키지 않도록 하는 역할을 한다. GP는 Guard Period로, DwPTS와 UpPTS 사이의 간격으로, 업링크와 다운링크가 서로 간섭하지 않도록 하는 역할을 한다. UpPTS는 업링크 전송이 시작되기 전에 필요한 시간으로, 단말이 업링크 전송을 준비한다. 단말이 기지국에 망 접속을 요청하는 임의접근(RACH) 프리앰블이나 사운딩 참조 신호(SRS)를 전송한다.

![](/static/posts/2026-06-07-lte-overview/spcial-subframe.png)

그래서 Special Subframe에서는 통신 전환을 위한 준비작업은 수행되어도, 실제로 의미있는 데이터 교환은 이루어지지 않는다.  
