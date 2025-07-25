---
layout: post
title: 기본 행 연산의 풀이 속도를 높여보자
date: '2024-04-19'
categories: [math]
tags: [math, linear-algebra, matrix, elementray-row-operation, gauss-jordan-elimination, reduced-row-echelon-form]
---

행렬의 기본 행 연산은 선형대수학의 가장 기초가 되는 연산이면서, 가장 자주 이용되는 연산입니다.

가장 자주 이용됨에도 불구하고 널리 알려진 기본 행 연산의 풀이 테크닉이 따로 없어 연산이 한 번 수행될 때마다 행렬 전체를 다시 작성해주어야 합니다.

$$
\begin{bmatrix}
1 & 1 & 2 & 9 \\
2 & 4 & -3 & 1 \\
3 & 6 & -5 & 0
\end{bmatrix}
$$

가령 이러한 행렬을 기본 행 연산으로 기약 행 사다리꼴로 만들고자 한다면 다음과 같이 모든 연산 작업마다 행렬 전체를 재작성하게됩니다.

$$
\begin{bmatrix}
1 & 1 & 2 & 9 \\
0 & 2 & -7 & -17 \\
3 & 6 & -5 & 0
\end{bmatrix}
$$

첫째 행에 -2를 곱한 값을 둘째 행에 더함.

$$
\begin{bmatrix}
1 & 1 & 2 & 9 \\
0 & 1 & -7/2 & -17/2 \\
3 & 6 & -5 & 0
\end{bmatrix}
$$

둘째 행에 1/2를 곱함.

$$
\begin{bmatrix}
1 & 0 & 11/2 & 35/2 \\
0 & 1 & -7/2 & -17/2 \\
0 & 0 & 1 & 3
\end{bmatrix}
$$

(중간 과정 생략)

$$
\begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3
\end{bmatrix}
$$

셋째 행에 -11/2를 곱한 값을 첫째 행에 더하고, 셋째 행에 7/2를 곱한 값을 둘째 행에 더함.

이렇게 기본 행 연산으로 행렬의 내용이 변경될 때 마다 행렬 전체를 다시 작성하는 것은 보기 편하지만, 필기로 수식을 계산할 때는 꽤 소모적일 수밖에 없습니다.

일반적인 수식을 필기로 전개하고 풀어낼 때와는 연산 한 회마다의 속도 차이가 너무 큽니다.

## 두 열의 순서를 변경하더라도 행렬은 변하지 않는다.

기본 행 연산 중 하나로, “두 열의 순서를 서로 변경”하는 작업이 있습니다.

$$
\begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3
\end{bmatrix}
,
\begin{bmatrix}

0 & 1 & 0 & 2 \\
1 & 0 & 0 & 1 \\
0 & 0 & 1 & 3
\end{bmatrix}
$$

때문에 위 두 식은 본질적으로 같습니다.

그렇다면 기본 행 연산의 결과를 매번 다시 작성하는 것이 아니라, 아래에 행 하나를 추가로 붙여쓰고 원래의 행에 취소선을 긋는다고 하더라도 문제되지 않을 것입니다.

$$
(1) \begin{bmatrix}
1 & 1 & 2 & 9 \\
2 & 4 & -3 & 1 \\
3 & 6 & -5 & 0
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 & 1 & 2 & 9 \\
0 & 2 & -7 & -17 \\
3 & 6 & -5 & 0
\end{bmatrix}
\\
(2) \begin{bmatrix}
1 & 1 & 2 & 9 \\
2 & 4 & -3 & 1 \\
3 & 6 & -5 & 0
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
1 & 1 & 2 & 9 \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
3 & 6 & -5 & 0  \\
0 & 2 & -7 & -17
\end{bmatrix}
$$

(1)이 첫째 행에 -2를 곱한 값을 둘째 행에 더한 것이라면, (2)는 (1)에 더해 둘째 행을 셋째 행과 서로 변경한 것이라고 생각할 수 있습니다.

$$
\begin{bmatrix}
1 & 1 & 2 & 9 \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
\enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{6} & \enclose{horizontalstrike}{-5} & \enclose{horizontalstrike}{0}  \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{-7} & \enclose{horizontalstrike}{-17} \\
0 & 1 & -7/2 & -17/2 \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{-11} & \enclose{horizontalstrike}{-27} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{-1/2} & \enclose{horizontalstrike}{-3/2} \\
0 & 0 & 1 & 3
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{9} \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
\enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{6} & \enclose{horizontalstrike}{-5} & \enclose{horizontalstrike}{0}  \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{-7} & \enclose{horizontalstrike}{-17} \\
0 & 1 & -7/2 & -17/2 \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{-11} & \enclose{horizontalstrike}{-27} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{-1/2} & \enclose{horizontalstrike}{-3/2} \\
0 & 0 & 1 & 3 \\
1 & 0 & 11/2 & 35/2
\end{bmatrix}
$$

더 나아가서 기본 행 연산이 충분히 진행되었을 때, 첫째 행이 셋째 행으로 내려가고 나머지 행이 한 칸씩 위로 올라가는 상황이 발생합니다. 

구체적으로는 둘째 행은 첫째 행, 셋째 행은 첫째 행이 되고, 첫째 행은 제일 끝으로 내려갔습니다.

다시 말해 취소선이 그어지는 행과, 끝 행이 바로 위-아래에 위치한 관계가 아니라면 모든 행의 위치가 한번에 모두 변경되는 것입니다.

이것을 한 번에 발생한 것으로 생각하여 기본 행 연산이 아니라고 할지 모르겠지만, 결국 취소선이 새로 그어지는 $i$째 행부터 $n$째 행까지 순차적으로 $i$째 행과 $i+1$째 행이 서로 교환되었다고 생각할 수 있습니다. ($n$은 행렬의 열의 개수)

결국 행렬은 본직적으로 동일합니다.

마지막으로 확인할 사항은, 행렬 양 끝에 붙은 대괄호입니다.

$$
\begin{matrix}
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{9} \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
\enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{6} & \enclose{horizontalstrike}{-5} & \enclose{horizontalstrike}{0}  \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{-7} & \enclose{horizontalstrike}{-17} \\
0 & 1 & -7/2 & -17/2 \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{-11} & \enclose{horizontalstrike}{-27} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{-1/2} & \enclose{horizontalstrike}{-3/2} \\
0 & 0 & 1 & 3 \\
1 & 0 & 11/2 & 35/2
\end{matrix}
$$

이미 필기로 작성된 대괄호는 이와 같이 계속해서 행렬의 세로 길이가 늘어나는 것을 상정하지 않았습니다. 상정한다고 하더라도, 늘어난 행렬을 정확히 커버할 수 있을 정도로 길게 작성하는 것은 좋은 일은 아닐 것입니다.

$$
\begin{matrix}
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{9} \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
\enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{6} & \enclose{horizontalstrike}{-5} & \enclose{horizontalstrike}{0}  \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{-7} & \enclose{horizontalstrike}{-17} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{-7/2} & \enclose{horizontalstrike}{-17/2} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{-11} & \enclose{horizontalstrike}{-27} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{-1/2} & \enclose{horizontalstrike}{-3/2} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{3} \\
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{11/2} & \enclose{horizontalstrike}{35/2} \\
1 & 0 & 0 & 1 \\
0 & 0 & 1 & 3 \\
0 & 1 & 0 & 2
\end{matrix}
$$

그래서 대괄호는 지우겠습니다.

$$
\begin{matrix}
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{9} \\
\enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{4} & \enclose{horizontalstrike}{-3} & \enclose{horizontalstrike}{1} \\
\enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{6} & \enclose{horizontalstrike}{-5} & \enclose{horizontalstrike}{0}  \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{2} & \enclose{horizontalstrike}{-7} & \enclose{horizontalstrike}{-17} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{-7/2} & \enclose{horizontalstrike}{-17/2} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{3} & \enclose{horizontalstrike}{-11} & \enclose{horizontalstrike}{-27} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{-1/2} & \enclose{horizontalstrike}{-3/2} \\
\enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{3} \\
\enclose{horizontalstrike}{1} & \enclose{horizontalstrike}{0} & \enclose{horizontalstrike}{11/2} & \enclose{horizontalstrike}{35/2} \\
1 & 0 & 0 & 1 \\
0 & 0 & 1 & 3 \\
0 & 1 & 0 & 2
\end{matrix}
\Rightarrow
\begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 0 & 1 & 3 \\
0 & 1 & 0 & 2
\end{bmatrix} \\
\Rightarrow
\begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3
\end{bmatrix}
$$

기본 행 연산을 더 진행해서, 기약 행 사다리꼴을 획득했습니다.
