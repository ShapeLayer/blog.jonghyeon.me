---
layout: post
title: F-분포와 F-검정
date: 2026-04-09
category: [probability-and-statistics]
---

〈빅데이터의과학적탐구〉 수업 노트

<br />

$F$-분포는 동일한 분산을 가지고 있는 두 개의 정규분포에서 추출된, 표본 분산들 간의 비율이 이루는 분포를 의미한다. 독립적인 두 $\chi^2$-분포에 관한 비율로 정의된다. 분산 비 검정, 분산 분석, 회귀 분석에서 자주 사용된다.  

![](/static/posts/2026-04-09-f-distribution-and-f-test/fdist-graph.png)

<br />

$\chi^2_{v_1}$ 을 따르는 $U_1$ 과 $\chi^2_{v_2}$ 을 따르는 $U_2$ 가 서로 독립일 때, $F$-분포를 따르는 확률변수 $F$ 는 다음과 같이 정의한다.  

$$
X = \frac{U_1 / v_1}{U_2 / v_2} \sim F_{v_1, v_2}
$$

\* $v_1$ 과 $v_2$ 는 자유도

$E(X) = \frac{v_2}{v_2 - 2}$ (단, $v_2 > 2$) , $Var(X) = \frac{2 v_2^2 (v_1 + v_2 - 2)}{v_1 (v_2 - 2)^2 (v_2 - 4)}$ (단, $v_2 > 4$) 이다.  

## 분산비검정($F$-검정)

$F$-분포 정의를 이용하여 두 분산을 비교하는 분산비검정(Variance Ratio Test)을 수행할 수 있다.  

$$
\begin{aligned}
U_1 = \frac{(n_1 - 1) s_1^2}{\sigma^2_1} \sim \chi^2_{n_1 - 1}, \quad U_2 = \frac{(n_2 - 1) s_2^2}{\sigma^2_2} \sim \chi^2_{n_2 - 1}
\end{aligned}
$$

$$
\begin{aligned}
F &= \frac{U_1 / v_1}{U_2 / v_2} \\
&= \frac{\cancel{(n_1 - 1)} s_1^2 / (\sigma^2_1 \cdot \cancel{v_1})}{\cancel{(n_2 - 1)} s_2^2 / (\sigma^2_2 \cdot \cancel{v_2})} \\
&= \frac{s_1^2 / \sigma^2_1}{s_2^2 / \sigma^2_2} \\
&= \frac{s_1^2}{s_2^2} \quad \text{(귀무가설 $H_0: \sigma^2_1 = \sigma^2_2$ 하에서)} \\
&\sim F_{n_1 - 1, n_2 - 1} \quad \text{(귀무가설 $H_0$ 하에서)}
\end{aligned}
$$

<br />

```R
> var.test(groupA$쇼핑액, groupB$쇼핑액)
```

```
	F test to compare two variances

data:  groupA$쇼핑액 and groupB$쇼핑액
F = 0.54726, num df = 54, denom df = 34, p-value = 0.04663
alternative hypothesis: true ratio of variances is not equal to 1
95 percent confidence interval:
 0.2893694 0.9910244
sample estimates:
ratio of variances 
         0.5472642 
```

이 사례에서는 $F$-값이 0.54726, $p$-값(유의확률)이 0.04663으로 일반적인 유의수준인 0.05보다 작다.  

또한, 두 분산의 비율에 대한 95% 신뢰구간인 (0.2893694, 0.9910244) 사이에 귀무가설이 가정하는 비율, $1$이 포함되어 있지 않으므로 귀무가설을 기각한다. 만약 귀무가설이 참이라면, 두 그룹의 분산이 같은 경우에 발생 가능한 비율 $1$이 신뢰구간에 포함되어야 한다.  

따라서, 두 그룹의 분산은 통계적으로 유의미하게 다르다(이분산이다)고 결론지을 수 있다.
