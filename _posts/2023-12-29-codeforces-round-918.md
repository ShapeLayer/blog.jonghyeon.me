---
layout: post
title: 코드포스, Round 918 (Div. 4) 돌아보기
date: '2023-12-29'
categories: [contest]
tags: [review, ps, codeforces]
---

![](/static/posts/2023-12-29-codeforces-round-918/스크린샷%202023-12-29%20082251.png)  

대회 할 때마다 느끼는건데, 빨리 풀어내야한다는 강박때문에 생각이 뚝뚝 끊기고 코드가 자연스럽게 짜이지 않는 것 같습니다.  

덕분인지 쉽게 풀 수 있을 문제도 여러번 틀렸습니다.  

대회가 익숙한 것도 아니고 PS 실력도 부족하니.. 억울한 결과는 아니라고 생각합니다.  

## A. Odd One Out

제시되는 세 개의 숫자 중 두 개는 중복입니다. 나머지 중복되지 않는 숫자 하나를 출력합니다.  

```py
for _i in range(int(input())):
  a, b, c = map(int, input().split())
  if a == b:
    print(c)
  if b == c:
    print(a)
  if c == a:
    print(b)
```

시작부터 급하게 짜느라 이렇게 짜서 내버렸습니다. 좀 더 좋은 코드가 있을텐데..  

## B. Not Quite Latin Square

입력에 `?`가 들어오는지 체크하고 `?`가 있는 줄에 `A`, `B`, `C` 중 무엇이 없는지 출력했습니다.  

급하게 대강 써서 넘기다가 몇번 틀렸습니다.  

## C. Can I Square?

수를 제곱근으로 나누고 소수점 아래를 버림한 뒤, 제곱해서 원래의 수와 차이가 있는지 체크했습니다.  

## D. Unnatural Language Processing

순차적으로 문자를 체크하면서 캐시 버퍼에 넣었다가, 문제가 제시하는 조건을 달성하게 되면 출력 버퍼로 옮겨두고 나중에 한 번에 출력했습니다.  

```py
while p < n:
  if gets[p] in 'bcd':
    cache.append(gets[p])
  else:
    if p < n - 2 and gets[p + 1] in 'bcd' and gets[p + 2] in 'bcd':
      cache.append(gets[p])
      cache.append(gets[p + 1])
      p += 1
    elif p == n - 2 and gets[p + 1] in 'bcd':
      cache.append(gets[p])
      cache.append(gets[p + 1])
      p += 1
    else:
      cache.append(gets[p])
    buf.append(''.join(cache))
    cache = []
  p += 1
```

이렇게 조건 분기가 까다롭지는 않아도 될 것 같은데, 마음이 다급해지니 조금 복잡하게 나왔습니다. 왠지 해킹당할 것 같은 느낌이 듭니다..  

## E. Romantic Glasses

최초 제출은 문제에서 구현하라는걸 그대로 구현하려고 했고, 당연히 TLE를 맞았습니다.  

이어서 누적합, 스위핑으로 풀이를 시도해봤습니다. 하지만 구현이 제대로 되지 않아서 결국 제출하지는 못했습니다.  

## F. Greetings

역시 최초 제출은 문제 구현을 그대로 따라가서 TLE를 맞았습니다.  

모두 속력과 방향이 일정한 점을 이용해 스위핑으로 풀 수 있겠다고 생각했지만, 뾰족한 풀이 없이 구현으로 들이박았다가 망해버려서 다음 시도를 제출하지 못했습니다.  

## G. Bicycles

개인적으로 좋아하는 분리집합 문제인줄 알아서 예시를 이리저리 뜯어보는데 아무리 봐도 입력과 출력이 제대로 맞지 않아서 번역기를 동원해가며 문제를 풀었습니다.  

영어 실력과 착각이 발목을 강하게 잡은 것 같습니다.  

이리 저리 경로 탐색을 넣어봤다가, 역시 구현이 제대로 되지 않아 제출조차 못했습니다.
