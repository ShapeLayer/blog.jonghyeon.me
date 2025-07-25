---
layout: post
title: 프로그래머스 우유와 요거트가 담긴 장바구니 문제 풀이
date: '2024-02-24'
categories: [ps, programmers]
tags: [ps, programmers, sql]
---

## 문제 파악하기

[프로그래머스, 우유와 요거트가 담긴 장바구니](https://school.programmers.co.kr/learn/courses/30/lessons/62284)

문제가 요구하는 것은 우유와 요거트를 동시에 구입한 장바구니의 ID를 찾아내는 것이므로, 우유와 요거트를 모두 구매한 장바구니를 어떻게 찾을 것인지를 잘 고려해보아야할 것 같습니다.  

| NAME | TYPE |
| :-: | :-: |
| `ID` |`INT` |
| `CART_ID` | `INT` |
| `NAME` | `VARCHAR` |
| `PRICE` | `INT` |

하지만 테이블은 위와 같이 물건 하나 당 항목이 하나 생성되므로, 바로 `WHERE` 문을 사용하기는 꽤 어려울 것 같습니다.  

## 문제 풀어보기

이 문제에서 구매했는지 확인해야 할 항목은 우유와 요거트 단 두 개 뿐, 신경써야 할 항목이 가변적이거나 매우 많지 않습니다.  

따라서 우유 구매 여부를 0번째 비트, 요거트 구매 여부를 1번째 비트에 담은 2진수 값을 만들어 장바구니 별로 하나의 항목만 남도록 병합해보았습니다.  

```sql
SELECT CART_ID, BIT_OR(CODE) AS BIT
FROM (
    SELECT CART_ID,
        CASE NAME
            WHEN 'Milk' THEN 1
            WHEN 'Yogurt' THEN 2
        ELSE 0
        END AS CODE
    FROM CART_PRODUCTS
) BIT_QUERIED
GROUP BY CART_ID;
```

우선 모든 구매 항목에 대해, 우유는 1, 요거트는 2, 그 외 항목은 0으로 변환하고, `CART_ID`를 중심으로 OR 연산을 걸어줍니다.  

이 경우 우유와 요거트를 모두 구매한 장바구니는 이 구매 내용 비트가 3이 됩니다.

$
2 ^ 1 * 1 + 2 ^ 0 * 1 = 3
$

우유와 요거트를 모두 구매한 장바구니는 구매 내용 비트가 3인지만 확인하면 어렵지 않게 확인할 수 있으므로, `WHERE BIT = 3`과 같이 조건을 걸어 정리할 수 있습니다.

### 답안 구현
[62284 MYSQL 답안](https://github.com/ShapeLayer/training/blob/main/tasks/online_judge/programmers/sql/62284.sql)
