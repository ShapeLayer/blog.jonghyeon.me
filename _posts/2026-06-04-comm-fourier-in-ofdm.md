---
layout: post
title: 디지털 시스템에서의 DFT까지의 과정
date: 2026-06-04
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<br />

## Continuous Time Fourier Series

주기 신호를 주파수로 표현하는 데 푸리에 급수가 활용된다.  

아래의 시간 연속적인 주기 신호 $x(t)$ 는 주기 $T$ 를 가진다. 이 신호는 무한히 많은 주파수 성분으로 표현될 수 있다.  

$$
C_k = \frac{1}{T} \int_{0}^{T} x(t) \exp(-j 2 \pi k t / T) dt \Leftrightarrow x(t) = \sum_{k=-\infty}^{\infty} C_k \exp(j 2 \pi k t / T)
$$

$\exp(-j 2 \pi k t / T)$ 는 기본 주파수 $1/T$ 를 가지는 복소 지수 함수로, $k$ 정수배의 주파수 성분, $k/T$ 주파수 성분이다.  

$C_k$ 는 이산 주파수 신호로, $x(t)$ 와 $\exp(-j 2 \pi k t / T)$ 사이의 유사성을 나타낸다. $x(t)$ 의 $k$ 번째 주파수 성분($k/T$ 주파수 성분)의 복소 진폭인 크기와 위상을 의미한다.

## Continuous Time Fourier Transform

Continuous Time Fourier Series에서 살펴본 바ー주기 신호 $x(t)$ 를 여러 개의 주파수 성분으로 표현했다.ー와 같이 시간 도메인의 연속한 신호를 주파수 도메인으로 변환할 수 있다.  

$$
X(f) = \int_{-\infty}^{\infty} x(t) \exp(-j 2 \pi f t) dt \Leftrightarrow x(t) = \int_{-\infty}^{\infty} X(f) \exp(j 2 \pi f t) df
$$

<br />

이 변환은 시간 도메인의 연속한 신호 $x(t)$ 를 주파수 도메인의 연속한 신호 $X(f)$ 로 변환한다. $x(t)$ 의 주기가 무한히 길어질 때, 푸리에 급수는 푸리에 변환으로 수렴한다. $(T \to \infty \Rightarrow \frac{1}{T} \to 0)$  

연속 푸리에 급수에서와 같이, $\exp(-j 2 \pi f t)$ 는 기본 주파수를 가지는 복소 지수 함수로서 $f$의 주파수 성분이고, $X(f)$ 는 $C_k$ 와 유사하게, $x(t)$ 와 $\exp(-j 2 \pi f t)$ 사이의 유사성을 나타낸다.

## Discrete Time Fourier Series

디지털 시스템에서는 모든 값이 이산적이므로, 푸리에 급수와 푸리에 변환도 이산적으로 표현되어야 한다.  

길이 $N$ 의 주기성을 갖는 이산 신호 $x[n]$ 은 

$$
X[k] = \frac{1}{N} \sum_{n=0}^{N-1} x[n] \exp(-j 2 \pi k n / N) \Leftrightarrow x[n] = \sum_{k=0}^{N-1} X[k] \exp(j 2 \pi k n / N)
$$

$x[n]$ 는 길이 $N$ 의 이산 신호, $N$ 개의 주파수로 구성된 신호이다. 다시 말해 주파수 도메인으로 전환된 $X[k]$ 는 $x[n]$ 의 $k$ 번째 주파수 성분이다.

역시 $\exp(-j 2 \pi k n / N)$ 는 기본 주파수 $1/N$ 를 가지는 신호이고, $X[k]$ 는 $x[n]$ 와 $\exp(-j 2 \pi k n / N)$ 사이의 유사성을 나타낸다. $X[k]$ 는 $x[n]$ 의 $k$ 번째 주파수 성분의 크기와 위상을 나타내는 것으로 해석할 수 있다.

## Discrete Time Fourier Transform

Discrete Time Fourier Series를 이용해 이산 푸리에 변환을 정의할 수 있다.  

$$
X[k] = \frac{1}{N} \sum_{n=-\infty}^{\infty} x[n] \exp(-j 2 \pi k n / N) \Leftrightarrow \frac{1}{2T} \int_{-T}^{T} X(f) \exp(j 2 \pi f n) df
$$

$x[n]$ 은 비주기(aperiodic)의 이산 시간 신호로, $x[n]$ 의 길이가 무한히 길어질 때, 푸리에 급수는 푸리에 변환으로 수렴한다. $(N \to \infty)$  

## Discrete Fourier Transform

시간 도메인에서 비주기 신호를 찾으려고 할 때, Discrete Time Fourier Transform을 수정해 사용할 수 있다.  

$$
X[k] = \sum_{n=0}^{N-1} x[n] \exp(-j 2 \pi k n / N) \Leftrightarrow x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \exp(j 2 \pi k n / N)
$$
다.

$X[k]$ 는 시간 영역에서 유한한 길이 $N$ 을 가지는 이산 신호 $x[n]$ 을 주파수 영역의 이산 신호로 변환한 결과로, $k$ 번째 주파수 성분의 복소 진폭을 나타낸다.
