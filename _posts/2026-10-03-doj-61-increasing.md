---
layout: post
title: 'DOJ #61 오름차순 만들기 문제 풀이'
date: '2026-10-03'
categories: [ps]
tags: [ps, doj, algorithm]
---

[DOJ, 〈#61 오름차순 만들기 `increasing`〉 문제 노트](https://doj.kr/ko/problems/61)

## 요약

- 접근 방법: 스위핑
- '증가 수열 만들기'를 목표로 하는 문제 처리에, '단조 증가 수열 만들기'를 목표로 하는 처리 수식을 활용하지 않는 것이 좋다.
- $K$ 가 문제에서 주어진 것과 같은 덧셈 단위일 때,
  - $\lceil \Delta / K \rceil$ 는 $A_i \le A_{i+1}$ 를 만족시키기 위해 필요한 최소한의 연산 횟수이다.
  - $\lfloor \Delta / K \rfloor + 1$ 은 $A_i < A_{i+1}$ 를 만족시키기 위해 필요한 최소한의 연산 횟수이다.

## 문제

주어진 $A = [A_1, A_2, \ldots, A_n]$, $K$ 에 대해서, $A$ 를 증가 수열로 만드려고 한다. $A$ 를 증가 수열로 만들기 위해 $A_i$ 에 $K$ 를 덧셈하는 연산의 최소 횟수를 구하여야 한다.  

어떤 $A_i$ 를 선택하더라도 $A_{i - 1}$ 보다 작아야 하므로, 모든 순간에서 이전 스텝의 $A_{i - 1}$ 값이 $A_i$ 를 처리하는 데 있어 기준점이 되어야 한다. 따라서 한 쪽 끝을 연산 처리의 시작점으로 설정하고, 다른쪽 끝을 향해 스위핑한다.  

$$
\begin{aligned}
O_1 &= \lceil (A_{i - 1} - A_i) / K \rceil \\
O_2 &= \lfloor (A_{i - 1} - A_i) / K \rfloor + 1 \\
A_{i, \text{new}} &= A_{i, \text{old}} + O_x \cdot K \\
\end{aligned}
$$

\* $K = 3$

| | $A_{i - 1}$ | $A_i$ | operator | compute | verdict |
| :-: | :-: | :-: | :-: | :-: | :-: |
| #1-1 | 8 | 7 | $O = \lceil (A_{i - 1} - A_i) / K \rceil$ | $O = \lceil (8 - 7) / 3 \rceil = 1$ <br /> $A_i = 7 + 1 \cdot 3 = 10$ | pass |
| #1-2 | 8 | 11 | $O = \lceil (A_{i - 1} - A_i) / K \rceil$ | $O = \lceil (8 - 11) / 3 \rceil = 0$ <br /> $A_i = 11 + 0 \cdot 3 = 11$ | pass |
| #1-3 | 8 | 8 | $O = \lceil (A_{i - 1} - A_i) / K \rceil$ | $O = \lceil (8 - 8) / 3 \rceil = 0$ <br /> $A_i = 8 + 0 \cdot 3 = 8$ | fail |
| #2 | 8 | 8 | $A_{i - 1, \text{new}} = A_{i - 1, \text{old}} + 1$ <br /> $O = \lceil (A_{i - 1, \text{new}} - A_i) / K \rceil$ <br /> $A_{i} = A_{i} + O \cdot K$ | $A_{i - 1, \text{old}} =  + 1 = 9$ <br /> $O = \lceil (9 - 8) / 3 \rceil = 1$ <br /> $A_i = 8 + 1 \cdot 3 = 11$ | pass |
| #3 | 8 | 8 | $O = \lfloor (A_{i - 1} - A_i) / K \rfloor + 1$ | $O = \lfloor (8 - 8) / 3 \rfloor + 1 = 1$ <br /> $A_i = 8 + 1 \cdot 3 = 11$ | pass |

#1, #2 방법은 단조 증가 수열을 만들기 위한 연산식을 변형한 것이다. 다만 그렇기 때문에 변형 과정에서 $A$ 가 단조 증가 수열을 표현하지 않도록 주의하여야 한다.  
