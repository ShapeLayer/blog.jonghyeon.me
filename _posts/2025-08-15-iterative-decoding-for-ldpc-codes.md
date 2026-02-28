---
layout: post
title: LDPC 코드의 반복적 디코딩 방법
date: '2025-08-15'
categories: [communications]
tags: [communications, ldpc, iterative-decoding]
---

## 도입

LDPC(low-density parity-check) 코드는 반복적 디코딩(iterative decoding)으로 섀넌 한계에 가까운 성능을 달성했다.

LDPC 코드를 디코딩하는데에는 여러 알고리즘을 사용할 수 있다. 대표적으로 SP(sum-product; 합-곱, 혹은 BP; belif-propagation) 알고리즘이 최적의 성능을 보이지만, 디코딩 복잡도가 높다. 이 SP 알고리즘을 대신해, MS(min-sum; 최소합) 알고리즘과 그 변형 디코딩 알고리즘인 NMS(normalized min-sum), OMS(offset min-sum) 알고리즘 등이 SP 알고리즘의 복잡도를 낮추고, 더 다양한 개별 시스템에서 사용할 수 있도록 개발되었다.

## 합-곱 알고리즘

반복적 디코딩 알고리즘은 패러티 검사 행렬의 시각적 표현인 테너 그래프에서 묘사할 수 있다. 반복적 디코딩에서 일반적으로 비트 LLR(log-likelihood ratio; 로그 우도비)을 메시지로 사용한다. 코드워드 $x$에 잡음이 섞인 수신 벡터 $y$에 대해, $x$의 $v$번째 비트에 대한 LLR은 다음과 같이 정의된다. $\tt{Pr}(y_v \vert x_v)$는 $x_v$에서의 $y_v$로의 전이확률이다.

$$
\ell_v = \ln{ \frac{\tt{Pr}(y_v \vert x_v = 0)}{\tt{Pr}(y_v \vert x_v = 1)} }
$$

LDPC 코드 디코딩은 VN과 CN 사이의 반복적인 메시지 교환이다. 반복 과정 $i$에 대해서 VN $v$에서 CN $c$로의 메시지 교환은 VN $v$와 인접한 CN들의 이웃 집합 $\mathcal{N}(v)$, $\mathcal{N}(v)$에서 CN $c$를 제외한 집합 $\mathcal{N}(v)/c$에 대해서 다음과 같이 표현할 수 있다.

$$
\ell^{(i)}_{v \rightarrow c} = \ell_v + \sum_{c' \in \mathcal{N}(c)/v}{\ell^{(i - 1)}_{c' \rightarrow v} }
$$
역으로 CN $c$에서 VN $v$로의 메시지 교환은 CN $c$와 인접한 VN들의 이웃 집합 $\mathcal{N}(c)$, $\mathcal{N}(c)$에서 VN $v$를 제외한 집합 $\mathcal{N}(c)/v$에 대해서 다음과 같이 표현할 수 있다. 첫번째 반복 과정에서, $\ell^{0}_{c \rightarrow v}$는 0이다.
$$
\ell^{(i)}_{c \rightarrow v} = 2 \tanh^{-1} \left( \prod_{v' \in \mathcal{N}(c)\setminus v} \tanh \left( \frac{\ell^{(i)}_{v' \rightarrow c}}{2} \right) \right)
$$

$i$회의 반복 과정 이후의 코드비트 $x_v$의 LLR에 대한 soft estimation $s_v$는 다음과 같은 계산을 거쳐 $y_v$에 대한 원본 추정값 $\hat{x}_v$를 결정한다. $\text{sgn}(s_v)$는 $s_v$의 부호이다.

$$
s_v = \ell_v + \sum_{c' in \mathcal{N}(v)}{\ell^{(i)}_{c' \rightarrow v}}
$$

$$
\hat{x}_v = \frac{1 - \text{sgn} (s_v)}{2}
$$

## 최소합 알고리즘과 변형판
SP 알고리즘은 쌍곡선 탄젠트 함수와 곱셈 연산이 계속해서 수행되어야 하므로 높은 연산 복잡도를 보인다. 최소합 알고리즘은 이 수식을 근사하여 연산의 복잡도를 낮추었다.

$$
\ell^{(i)}_{c \rightarrow v} = \left( 
  \prod_{v' \in \mathcal{N}(c)\setminus v} \text{sgn} \left( 
    \ell^{(i)}_{v' \rightarrow c}
  \right)
\right) \times \min_{v' \in \mathcal{N}(c)/v}{\lvert \ell^{(i)}_{v' \rightarrow c} \rvert}
$$

하지만 근사된 수식은 SP 알고리즘과 비교하여 꽤 큰 손실이 발생하여, 이후에는 최소합 알고리즘을 변형하여 성능 손실을 개선한 디코딩 알고리즘이 더 제안되었다.

대표적으로 정규화 MS(NMS; Normalized Min-sum) 알고리즘은 MS 알고리즘 연산식에 정규화 스케일 계수 $\alpha$를 곱한다.

$$
\ell^{(i)}_{c \rightarrow v} = \alpha \times \left( 
  \prod_{v' \in \mathcal{N}(c)\setminus v} \text{sgn} \left( 
    \ell^{(i)}_{v' \rightarrow c}
  \right)
\right) \times \min_{v' \in \mathcal{N}(c)/v}{\lvert \ell^{(i)}_{v' \rightarrow c} \rvert}
$$

혹은 MS 알고리즘 연산식에 오프셋 보정항을 추가하는 방법으로 손실을 보정한 오프셋 MS(OMS; Offset min-sum) 알고리즘도 제안되었다.

$$
\ell^{(i)}_{c \rightarrow v} = \left( 
  \prod_{v' \in \mathcal{N}(c)\setminus v} \text{sgn} \left( 
    \ell^{(i)}_{v' \rightarrow c}
  \right)
\right) \times \max \left\{
  \min_{v' \in \mathcal{N}(c)/v}{\lvert \ell^{(i)}_{v' \rightarrow c} \rvert} - \beta, 0
  \right\}
$$

OMS 방법은 곱셈 연산을 피해 반복 과정의 디코더를 구현하는데 더 적합하다. NMS와 OMS는 중요 인자 $\alpha$, $\beta$가 밀도 진화(DE; density evolution)를 거쳐 모든 특정한 LDPC 코드에 대해 최적화되어야만 한다. 일반적인 LDPC 코드들에는 $\alpha = .8$, $\beta=.15$가 권장된다.

이후에 신호 진폭과 잡음 분산을 인식하는 적응적 방법이 몇 가지 제안되었지만, 이들은 계산 복잡도를 증가시켰다.

## 참고: 프로토그래프 LDPC 코드

다중간선 유형의 LDPC(MET-LDPC; Multi-edge type LDPC) 코드는 구조화된 LDPC 코드의 통합 프레임워크이다. 단일한 간선 유형만 갖는 기존 LDPC의 테너 그래프와 달리 MET-LDPC 코드는 여러가지 간선 유형을 제공한다. MET-LDPC 코드는 특정한 제약 조건 하에 최적화된 코드를 탐색할 수 있게 한다.

프로토그래프 LDPC 코드는 작은 베이스코드로 정의되는 MET-LDPC의 한 유형이다. $(N_b, K_b)$ 베이스 코드에서 $N_b$와 $N_b - k_b$는 각각 해당 베이스코드(=베이스그래프)에 대응하는 테너 그래프의 변수 노드 VN(Value Node)과 검사 노드(Check Node)이다.

$(N, K)$코드는 베이스그래프를 확장하여 생성한다. 구체적으로 우선, 베이스그래프의 $Z=N/N_b=K/K_b$개 사본을 생성한다. 이어서 동일한 간선 유형 내에서 간선들을 순열화(permuting)하여 $Z$개로 분리된 베이스그래프 사본들을 하나의 그래프로 통합한다. 이 작업을 리프팅, 생성된 그래프는 Z-lifted LDPC 코드로 불린다.  

순열(permuting) 처리는 같은 유형의 간선 다발 내에서 수행된다. 그래프의 차수와 같이, 간선과 노드의 구조적 속성은 리프팅된 코드와 베이스그래프가 동일하다. 프로토그래프 LDPC 코드의 거시적 구조는 베이스그래프를 통해 파악될 수 있다.
