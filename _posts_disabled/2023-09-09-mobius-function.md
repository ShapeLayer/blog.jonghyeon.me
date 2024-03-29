---
layout: post
title: 뫼비우스 함수 알아보기
date: '2023-09-09'
categories: [math]
tags: [math]
---

뫼비우스 함수는 양의 정수에 대해 아래와 같이 정의되는 함수입니다.  

$$
\mu (n)
= \begin{cases}
1 & \text{(n=1)}  \\
(-1)^{\omega (n)} & \text{(n is square-free integer)}  \\
0 & \text{(otherwise)}  
\end{cases}
$$

이 함수는 정의로는 자세한 내용을 알기 어려운 것 같습니다.  

## Square-free
"Square-free"하다는 것은 소인수분해 시 제곱 인수가 존재하지 않는다는 것을 의미합니다.  

예를 들어, 6은 1, 2, 3, 6이 인수이니 square-free합니다. 하지만 12의 인수는 1, 2, 3, 4, 6, 12로 제곱수 4가 포함되므로 square-free하지 않습니다.  

잠시 $\mu (n)$의 정의를 확인해보면 square-free하지 않은 $n$은 모두 0으로 정의됨을 알 수 있습니다. 다시 말해 $\mu (n)$의 결과가 0이 아닌 값을 가지려면 $n$은 1이거나 square-free해야합니다.  

따라서 $\mu (6) \neq 0$이고, $\mu (12) = 0$입니다.  

## w(n), 소인수계량함수
$\mu (n)=(-1)^{\omega (n)} \, \text{(n is square-free integer)} $

남은 정의 중 $(-1)^{\omega (n)}$의 $\omega (n)$은 소인수계량함수를 의미합니다. 간단히 말해 $\omega (n)$은 $n$의 소인수의 개수입니다.  

예를 들어, 2는 2를 소인수로 갖습니다. 따라서 $\mu (2) = (-1)^{1}=-1$ 입니다. 6은 2, 3을 소인수로 갖습니다. 따라서 $\mu (6) = (-1)^{2}=1$ 입니다.  

## 뫼비우스 함수의 포함 배제 원리

정의대로 계산해보면 $\mu (2) \mu (3) = \mu (6) = 1$임을 알 수 있습니다.  

2와 3은 서로 소인수이므로 $2 \times 3$을 하더라도 여전히 square-free합니다. 그리고 $\mu (n)$에서 집중하는 것은 $\mu (n)$의 짝수, 홀수 여부입니다. $\mu (n)$은 $\omega (n)$이 홀수라면 -1, 짝수라면 1인데, $\omega (n)$이 홀수인 두 수가 곱해진 수는 $\omega (n)$이 짝수임이 자명하므로 $\mu (n)=1$입니다.  

## 뫼비우스 함수 사용하기

Square-free한 정수를 처리해야 할 때 뫼비우스 함수는 꽤 유용합니다. 대표적으로 백준 온라인 저지의 1557번 문제가 뫼비우스 함수를 사용해야하는 문제입니다.  

[백준 1557 제곱 ㄴㄴ 문제 풀이](/posts/2023-09-09-boj-1557)  
