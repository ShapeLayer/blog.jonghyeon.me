---
layout: post
title: 파이썬의 이터레이터
date: '2022-04-12'
categories: [language, python]
tags: [python, computer-science]
---

이터레이터(Iterator)를 직역하면 반복자입니다. 그리고 이 이터레이터를 보통 이터레이블(Iterable)하다, 즉 반복가능하다고 합니다. 대체 뭐가 반복자이고 반복가능하다는걸까요?


## for문 곱씹어보기

```python
for i in range(5):
  print(i)
# 0
# 1
# 2
# 3
# 4
```

가장 기본적인 형태의 for문을 살펴봅시다. 이 경우 파이썬은 콘솔에 `0`부터 `4`까지를 출력한 후 종료됩니다.  
`for` 문 안에 `i`라는 변수가 임시로 생성되고, 이 `i`는 한번 반복할때마다 차례대로 `0` `1` `2` `3` `4` 로 갱신이 되는거죠.

```python
arr = [10, 3, 4, 5, 7]
for i in arr:
  print(i)
# 10
# 3
# 4
# 5
# 7
```

어떤 교수님은 이러한 형태의 `for` 문도 가르치십니다.  
이 경우 `i` 는 한번 반복할때마다 `10` `3` `4` `5` `7` 을 의미하게 되어서 그대로 출력됩니다.

## range()와 리스트

위 두 사례는 `for i in` 부분까지는 똑같지만 그 뒤 부분에서 차이를 보이고 있습니다. 이것도 그냥 단순 암기해야하는 문법일까요?

```python
print(list(range(5)))
# [0, 1, 2, 3, 4]

list(range(5)) == [0, 1, 2, 3, 4]
# True
```

괄호 단위로 끊어 읽어봅시다. `range(5)` 를 `list()` 를 사용해서 리스트로 변형했습니다. `print()`는 콘솔에 결과를 출력하는 것 뿐이니, `list(range(5))` 가 `[0, 1, 2, 3, 4]` 임을 알 수 있습니다.

실제로 파이썬에 리스트로 변환한 `range(5)`와 그냥 리스트를 비교하니 둘을 똑같이 인식함을 확인할 수 있습니다.

그럼 이제 for문의 사용법이 두 가지가 아님을 알 수 있습니다.

```python
for i in range(5):
	# code
for i in [0, 1, 2, 3, 4]:
  # code
```

이 두 for문은 사실상 같은 내용을 의미합니다. `range(5)` 가 0~4를 담는 리스트를 자동 생성하는 것이라고 생각해도 될 정도로 말입니다.  

## 다시 이터레이터로 돌아와서

글머리에 이터레이터를 "반복자" "반복 가능한 데이터"라고 표현했습니다. 이제 for문을 통해 다시 한번 확인해봅시다.

```python
sums = 0
for n in [10, 9, 8, 7, 6, 5]:
  sums += n
# sums = 10 + 9 + 8 + 7 + 6 + 5
```

`for <var> in <iter>` 의 `<iter>` 부분에는 리스트와, `list()` 를 통해 리스트가 될 수 있는 `range()` 가 들어갔습니다. 이들의 특징은 "하나의 변수에 여러 값을 한번에 넣을 수 있다"입니다.  

그렇다면 위 특징에 해당하는 다른 타입들을 떠올려봅시다.  

```python
tup = (1, 2, 3, 4, 5)
for t in tup:
  print(t)
# 1
# 2
# 3
# 4
# 5
```

```python
dic = {'name': '문성수', 'high_school': '숭덕고등학교', 'university': '전남대학교'}
for key in dic:
  print(key, dic[key])
# name 문성수
# high_school 숭덕고등학교
# university 전남대학교
```

네 맞습니다. 위 예시는 모두 이터레이터입니다.  

다시한번, **이터레이터는 for문의 `in` 다음에 배치해서 사용할 수 있습니다.**  
동시에, `for` 와 `in` 사이에 배치한 변수(위 경우에는 `t` 와`key`)가 **반복을 거듭하면서 계속 다른 값을 가져올 수 있습니다.**  

딕셔너리는 리스트가 두개 만들어질 수 있습니다. 키(Key) 리스트와 값(Value) 리스트입니다.  

하지만 반복문은 지금까지 `list()` 를 한번 거친 값을 사용하는 경향을 보였습니다. 따라서 딕셔너리 역시 그렇게 처리될 것입니다.  

```python
list(dic)
# 딕셔너리를 리스트로 변환했는데도 오류없이 잘 처리됩니다.
# ['name', 'high_school', 'university']
```

딕셔너리 역시 마찬가지로 `list()` 를 한번 거친 값이 for문에 활용됩니다. `list()`를 한번 거치니 키값이 나타나는 것을 확인할 수 있습니다.

여기서 자연스럽게 넘어갔는데, 딕셔너리를 리스트로 변환했는데 오류없이 잘 처리되었습니다.  
이를 통해 한 가지를 더 확인할 수 있습니다. 바로 이터레이터는 `list()` 를 거쳐도 오류 없이 잘 처리된다는 것입니다.  


## 인덱싱과 슬라이싱

이터레이터의 특징 중 "하나의 변수에 여러가지 값을 담을 수 있다."를 떠올려봅시다.  
이터레이터는 여러 개의 값을 하나로 묶은 것입니다. 때문에 원래의 값을 사용하려면 인덱싱과 슬라이싱을 사용해야 했습니다.  

```python
(1, 2, 3, 4, 5)[3] # 3번 인덱싱
# 4
{'name': '박종현', 'high_school': '숭덕고등학교', 'university': '전남대학교'}['name'] # 'name' 키 인덱싱
# 박종현
[10, 5, 3, 4, 1][2:4] # 2~3 슬라이싱
# [3, 4]
```

그런데 우리는 인덱싱과 슬라이싱이 되는 데이터타입을 하나 더 압니다. 바로 문자열(String)입니다.  

```python
text = '다람쥐 헌 쳇바퀴에 타고파.'
text[2]
# '쥐'
text[::-1]
# '.파고타 에퀴바쳇 헌 쥐람다'
text[-1]
# '.'
```

사실 문자열을 문장이라 하지 않고 "문자열"이라고 표현한 것은 컴퓨터가 이걸 "문자"들의 "배열"(=리스트)로 처리하고 있기 때문입니다.  

C언어를 학습했다면 다음 코드를 바로 떠올릴 것입니다.  
```c
char foo[10] = "foo\0";
```

파이썬 역시 비슷하게 처리하므로 우리는 문자열을 인덱싱, 슬라이싱할 수 있습니다.  

문자열을 문자들의 "리스트"로 생각하고 처리하고 있으므로 아예 문자 리스트로 변환할 수도 있습니다.

```python
list('다람쥐 헌 쳇바퀴에 타고파')
# ['다', '람', '쥐', ' ', '헌', ' ', '쳇', '바', '퀴', '에', ' ', '타', '고', '파', '.']
```

사실 문자열은 이터레이터입니다. 그리고 for문에 넣어도 오류 없이 동작합니다.  

```python
for alphabet in 'apple':
  print(alphabet)
# a
# p
# p
# l
# e
```

그렇다면 이제 인덱싱과 슬라이싱도 문자열, 리스트 각각 따로 생각할 필요가 없습니다.  
애초에 둘 다 똑같은 이터레이터이므로 똑같이 처리되는건 당연합니다.  

```python
'다람쥐 헌 쳇바퀴에 타고파.'[0:3]
# '다람쥐'

['다', '람', '쥐', ' ', '헌', ' ', '쳇', '바', '퀴', '에', ' ', '타', '고', '파', '.'][0:3]
# ['다', '람', '쥐']
```

## 되짚어보기

지금까지 언급한 이터레이터의 특징을 요약하면 이렇습니다.

- 하나의 변수에 여러가지 값을 담을 수 있다.
- 반복문(for문)에 사용할 수 있다.
- for문을 사용하면 반복할 때마다 임시로 선언한 변수의 값이 바뀐다. (`for i in range()` 의 `i` 가 계속 바뀐다.)
    
    = 이터레이터는 for문의 `for <var> in <iter>` 의 `<iter>` 부분에 들어갈 수 있고, `<var>` 는 반복할 때 마다 이터레이터 속 값을 하나씩 꺼낸다.
    
- 인덱싱이 가능하다: `[1]`
  (슬라이싱은 모든 이터레이터가 되는 것이 아닙니다: `[:2]` `[::-1]`)
- `list()` 를 오류 없이 통과한다.
- 대표 타입: 리스트, 문자열, 튜플, 딕셔너리, 레인지(`range`)
