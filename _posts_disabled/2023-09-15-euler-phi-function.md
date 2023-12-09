---
layout: post
title: 오일러 피 함수의 정의와 활용
date: '2023-09-15'
categories: [math]
tags: [math]
---

오일러 피 함수는 어떤 양의 정수 N에 대해서 1부터 N까지의 수 중 N과 서로소인 자연수의 개수를 구하는 함수입니다.

$$
\varphi (n) = \vert {m: 1 \leq m \leq n, gcd(m, n) = 1} \vert (n \in \mathbb{N}) \\
\varphi (n) = \sum_{d \vert n}{d \mu (\frac{n}{d})} = n \underset{p|n}{\Pi}(1-\frac{1}{p}) \\
= n(1 - \frac{1}{p_1})(1 - \frac{1}{p_2})...({1-\frac{1}{p_m}})
$$

$$
\varphi (20) = 20(1 - \frac{1}{2})(1 - \frac{1}{5}) = 20 \times \frac{1}{2} \times \frac{4}{5} = 8
$$
