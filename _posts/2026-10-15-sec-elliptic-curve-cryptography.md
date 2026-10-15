---
layout: post
title: 'Elliptic Curve Cryptography'
date: '2026-10-15'
category: [security]
---

_〈컴퓨터정보보안〉 수업 노트_

<br />

Elliptic Curve는 암호 시스템은 아니다. 하지만 공개 키 암호화 시스템에서 활용 가능한 수학적 원리를 제공한다.  

이 커브를 사용하면 더 적은 계산 비트수로 다른 방법과 비슷한 수준의 보안성을 제공해, 더 효율적인 암호화가 가능하다.  

## Elliptic Curve

![](/static/posts/2026-10-15-sec-elliptic-curve-cryptography/elliptic_curve.png)  

Elliptic Curve는 위의 사진과 같은 개형을 보인다.  

$$
y^2 = x^3 + ax + b
$$

이 방법에서는 커브를 가로지르는 직선 $\overleftrightarrow{P_1 P_2}$ 이 커브와 만나는 또 다른 점 $P$ 를 이용한다. 실제로 사용할 $P_3$ 는 $P$ 를 지나는 수직선상에서 커브와 만나는 또 다른 점이다.  

이 때 $P_3$ 는 또 다른 방법으로 표현 가능하다.  

$$
P_3 = P_1 + P_2
$$

<br />

$P_1 = (x_1, y_1)$, $P_2 = (x_2, y_2)$ 일 때, $P_3 = (x_3, y_3)$ 는 다음과 같이 계산 가능하다.  

$$
x_3 = m^2 - x_1 - x_2 \mod p
$$

$$
y_3 = m(x_1 - x_3) - y_1 \mod p
$$

$$
m = (y_2 - y_1)(x_2 - x_1)^{-1} \mod p \quad \text{if } P_1 \neq P_2
$$

$$
m = (3x_1^2 + a)(2y_1)^{-1} \mod p \quad \text{if } P_1 = P_2
$$

또한 특수해로 $m$ 이 무한이라면, $P_3 = \infty$,  모든 $P$ 에 대해서는 $\infty + P = P$ 이다.\*

\*$P$ 가 무한대 점과 더해지면 $P$ 자신이 된다.  

## 예시

$$
y^2 = x^3 + 2x + 3 \mod 5
$$

일 때, $x$ 는 mod 5에 맞게 다섯 개 값을 계산한다.  

- $x = 0 \Rightarrow y^2 = 3 \mod 5 \Rightarrow \text{no solution}$
- $x = 1 \Rightarrow y^2 = 6 \mod 5 = 1 \Rightarrow y = 1, 4$
- $x = 2 \Rightarrow y^2 = 15 \mod 5 = 0 \Rightarrow y = 0$
- $x = 3 \Rightarrow y^2 = 36 \mod 5 = 1 \Rightarrow y = 1, 4$
- $x = 4 \Rightarrow y^2 = 75 \mod 5 = 0 \Rightarrow y = 0$

따라서 만족하는 점은 
$(1, 1), (1, 4), (2, 0), (3, 1), (3, 4), (4, 0)$  
와, 무한대 $\infty$ 이다.

## Diffie-Hellman에의 적용

- A의 키 계산: $A(B(x, y))$
- B의 키 계산: $B(A(x, y))$

<br />

- 공개 키: 커브 정의 $E$ 와 점 $P$
- 개인 키: $a, b$ (임의의 정수)

<br />

예:
- 공개 키
  - 커브 $y^2 = x^3 + 7x + b \mod 37$
  - 점 $P = (2, 5) \Rightarrow b = 3$
- 개인 키
  - $a = 4, b = 7$
- 키 계산
  - A의 전송: $A(P) = 4(2, 5) = (7, 32)$
  - B의 전송: $B(P) = 7(2, 5) = (18, 35)$
  - A의 키 계산: $A(B(P)) = 4(18, 35) = (22, 1)$
  - B의 키 계산: $B(A(P)) = 7(7, 32) = (22, 1)$
