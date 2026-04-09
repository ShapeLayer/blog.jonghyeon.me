---
layout: post
title: 교차분석에서의 카이제곱검정의 활용
date: 2026-04-09
category: [probability-and-statistics]
---

〈빅데이터의과학적탐구〉 수업 노트

<br />

카이제곱검정은 교차되는 두 범주형 변수가 서로 독립인지 여부를 검증하는 통계적 방법이다.  

획득한 어떤 데이터에 대해서, 실제로 이들 데이터가 완전히 독립적일 때 기대할 수 있는 데이터 분포가, 실제 데이터 분포와 얼마나 다른지 계산하는 방식으로 검정을 수행한다. 만약 데이터 분포가 카이제곱분포를 잘 따르고 있다면, 데이터 분포는 기대 분포와 크게 다르지 않을 것이다.  

$$
\chi^2 = \sum_{i=1}^n \frac{(O_i - E_i)^2}{E_i}
$$

여기서 $O_i$ 는 관측된 빈도수이고, $E_i$ 는 기대되는 빈도수이다.

검정통계량은 카이제곱 확률변수의 정의를 응용한 것이다. 두 변수를 교차하는 표를 작성하였을 때, 각 셀에 대해 실제 관측된 빈도 $O_i$, 독립이라는 가정 하에 기대되는 빈도 $E_i$ 을 사용한다.  

$$
\begin{aligned}
Z_i &= \frac{O_i - E_i}{\sqrt{E_i}} \\
\chi^2 &= \sum_{i=1}^n Z_i^2 = \sum_{i=1}^n \frac{(O_i - E_i)^2}{E_i}
\end{aligned}
$$

<br />

이렇게 계산된 $\chi^2$ 값이 카이제곱분포에서 특정 자유도에 해당하는 임계값보다 크면, 귀무가설을 기각하고 두 범주형 변수가 독립이 아니라고 결론지을 수 있다. 교차분석에서 귀무가설은 항상 두 변수가 독립이라는 가정이다.

일반적으로 임계값은 유의수준 $\alpha$ 에 따라 결정된다. 만약 $\alpha = 0.05$ 라면, 카이제곱분포에서 자유도에 해당하는 값이 95% 신뢰구간의 상한값이다. 만약 계산된 $\chi^2$ 값이 이 임계값보다 크다면, 귀무가설을 기각한다.  

## 예시

성별과 직업을 조사한 어떤 설문조사에서, 다음과 같은 결과를 획득하였다고 가정한다.  

| 직업\성별 | 남성 | 여성 | 합계 |
| --- | --- | --- | --- |
| 공무원 | 9 | 3 | 12 |
| 농어업 | 13 | 0 | 13 |
| 자영업 | 11 | 6 | 17 |
| 전문직 | 7 | 10 | 17 |
| 회사원 | 15 | 16 | 31 |
| 합계 | 55 | 35 | 90 |

이 데이터는 교차되는 두 범주형 변수를 가지고 있다. 이 데이터를 근거로 "성별은 직업에 영향을 미치지 않는다"는 주장의 타당성을 검증하려고 할 때, 카이제곱검정을 사용할 수 있다.  

```R
# data$직업, data$성별 에 대해 교차검정
# 소수점 세자리까지 표시
# 표시할 셀의 최대 너비는 5
# 기대빈도 표시
# 행 비율 표시
# 맥네마 검정은 수행하지 않음
cross_table <- CrossTable(data$직업, data$성별, digits=3, max.width=5, expected=TRUE, prop.r=TRUE, mcnemar=FALSE)
```

<p><strong>Cell Contents</strong></p>
<ul>
      <li>N: 관측 빈도</li>
      <li>Expected N: 기대 빈도</li>
      <li>Chi-square contribution: 카이제곱 기여도</li>
      <li>N / Row Total: 행 비율</li>
      <li>N / Col Total: 열 비율</li>
      <li>N / Table Total: 전체 비율</li>
</ul>

<p><strong>Total Observations in Table:</strong> 90</p>

<table>
      <thead>
            <tr>
                  <th>직업</th>
                  <th>성별</th>
                  <th>N</th>
                  <th>Expected N</th>
                  <th>Chi-square</th>
                  <th>N/Row</th>
                  <th>N/Col</th>
                  <th>N/Table</th>
                  <th>Row Total</th>
            </tr>
      </thead>
      <tbody>
            <tr>
                  <td rowspan="2">공무원</td>
                  <td>남자</td>
                  <td>9</td><td>7.333</td><td>0.379</td><td>0.750</td><td>0.164</td><td>0.100</td><td rowspan="2">12 (0.133)</td>
            </tr>
            <tr>
                  <td>여자</td>
                  <td>3</td><td>4.667</td><td>0.595</td><td>0.250</td><td>0.086</td><td>0.033</td>
            </tr>
            <tr>
                  <td rowspan="2">농어업</td>
                  <td>남자</td>
                  <td>13</td><td>7.944</td><td>3.217</td><td>1.000</td><td>0.236</td><td>0.144</td><td rowspan="2">13 (0.144)</td>
            </tr>
            <tr>
                  <td>여자</td>
                  <td>0</td><td>5.056</td><td>5.056</td><td>0.000</td><td>0.000</td><td>0.000</td>
            </tr>
            <tr>
                  <td rowspan="2">자영업</td>
                  <td>남자</td>
                  <td>11</td><td>10.389</td><td>0.036</td><td>0.647</td><td>0.200</td><td>0.122</td><td rowspan="2">17 (0.189)</td>
            </tr>
            <tr>
                  <td>여자</td>
                  <td>6</td><td>6.611</td><td>0.056</td><td>0.353</td><td>0.171</td><td>0.067</td>
            </tr>
            <tr>
                  <td rowspan="2">전문직</td>
                  <td>남자</td>
                  <td>7</td><td>10.389</td><td>1.105</td><td>0.412</td><td>0.127</td><td>0.078</td><td rowspan="2">17 (0.189)</td>
            </tr>
            <tr>
                  <td>여자</td>
                  <td>10</td><td>6.611</td><td>1.737</td><td>0.588</td><td>0.286</td><td>0.111</td>
            </tr>
            <tr>
                  <td rowspan="2">회사원</td>
                  <td>남자</td>
                  <td>15</td><td>18.944</td><td>0.821</td><td>0.484</td><td>0.273</td><td>0.167</td><td rowspan="2">31 (0.344)</td>
            </tr>
            <tr>
                  <td>여자</td>
                  <td>16</td><td>12.056</td><td>1.291</td><td>0.516</td><td>0.457</td><td>0.178</td>
            </tr>
            <tr>
                  <td colspan="2">Column Total</td>
                  <td>90</td>
                  <td>-</td>
                  <td>-</td>
                  <td>-</td>
                  <td>-</td>
                  <td>1.000</td>
                  <td>90</td>
            </tr>
            <tr>
                  <td colspan="2">성별 합계</td>
                  <td>남자 55 / 여자 35</td>
                  <td>-</td>
                  <td>-</td>
                  <td>-</td>
                  <td>남자 0.611 / 여자 0.389</td>
                  <td>-</td>
                  <td>-</td>
            </tr>
      </tbody>
</table>

<p><strong>Statistics for All Table Factors</strong></p>
<table>
      <thead>
            <tr>
                  <th>Test</th>
               <th>Chi-square</th>
                  <th>d.f.</th>
                  <th>p-value</th>
            </tr>
      </thead>
      <tbody>
            <tr>
                  <td>Pearson's Chi-squared test</td>
                  <td>14.29367</td>
                  <td>4</td>
                  <td>0.006414416</td>
            </tr>
      </tbody>
</table>

$\chi^2$ 값이 14.29367, 유의수준 0.006으로, 95% 신뢰구간 바깥을 기각할 때, 가설을 기각할 수 있다. 따라서, 성별과 직업은 독립이 아니라고 결론지을 수 있다.
