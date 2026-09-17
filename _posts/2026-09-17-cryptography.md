---
layout: post
title: 'Cryptography'
date: '2026-09-17'
category: [security]
---

_〈컴퓨터정보보안〉 수업 노트_

## Cryptography

Cipher 혹은 Cryptosystem은 평문을 암호화한 것, 혹은 그 알고리즘을 의미한다. 기본적으로 외부의 인물이 평문을 확인하는 것을 막기 위해 사용한다.  

크립토시스템은 Kerckhoffs 원칙을 기본으로 전제한다.
- 시스템은 완전히 잘 알려져있다.
- 오직 키만이 비밀이다.

이렇게 전제하는 것은, cryptosystem의 구현은 항상 역공학이 가능하고, 알고리즘이 평생 비밀로 남아있을 것으로 기대하는 것이 불가능하기 때문이다. 대신 차라리 알고리즘을 공개하여 알고리즘의 약점을 공개 검토하는 것이 보안 측면에서는 더욱 유익하다.  

## 키

암호 알고리즘의 성능을 판단하는 주효한 고려 사항은 암호 체계가 사용하는 키의 경우의 수이다. 완전 탐색을 수행한다고 가정할 때, 밣생 가능한 키의 가짓수가 늘어날수록 탐색에 수행되는 시간은 증가하고, 이 시간을 비현실적인 수준이 되도록 만들어두기만 해도 안전을 확보할 수 있다.    

### 카이사르 암호

최초의 암호화 알고리즘으로 여겨지는 카이사르 암호는, 알파벳 전체를 shift하는 것으로 실현한다.

<table>
  <tbody>
    <tr>
      <td>원문</td>
      <td>a</td>
      <td>b</td>
      <td>c</td>
      <td>d</td>
      <td>e</td>
      <td>...</td>
    </tr>
    <tr>
      <td>암호문</td>
      <td>E</td>
      <td>F</td>
      <td>G</td>
      <td>H</td>
      <td>I</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

이 암호가 쉽게 풀리는 것은 알고리즘 자체의 문제 측면에서보다는 가능한 키의 경우가 현저히 적은 것이 더 크다고 할 수 있다. shift하는 횟수가 키이므로, 0-shift를 제외하고 단 25개의 키(1, 2, ..., 25)만 존재해 25회만 완전 탐색하면 풀리기 때문이다.  

<br />

이후에 10세기 경까지는 이것을 일반화해 알파벳을 1:1 대응하여 사용하곤 했다.

<table>
  <tbody>
    <tr>
      <td>원문</td>
      <td>a</td>
      <td>b</td>
      <td>c</td>
      <td>...</td>
    </tr>
    <tr>
      <td>암호문</td>
      <td>K<br />(26개 중 하나)</td>
      <td>P<br />(25개 중 하나)</td>
      <td>Z<br />(24개 중 하나)</td>
      <td>...</td>
    </tr>
  </tbody>
</table>

이렇게 하면 26!가지의 키가 존재할 수 있다. $25! > 2^{88}$ 이므로, 1초에 $2^{40}$ 개 키를 시도할 수 있는 컴퓨터를 가정한다면, 완전히 탐색하는 데 약 8.9백만년이 소요된다. 이정도가 되면 비로소 완전탐색에 대해서 강건하다고 할 수 있다.  

## 부채널 공격

하지만 일반화된 카이사르 암호를 실제로 사용할 수는 없다. 알고리즘에 따라서는 가능한 모든 키를 탐색하지 않아도 평문을 추정할 수 있다. 이 방법을 부채널 공격이라고 한다.  

### 알파벳 등장 비율의 통계적 접근

카이사르 암호와 같이 평문과 암호문의 문자가 1:1로 대치될 때, 평문이 작성되는 언어의 통계를 사용하여 추정할 수 있다. 영어의 경우에는 모음 aeiou와 t 등이 높은 빈도로 등장한다. 

<table>
  <tr>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>D</th>
    <th>E</th>
    <th>F</th>
    <th>G</th>
    <th>H</th>
  </tr>
  <tr>
    <td>21</td>
    <td>26</td>
    <td>6</td>
    <td>10</td>
    <td>12</td>
    <td>51</td>
    <td>10</td>
    <td>25</td>
  </tr>
  <tr>
    <th>I</th>
    <th>J</th>
    <th>K</th>
    <th>L</th>
    <th>M</th>
    <th>N</th>
    <th>O</th>
    <th>P</th>
  </tr>
  <tr>
    <td>10</td>
    <td>9</td>
    <td>3</td>
    <td>10</td>
    <td>0</td>
    <td>1</td>
    <td>15</td>
    <td>28</td>
  </tr>
  <tr>
    <th>Q</th>
    <th>R</th>
    <th>S</th>
    <th>T</th>
    <th>U</th>
    <th>V</th>
    <th>W</th>
    <th>X</th>
  </tr>
  <tr>
    <td>42</td>
    <td>0</td>
    <td>0</td>
    <td>27</td>
    <td>4</td>
    <td>24</td>
    <td>22</td>
    <td>28</td>
  </tr>
  <tr>
    <th>Y</th>
    <th>Z</th>
  </tr>
  <tr>
    <td>6</td>
    <td>8</td>
  </tr>
</table>

1:1 대치로 생성된 암호문의 문자들이 이 표와 같은 통계를 보인다면, 알파벳의 전반적인 등장 비율에 맞춰 텍스트를 추정할 수 있다.  

![](/static/posts/2026-09-17-cryptography/replace-cipher-english.png)  

<br />

이와 같이 암호문으로부터 평문을 추정할 수 있는 방법이 별도로 존재한다면, Cryptosystem의 알고리즘이 얼마나 복잡한지와는 무관하게, 평문을 확인할 수 있다.  

따라서 어떤 Cryptosystem이 안전하다고 서술하는 것은, 부채널 공격이 불가능하여 완전 탐색만 가능한 것과 같다. 이 경우에는 키 사이즈, 발생 가능한 키의 경우의 수만 늘리면 더욱 안전해질 수 있다.  

### Vigenere Cipher

위와 같은 Monoalphabetic(=1:1 대치) 방법을 사용하지 않고 $N$ 개씩 묶어 $M$ 개 길이의 문자열로 대치한다면 위의 빈도수 공격, 통계적 접근에 강한 문자를 만들 수 있다.  

예를 들어, 알파벳을 3개씩 묶어 암호화하면 키는 ${_{26}\mathrm{P}_3}$ 개의 표현자로 구성된다.  

<br />

Vigenere Cipher에서는 카이사르 암호의 변형으로, 문자열(혹은 어떠한 값 배열)을 키로 사용해, 빈도수 공격을 완화한다.  

- 키(Keyword) = `CAT`
- 평문 = `attackatdawn`

과 같은 상황일 때 키와 평문을 다음과 같이 shift할 수 있다.

<table>
  <tr>
    <th>a</th>
    <th>t</th>
    <th>t</th>
    <th>a</th>
    <th>c</th>
    <th>k</th>
  </tr>
  <tr>
    <td colspan="6">C (3만큼 shift)</td>
  </tr>
  <tr>
    <td>d</td>
    <td>w</td>
    <td>w</td>
    <td>d</td>
    <td>f</td>
    <td>n</td>
  </tr>
  <tr></tr>
  <tr>
    <th>a</th>
    <th>t</th>
    <th>d</th>
    <th>a</th>
    <th>w</th>
    <th>n</th>
  </tr>
  <tr>
    <td>C</td>
    <td>A</td>
    <td>T</td>
    <td>C</td>
    <td>A</td>
    <td>T</td>
  </tr>
  <tr>
    <td>d</td>
    <td>t</td>
    <td>w</td>
    <td>d</td>
    <td>w</td>
    <td>g</td>
  </tr>
</table>


이 암호는 키를 반복해 사용하는 특성이 있으므로, 키의 길이 $N$ 에 대해서, 같은 변화 패턴을 보이는 $N$ 을 찾는 것으로 공격할 수 있다.  

- len(key) = 1 일 때, 변화 양상이 같은가?
- len(key) = 2 일 때, 변화 양상이 같은가?
- len(key) = 3 일 때, 변화 양상이 같은가?
- ...

우선 암호문에서 같은 문자열이 반복해서 나타나는 위치를 찾고, 그 위치 사이의 거리의 약수를 키 길이 후보로 삼는다. 예를 들어 같은 패턴이 12글자 간격으로 반복된다면 $N=1, 2, 3, 4, 6, 12$ 등을 후보로 볼 수 있다.

각 후보 $N$ 에 대해서는 암호문을 다음처럼 $N$ 개의 그룹으로 나눈다. 첫 번째 그룹은 1, $N+1$, $2N+1$, ... 번째 문자로, 두 번째 그룹은 2, $N+2$, $2N+2$, ... 번째 문자로 구성한다. 같은 그룹에 속한 문자들은 키의 같은 문자로 shift되므로, 각 그룹은 하나의 카이사르 암호처럼 분석할 수 있다.

### Double Transposition

Double Transposition은 문자를 치환하지 않고 위치만 두 번 재배열하는 방법이다. 먼저 평문을 정해진 열 수의 표에 행 방향으로 채운 뒤, 첫 번째 키에 따라 열의 순서를 바꾸고 열 방향으로 읽어 중간 암호문을 만든다. 그런 다음 중간 암호문을 다시 표에 채우고, 두 번째 키에 따라 행 또는 열의 순서를 바꿔 최종 암호문을 얻는다.  

<br />

평문 `MEETMEATNOON`에 대해, 두 키 `3, 1, 4, 2`, `2, 4, 1, 3`에 대해 다음과 같이 처리할 수 있다.  

평문을 3행 4열의 표에 행 방향으로 채운다. 첫 번째 키가 지정한 열 읽기 순서대로 각 열을 위에서 아래로 읽어 `EAO`, `MMN`, `TTN`, `EEO`를 얻는다. 이를 이어 붙인 중간 문자열은 `EAOMMNTTNEEO`가 된다.

<table>
  <tr>
    <td>M</td>
    <td>E</td>
    <td>E</td>
    <td>T</td>
  </tr>
  <tr>
    <td>M</td>
    <td>E</td>
    <td>A</td>
    <td>T</td>
  </tr>
  <tr>
    <td>N</td>
    <td>O</td>
    <td>O</td>
    <td>N</td>
  </tr>
</table>

첫 번째 열 읽기 순서: 3 → 1 → 4 → 2

<table>
  <tr>
    <td>E</td>
    <td>A</td>
    <td>O</td>
    <td>M</td>
  </tr>
  <tr>
    <td>M</td>
    <td>N</td>
    <td>T</td>
    <td>T</td>
  </tr>
  <tr>
    <td>N</td>
    <td>E</td>
    <td>E</td>
    <td>O</td>
  </tr>
</table>

중간 문자열을 다시 표에 채운 뒤, 두 번째 키의 열 읽기 순서 2, 4, 1, 3을 적용한다. 각 열에서 `ANE`, `MTO`, `EMN`, `OTE`를 얻으므로 최종 암호문은 `ANEMTOEMNOTE`가 된다.

두 번째 열 읽기 순서: 2 → 4 → 1 → 3

각 전치 단계에서는 문자의 종류와 등장 횟수가 바뀌지 않으므로 단일 전치만으로는 영어의 문자 빈도 자체를 숨길 수 없다. 그러나 문자의 위치 관계와 단어의 연속성이 두 번 섞이기 때문에, 빈도를 세는 방식으로는 평문을 복원하기 어렵다. 공격자는 반복되는 문자열, 문자의 위치, 가능한 표의 크기와 두 키의 순서를 함께 추정해야 한다.  

Double Transposition은 같은 전치 키를 두 번 적용하는 것보다 서로 다른 키를 사용하는 편이 안전하다. 다만 전치 과정에서 문자가 바뀌지 않으므로 충분히 긴 암호문이 주어지면 언어의 통계적 특성이나 반복 패턴이 여전히 유효한 단서로써 활용될 수 있다.  

### One-time Pad

One-time Pad는 cipher text만으로는 평문을 유추할 수 없고, 키 소유자만 이해 가능하도록 설계된 암호화 방식이다. pad 키는 랜덤 전환되어야 하고, 한번만 쓰여야 한다. 또 pad 길이는 메시지 길이와 동일하다.  

이 방법에서는 평문을 키와 XOR 연산하여 암호문을 생성한다.  

$$
\text{Ciphertext} = \text{Plaintext} \oplus \text{Key}
$$

<br />

<table>
  <tr>
    <th>e</th>
    <td>000</td>
    <th>h</th>
    <td>001</td>
    <th>i</th>
    <td>010</td>
    <th>k</th>
    <td>011</td>
  </tr>
  <tr>
    <th>l</th>
    <td>100</td>
    <th>r</th>
    <td>101</td>
    <th>s</th>
    <td>110</td>
    <th>t</th>
    <td>111</td>
  </tr>
</table>

위와 같이 부호화된 텍스트에 대해, 다음과 같이 랜덤하게 생성된 키를 XOR 연산하여 암호문을 생성한다.  

- Plaintext: `heilhitler`
- Key: `trsrtlerse`

<table style="text-align: center;">
  <tr>
    <th>origin</th>
    <td>h<br />001</td>
    <td>e<br />000</td>
    <td>i<br />010</td>
    <td>l<br />100</td>
    <td>h<br />001</td>
    <td>i<br />010</td>
    <td>t<br />111</td>
    <td>l<br />100</td>
    <td>e<br />000</td>
    <td>r<br />101</td>
  </tr>
  <tr>
    <th>key</th>
    <td>t<br />111</td>
    <td>r<br />101</td>
    <td>s<br />110</td>
    <td>r<br />101</td>
    <td>t<br />111</td>
    <td>l<br />100</td>
    <td>e<br />000</td>
    <td>r<br />101</td>
    <td>s<br />110</td>
    <td>e<br />000</td>
  </tr>
  <tr>
    <th>⊕</th>
    <td>s<br />110</td>
    <td>r<br />101</td>
    <td>l<br />100</td>
    <td>h<br />001</td>
    <td>s<br />110</td>
    <td>s<br />110</td>
    <td>t<br />111</td>
    <td>h<br />001</td>
    <td>s<br />110</td>
    <td>r<br />101</td>
  </tr>
</table>

키가 정확하지 않으면 원래의 평문과는 완전히 다른 텍스트를 획득할 수 있다.  

<table style="text-align: center;">
  <tr>
    <th>cipher</th>
    <td>s<br />110</td>
    <td>r<br />101</td>
    <td>l<br />100</td>
    <td>h<br />001</td>
    <td>s<br />110</td>
    <td>s<br />110</td>
    <td>t<br />111</td>
    <td>h<br />001</td>
    <td>s<br />110</td>
    <td>r<br />101</td>
  </tr>
  <tr>
    <th>try</th>
    <td>r<br />101</td>
    <td>t<br />111</td>
    <td>e<br />000</td>
    <td>r<br />101</td>
    <td>t<br />111</td>
    <td>l<br />100</td>
    <td>e<br />000</td>
    <td>r<br />101</td>
    <td>s<br />110</td>
    <td>e<br />000</td>
  </tr>
  <tr>
    <th>⊕</th>
    <td>k<br />011</td>
    <td>i<br />010</td>
    <td>l<br />100</td>
    <td>l<br />100</td>
    <td>h<br />001</td>
    <td>i<br />010</td>
    <td>t<br />111</td>
    <td>l<br />100</td>
    <td>e<br />000</td>
    <td>r<br />101</td>
</table>

<br />

이 방법은 수학적으로 완벽하게 안전한 방법으로 증명되었다. 하지만 메시지와 동일한 길이의 키를 안전하게 전달할 경로가 있다면, 오히려 그 경로로 키가 아니라 평문을 전달하더라도 문제가 없을 것이므로 실제의 효용은 떨어진다.  

One-time Pad가 실제로 사용된 사례 Project VENONA에서는 소련의 스파이가 핵개발 정보를 수천회 빼돌리는데 One-time Pad가 사용되었는데, 하나의 키를 갱신 없이 재사용한 것 때문에 발각되었다.  

### Codebook Cipher

One-time Pad와 유사하게 양 측이 동일한 데이터를 사전에 공유해두어야 하는 방식으로 Codebook Cipher 방법도 있다. 이 방법은 $\text{Plaintext} \to \text{Ciphertext}$ 의 대응을 사전에 정의해두고, 평문이 주어지면 대응되는 암호문을 찾아 전송하는 방식이다.  

이 방법은 주로 단어를 바꾸는 방식으로 사용되었기 때문에, 평문과 암호문의 길이가 동일하지 않고, 통계적 접근이 통하지 않는다.  

하지만 사전에 정의된 대응표(codebook)가 유출되면, 평문이 모두 노출되므로 안전하지 않았다. 보완책으로 코드북을 두 개 두고 한 개는 평문을 암호문으로, 다른 한 개는 이 암호문의 값을 다시 한번 수정하는 데 사용하여, 코드북이 둘 다 유출되어야만 평문이 노출되도록 하는 방법도 사용되었다. (Additive 방법) 다만 이 경우에도 근본적인 문제가 해결된 것은 아니었다.  

## 혼동과 확산

이들 사례에서 보듯, 암호화 알고리즘은 알고리즘 그 자체의 수학적인 복잡성만으로는 안전성을 확보할 수 없다. Claude Shannon은 이를 두고 암호화 알고리즘은 혼동(Confusion)과 확산(Diffusion)을 기본 원리로 삼아야 한다고 주장하였다.

- 혼동(Confusion): 원문과 암호문은 서로 관계가 없음
- 확산(Diffusion): 원문의 통계적 특징을 암호문 전체로 분산시켜 암호문에 드러나지 않도록 함

앞에서 혼동을 잘 구현하더라도 부채널 공격에 의해 평문을 추정할 수 있다면 안전하지 않은 사례를 살펴보았고, 역으로 확산이 잘 구현되었음에도 다양한 방법으로 잠재적으로 안전하지 않은 사례도 살펴보았다.  

혼동과 확산은 암호화 설계에 있어 기본적이면서 중요한 원칙이다. 오늘날에도 이 원리를 근거로 암호화 알고리즘을 설계하고 있다.  
