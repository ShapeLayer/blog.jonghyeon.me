---
layout: post
title: 최소항의 합과 최대항의 곱
date: '2024-04-11'
categories: [logic-circuit]
tags: [logic-circuit, computer-science, bool]
---

논리회로를 설계하는 데 있어서, 리터럴과 대수적 표현식을 최적화하는 것은 중요합니다.  

여느 최적화나 다 그렇듯, 식을 적절하게 즉 최적화하면 전체 시스템에 투입할 자원도 줄이고, 시스템 전체의 복잡성도 줄일 수 있습니다.  

## 곱항, 최소항, 정규합과 최소 곱의합

**곱항(product term)** 은 리터럴이 AND(곱) 연산으로 연결된 것으로, $abc$ , $a'b$ 와 같이 표현합니다.  

곱항이 시스템에 투입되는 변수를 모두 포함하고 있다면 **표준곱항(standard product term)** 이라고 하면서, **최소항(minterm)** 이라고 합니다.  

$w$ , $x$ , $y$ , $z$ 네 개 변수를 사용하는 시스템에서 $wxy'z'$ 는 표준곱항이지만, $xyz$ 는 $w$ 를 사용하지 않았으므로 표준곱항으로 볼 수 없습니다.  

곱항 여러 개를 OR(합) 연산한 식을 **곱의합(sum of products; SOP)** 라고 정의하는데, 대표적으로는 아래와 같습니다.  

1. $w'xyz + wxy'z + wxyz$
2. $x + wy' + wxy'z'$
3. $wz'$
4. $x'$

이러한 곱의합 중, 모든 합이 표준곱항으로 이루어진 곱의합 식을 **정규합(canonical sum)** , **표준곱항의 합(sum of standard product terms)** 혹은 **최소항의 합(sum of minterms)** 라고 합니다. 이러한 용어는 단순히 표준곱항과 최소항이 동의어이기 때문에 늘어난 것입니다.  

또 **최소 곱의합(minimum sum of products)** 도 있는데, 가장 적은 수의 곱항을 가지고, 가능한 경우 중 가장 적은 수의 리터럴을 가지는 곱의합 식을 의미합니다.  

<table>
  <thead>
    <tr>
      <th>명칭(국문)</th>
      <th>명칭(영문)</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>곱항</td>
      <td>product term</td>
      <td>곱 연산 항</td>
    </tr>
    <tr>
      <td>표준곱항</td>
      <td>standard product term</td>
      <td rowspan="2">시스템의 모든 변수를 사용한 곱항</td>
    </tr>
    <tr>
      <td>최소항</td>
      <td>minterm</td>
    </tr>
    <tr>
      <td>곱의합</td>
      <td>sum of products; SOP</td>
      <td>곱항이 합 연산으로 연결된 항</td>
    </tr>
    <tr>
      <td>정규합</td>
      <td>canonical sum</td>
      <td rowspan="3">모든 항이 표준곱항으로 이루어진 곱의합 식</td>
    </tr>
    <tr>
      <td>표준곱항의 합</td>
      <td>sum of standard product terms</td>
    </tr>
    <tr>
      <td>최소항의 합</td>
      <td>sum of minterms</td>
    </tr>
    <tr>
      <td>최소 곱의합</td>
      <td>minimum sum of products</td>
      <td>
        가장 적은 수의 곱항을 가지는 곱의합 식<br />
        (+가능한 식 중 리터럴의 개수가 가장 적은 식)
      </td>
    </tr>
  </tbody>
</table>

1. $x'yz' + x'yz + xy'z' + xy'z + xyz$
2. $x'y + xy' + xyz$
3. $x'y + xy' xz$

위 세 식은 $x$ , $y$ , $z$ 를 변수로 사용하는 동일한 시스템을 서술하고 있습니다. 구체적으로는 점차 최적화되었습니다.  

* &lt;1.&gt; 식은 $x$ , $y$ , $z$ 모두를 포함하니 표준곱항의 합입니다.  
* &lt;3.&gt; 식은 가장 적은 수의 곱항을 가지는 곱의합 식이므로 최소 곱의합입니다.  

## 합항, 최대항, 정규곱과 최소 합의곱

곱 연산에 대한 정의와 비슷하게 합 연산에 대한 정의도 존재합니다.  

**합항(sum term)** 은 리터럴이 OR(합) 연산으로 연결된 것으로, $a + b + c$ , $a'+b$ 와 같이 표현합니다.  

합항이 시스템에 투입되는 변수를 모두 포함하고 있다면 **표준합항(standard sum term)** 이라고 하면서, **최대항(maxterm)** 이라고 합니다.  

$w$ , $x$ , $y$ , $z$ 네 개 변수를 사용하는 시스템에서 $w + x + y' + z'$ 는 표준합항이지만, $x+ y + z$ 는 $w$ 를 사용하지 않았으므로 표준합항으로 볼 수 없습니다.  

합항 여러 개를 AND(곱) 연산한 식을 **합의곱(product of sums)** 라고 정의하는데, 대표적으로는 아래와 같습니다.  

1. $(w' + x + y + z)(w + x + y' + z)(w + x + y + z)$
2. $x(w + y')(w + x + y' + z')$
3. $w + z'$
4. $x'$

이러한 합의곱 중, 모든 곱이 표준합항으로 이루어진 곱의합 식을 **정규곱(canonical product)** , **표준합항의 곱(product of standard sum terms)** 혹은 **최대항의 곱(sum of maxterms)** 라고 합니다.  

또 **최소 합의곱(minimum product of sums)** 는 가장 적은 수의 합항을 가지고, 가능한 경우 중 가장 적은 수의 리터럴을 가지는 합의곱 식을 의미합니다.  

<table>
  <thead>
    <tr>
      <th>명칭(국문)</th>
      <th>명칭(영문)</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>합항</td>
      <td>sum term</td>
      <td>합 연산 항</td>
    </tr>
    <tr>
      <td>표준합항</td>
      <td>standard sum term</td>
      <td rowspan="2">시스템의 모든 변수를 사용한 합항</td>
    </tr>
    <tr>
      <td>최대항</td>
      <td>maxterm</td>
    </tr>
    <tr>
      <td>합의곱</td>
      <td>product of sums; POS</td>
      <td>합항이 곱 연산으로 연결된 항</td>
    </tr>
    <tr>
      <td>정규곱</td>
      <td>canonical product</td>
      <td rowspan="3">모든 항이 표준합항으로 이루어진 합의곱 식</td>
    </tr>
    <tr>
      <td>표준합항의 곱</td>
      <td>product of standard sum terms</td>
    </tr>
    <tr>
      <td>최대항의 곱</td>
      <td>product of maxterms</td>
    </tr>
    <tr>
      <td>최소 합의곱</td>
      <td>minimum product of sums</td>
      <td>
        가장 적은 수의 합항을 가지는 합의곱 식<br />
        (+가능한 식 중 리터럴의 개수가 가장 적은 식)
      </td>
    </tr>
  </tbody>
</table>

## 합항.. 곱의합.. 최소 곱의합, 최소항의 곱..?

역 개념이 비슷한 이름으로 계속해서 정의되니 용어가 쌓일수록 헷갈리기 쉽습니다. 개념을 요약하자면 다음과 같습니다.  

<table>
  <thead>
    <tr>
      <th colspan="3">곱항</th>
      <th colspan="3">합항</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>곱항</td>
      <td>product term</td>
      <td>곱 연산 항</td>
      <td>합항</td>
      <td>sum term</td>
      <td>합 연산 항</td>
    </tr>
    <tr>
      <td>표준곱항</td>
      <td>standard product term</td>
      <td rowspan="2">시스템의 모든 변수를 사용한 곱항</td>
      <td>표준합항</td>
      <td>standard sum term</td>
      <td rowspan="2">시스템의 모든 변수를 사용한 합항</td>
    </tr>
    <tr>
      <td>최소항</td>
      <td>minterm</td>
      <td>최대항</td>
      <td>maxterm</td>
    </tr>
    <tr>
      <td>곱의합</td>
      <td>sum of products; SOP</td>
      <td>곱항이 합 연산으로 연결된 항</td>
      <td>합의곱</td>
      <td>product of sums; POS</td>
      <td>합항이 곱 연산으로 연결된 항</td>
    </tr>
    <tr>
      <td>정규합</td>
      <td>canonical sum</td>
      <td rowspan="3">모든 항이 표준곱항으로 이루어진 곱의합 식</td>
      <td>정규곱</td>
      <td>canonical product</td>
      <td rowspan="3">모든 항이 표준합항으로 이루어진 합의곱 식</td>
    </tr>
    <tr>
      <td>표준곱항의 합</td>
      <td>sum of standard product terms</td>
      <td>표준합항의 곱</td>
      <td>product of standard sum terms</td>
    </tr>
    <tr>
      <td>최소항의 합</td>
      <td>sum of minterms</td>
      <td>최대항의 곱</td>
      <td>product of maxterms</td>
    </tr>
    <tr>
      <td>최소 곱의합</td>
      <td>minimum sum of products</td>
      <td>
        가장 적은 수의 곱항을 가지는 곱의합 식<br />
        (+가능한 식 중 리터럴의 개수가 가장 적은 식)
      </td>
      <td>최소 합의곱</td>
      <td>minimum product of sums</td>
      <td>
        가장 적은 수의 합항을 가지는 합의곱 식<br />
        (+가능한 식 중 리터럴의 개수가 가장 적은 식)
      </td>
    </tr>
  </tbody>
</table>

## 드모르간의 법칙과 minterm, maxterm

다행인지 불행인지 모르겠지만, 이렇게 상보적인 정의들은 모두 회로의 최적화에 쓰입니다.

표현이 다르더라도 합항을 사용하든, 곱항을 사용하든 같은 회로를 표현할 수 있기 때문입니다.  

$(AB)' = A' + B'$  

$(A + B)' = A'B'$

$(X_1 X_2 \cdots X_n)' = X_1' + X_2' + \cdots + X_n'$

$(X_1 + X_2 + \cdots + X_n) = X_1' X_2' \cdots X_n'$

드모르간의 법칙은 리터럴의 보수 처리에 대해 위의 식들이 성립함을 보장합니다.  

드모르간의 법칙을 활용하면 최소항의 합과 최대항의 곱의 관계를 잘 파악할 수 있습니다.  

| $x$ | $y$ | 최소항의 합($\Sigma$) | 최대항의 곱($\Pi$) |
| :-: | :-: | :-: | :-: |
| $0$ | $0$ | $x'y'$ | $x + y$ |
| $0$ | $1$ | $x'y$ | $x + y'$ |
| $1$ | $0$ | $xy'$ | $x' + y$ |
| $1$ | $1$ | $xy$ | $x' + y'$ |

_최소항의 합과 최대항의 곱에 대한 진리표_  

| $x$ / $y$ | $0$ | $1$ |
| :-: | :-: | :-: |
| $0$ | SOP | POS |
| $1$ | POS | POS |

$(x, y) = (0, 0)$ _일 때 카르노 맵_

네. 직관에 따라 "상보적"이라고 표현했지만, 최소항의 합과 최대항의 곱은 정확히 보수 관계입니다.  
