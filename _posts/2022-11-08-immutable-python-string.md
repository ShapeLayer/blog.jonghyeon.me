---
layout: post
title: 파이썬 문자열 타입의 불변 특성
date: '2022-11-08'
categories: [language, python]
tags: [python, computer-science]
---

파이썬의 문자열 타입은 유동적이고 유연하다.  

```py
>>> string = 'foo'
>>> string += '_bar'
>>> string[0]
'f'
>>> string[0:3]
'foo'
```

이러한 특징들은 파이썬 학습자들로 하여금 문자열 타입이 정말로 가변적이고 유동적이라는 인식을 갖게 만든다. 하지만 이 인식은 많은 이들이 문자열을 다루면서 공통적인 실수를 범하게 하는 계기로서 작용한다.  

```py
>>> string[0] = 'p'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

파이썬 학습자가 많이 겪는 문제 상황 중 하나는 위 코드가 왜 오류가 나는지 모르겠다는 것이다.  

하지만 당연하게도 오류가 발생한다. 파이썬의 문자열 타입은 불변(Immutable)하기 때문이다.  

## 문자열의 불변 특성을 가리는 문법적 설탕

파이썬의 문자열 타입은 불변이지만, 학습 과정에서 그 사실을 깨닫는 경우는 많지 않다. 

이 점에서 보았을 때, 파이썬의 문자열 부분 문법적 설탕은 성공적이다. 실제로 문자열을 어느정도 가변적으로 다룰 수 있고 많은 이들이 문자열은 가변적인 타입이라고 생각하고 있기 때문이다.  

```py
>>> foo = 'bar'
>>> foo += ' bar'
>>> foo
'bar bar'
```

<br />

파이썬은 `id()`를 이용해, 어떤 값을 식별하는데 이용하는 해시를 사용자 측에서 확인할 수 있도록 하고 있다.  

```py
>>> arr = [0]
>>> brr = arr
>>> id(arr)
140532569057152
>>> id(brr)
140532569057152
```

위 코드에서 `brr` 변수는 `brr = arr` 시점에서 메모리 상의 `arr`의 값을 가리키게 되었다. 다시 말해 `arr`과 `brr`은 메모리 상의 동일한 주소를 가리킨다. 조금 더 나아간 표현으로 같은 값을 "참조"하고 있다.  

다른 표현으로 메모리 상 `[0]`이라는 데이터가 위치하고 있는 공간에 대해 `arr`, `brr`라는 별명이 붙은 것이다. ID가 같다면 같은 객체이다.  

이 코드에서 `arr`과 `brr`이 같은 값을 참조하므로 다음과 같이 작동할 수 있다.  

```py
>>> arr.append(1)
>>> brr
[0, 1]
```

`arr`과 `brr`은 같은 것을 의미하므로 `arr` 값을 변경한다는 것은 곧 `brr` 값을 변경하는 것과 같다.  

<br />

하지만 문자열 타입은 상황이 조금 다르다.  

```py
>>> foo = 'foo'
>>> id(foo)
139746962569456
>>> foo += ' bar'
>>> id(foo)
139746962569776
```

`foo` 변수가 연산을 거치니 ID가 변경되었다.  

파이썬은 문자열 연산을 시행할 때 `'foo bar'`라는 새로운 값을 메모리에 추가한 뒤, 기존의 `'foo'` 값을 메모리에서 삭제하고 메모리 상의 `'foo bar'`를 `foo` 변수에 연결했다.  

즉, `foo = 'foo'`의 `foo`와 `foo += 'bar'`의 `foo`는 본질적으로 다른 객체가 되었다.  

<br />

```c
#include <stdio.h>

int main()
{
    char foo[10] = "foo\0";
    printf("%s\n", foo);
    foo[3] = ' ', foo[4] = 'b', foo[5] = 'a', foo[6] = 'r', foo[7] = '\0';
    printf("%s\n", foo);
    
    return 0;
}
```
```
foo
foo bar
```

물론 실제로는 위와 같이 작성할 일은 없겠지만, 위의 C 코드와 비교했을 때 파이썬 문자열의 불변 문자열 특성은 더 두드러진다.  

C의 문자열은 `char` 형의 배열의 불과하므로 사전에 선언한 배열 크기에만 벗어나지 않는다면 어떻게 수정을 가하더라도 본질적으로는 같은 데이터, 같은 참조이다.  

하지만 파이썬은 어떻게 수정을 가하던 본질적으로 새로 생성된 데이터이므로 같은 참조일 수 없다.  

## 다량의 문자열 합성이 필요하다면 연산 횟수를 줄여라

방금 보았듯 문자열 연산은 메모리 할당과 해제를 연달아 수행하므로, 러닝 타임을 빡빡하게 가져가야한다면 문자열 연산 횟수를 줄이는 것이 좋다.  

실제로 문자열 연산이 수 없이 많이 필요한 경우, 리스트를 활용하여 문자열 연산 횟수를 줄이는 것이 성과를 거둘 수 있음을 확인할 수 있다.  

```py
from time import time

def merge_using_string_operation():
    string = ''
    start = time()
    for _i in range(100000):
        string += 'string '
    end = time()
    return end - start

def merge_using_list_append():
    string = ''
    start = time()
    string_buf = []
    for _i in range(100000):
        string_buf.append('string ')
    string = ''.join(string_buf)
    end = time()
    return end - start

if __name__ == '__main__':
    print(f'merge_using_string_operation: {merge_using_string_operation()}')
    print(f'merge_using_list_append:      {merge_using_list_append()}')
```

```
$ python3 string.py 
merge_using_string_operation: 0.008493185043334961
merge_using_list_append:      0.00702214241027832
```

\* _이 코드는 Github Codespaces의 4코어/8GB 메모리 환경에서 CPython 3.10.4로 실행했다._  

_검증되진 않았지만 버전에 따라 10배의 성능 차이가 난다는 언급도 있어 Faster CPython 이전의 버전에서는 더욱 유의미한 차이가 발생할 수도 있다._  

### 참고: 리스트 연산자로 문자열 합성을 시도하지 마세요.

아래 코드는 위에서 제시한 `merge_using_list_append` 함수와 리스트 병합 방식만 다르다.  
 * `merge_using_list_append`:    `string_buf.append('string ')`
 * `merge_using_list_operation`: `string_buf += ['string ']`

```py
def merge_using_list_operation():
    string = ''
    start = time()
    string_buf = []
    for _i in range(100000):
        string_buf += ['string ']
    string = ''.join(string_buf)
    end = time()
    return end - start

if __name__ == '__main__':
    print(f'merge_using_string_operation: {merge_using_string_operation()}')
    print(f'merge_using_list_append:      {merge_using_list_append()}')
    print(f'merge_using_list_operation:   {merge_using_list_operation()}')
```

하지만 새 `merge_using_list_operation` 함수는 리스트 병합 과정에서 불필요한 박싱을 거친다. 그 결과 문자열 연산보다 긴 러닝타임이 측정되었다.  

```
$ python3 string.py 
merge_using_string_operation: 0.008493185043334961
merge_using_list_append:      0.00702214241027832
merge_using_list_operation:   0.009548664093017578
```

* [테스트 코드](https://github.com/ShapeLayer/blog.jonghyeon.me/blob/main/static/posts/2022-11-08-immutable-python-string/string.py)  
