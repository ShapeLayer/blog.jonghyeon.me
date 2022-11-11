---
layout: post
title: 파이썬 문자열 타입의 불변 특성
date: '2022-11-08'
categories: [language, python]
tags: [python, computer-science]
---

파이썬의 문자열 타입은 유동적이고 유연한 것처럼 보입니다. 실제로 파이썬의 문자열 타입은 강력하고 좋은, 많은 기능들을 제공합니다.  

```py
>>> string = 'foo'
>>> string += '_bar'
>>> string[0]
'f'
>>> string[0:3]
'foo'
```

이러한 특징들은 파이썬 학습자들로 하여금 문자열 타입이 정말로 가변적이고 유동적이라는 인식을 갖게 만들어줍니다.  

하지만 이 인식은 많은 이들이 문자열을 다루면서 공통적인 실수를 범하게 하는 계기가 되었습니다.  

```py
>>> string[0] = 'p'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

제가 주변에 파이썬을 가르칠 때, 가장 많이 받는 질문 중 하나는 위 코드가 왜 오류가 나는지 모르겠다는 것입니다.  

원인은 간단합니다. 파이썬의 문자열 타입은 불변(Immutable)하기 때문입니다.  

## 문자열의 불변 특성을 가리는 문법적 설탕

파이썬의 문자열 타입은 불변이지만, 학습 과정에서 그 사실을 깨닫는 경우는 많지 않습니다. 실제로 위 오류를 맞닥뜨려도, 단순히 해결책만 찾아보고 넘어가는게 다반사입니다.  

문자열이 불변하다는 사실 자체는 실제로 그렇게 중요하지 않을 수도 있고, 이를 모른다고 해서 파이썬 코드를 짜지 못하는 것은 아닙니다.  

이 점에서 보았을 때, 아래와 같은 문법적 설탕은 성공적인 셈입니다.  
실제로 문자열을 어느정도 가변적으로 다룰 수 있고 많은 이들이 문자열은 가변적인 타입이라고 생각하니 말입니다.  

```py
>>> foo = 'bar'
>>> foo += ' bar'
>>> foo
'bar bar'
```

하지만 문자열이 실제로 불변적이라는걸 어떻게 알 수 있을까요?  

파이썬은 어떤 값을 식별하는데 이용하는 해시를 파이썬 사용자가 확인할 수 있도록 해주었습니다. 바로 `id()` 함수입니다.  

```py
>>> arr = [0]
>>> brr = arr
>>> id(arr)
140532569057152
>>> id(brr)
140532569057152
```

위 코드에서 `brr` 변수는 `brr = arr` 시점에서 메모리 상의 `arr`의 값을 가리키게 되었습니다.  
다시 말해 `arr`과 `brr`은 메모리 상의 동일한 주소를 가리킵니다. 조금 더 나아간 표현으로 같은 값을 **"참조"하고 있습니다.**  

이해하기 유용한 표현으로 메모리 상의 `[0]`이라는 데이터에 대해 `arr`, `brr`라는 태그가 붙은 것입니다.  
즉, ID가 같다면 같은 객체임을 의미합니다.  

위 예제에서 `arr`과 `brr`이 같은 값을 참조하므로 다음과 같이 작동할 수 있습니다.  

```py
>>> arr.append(1)
>>> brr
[0, 1]
```

`arr`과 `brr`은 같은 것을 의미하므로 `arr` 값을 변경한다는 것은 곧 `brr` 값을 변경하는 것과 같습니다.  

하지만 문자열 타입의 경우 상황이 조금 다릅니다.  

```py
>>> foo = 'foo'
>>> id(foo)
139746962569456
>>> foo += ' bar'
>>> id(foo)
139746962569776
```

`foo` 변수가 연산을 거치니 ID가 변경되었습니다.  

파이썬은 문자열 연산을 시행할 때 `'foo bar'`라는 새로운 값을 메모리에 추가한 뒤, 기존의 `'foo'` 값을 메모리에서 삭제하고 메모리 상의 `'foo bar'`를 `foo` 변수에 연결한 것입니다.  

즉, `foo = 'foo'`의 `foo`와 `foo += 'bar'`의 `foo`는 본질적으로 다른 객체입니다.  

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

물론 위와 같은 코드를 작성할 일은 없겠지만, 위의 C 코드와 비교했을 때 파이썬 문자열의 불변 문자열 특성은 더 두드러집니다.  

C의 문자열은 `char` 형의 배열의 불과하므로 사전에 선언한 배열 크기에만 벗어나지 않는다면 어떻게 수정을 가하더라도 "본질적으로" 같은 데이터, 같은 참조에 해당합니다.  

하지만 파이썬은 어떻게 수정을 가하던 본질적으로 새로 생성된 데이터이므로 같은 참조일 수 없는 것입니다.  

이로 미루어보아 파이썬의 문자열 타입은 훌륭한 문법적 설탕을 가지고 있는 셈입니다.  

## 다량의 문자열 합성이 필요하다면 연산 횟수를 줄여라

방금 보았듯 문자열 연산은 메모리 할당과 해제를 연달아 수행하므로, 러닝 타임을 빡빡하게 가져가야한다면 문자열 연산 횟수를 줄이는 것이 좋습니다.  

실제로 문자열 연산이 수 없이 많이 필요한 경우, 리스트를 활용하여 문자열 연산 횟수를 줄이는 것이 성과를 거둘 수 있음을 확인할 수 있었습니다.  

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

이 코드는 Github Codespaces의 4코어/8GB 메모리 환경에서 CPython 3.10.4로 실행하였습니다.  

검증되진 않았지만 버전에 따라 10배의 성능 차이가 난다는 언급도 있어 Faster CPython 이전의 버전에서는 유의미한 차이가 발생할 수도 있습니다.  

### 참고: 리스트 연산자로 문자열 합성을 시도하지 마세요.

테스트 코드를 작성하며 리스트 연산자로 문자열 합성을 시도해기도 했습니다.  

아래 코드는 위에서 제시한 `merge_using_list_append` 함수와 리스트 병합 방식만 다릅니다.  
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

이 함수는 리스트 병합 과정에서 불필요한 박싱을 거칩니다.  

그 결과 문자열 연산보다 긴 러닝타임이 측정되었습니다.  

```
$ python3 string.py 
merge_using_string_operation: 0.008493185043334961
merge_using_list_append:      0.00702214241027832
merge_using_list_operation:   0.009548664093017578
```

* 테스트 과정에서 사용한 코드는 리포지토리에 첨부하였습니다. [이곳에서 확인할 수 있습니다.](https://github.com/ShapeLayer/blog.jonghyeon.me/blob/main/static/posts/2022-11-08-immutable-python-string/string.py)  

## 문자열 불변 특성을 이용한 CPython의 최적화 기법

문자열이 불변하니 아래와 같은 일도 가능하게 됩니다.  

```py
>>> foo = 'foo'
>>> bar = 'foo'
>>> id(foo)
139746962569456
>>> id(bar)
139746962569456
```

`foo` 변수와 `bar` 변수에 각각 `'foo'` 값을 할당했는데, ID를 확인하니 두 변수는 메모리 상에서 같은 값을 가리키고 있습니다.  

즉, 메모리에 올라간 `'foo'` 값의 별칭이 `foo` 변수와 `bar` 변수가 된것입니다.  

하지만 `foo` 변수를 변경했는데 `bar`변수가 함께 변경되는 상황은 발생하지 않습니다.  

```py
>>> foo = 'bar'
>>> bar
'foo'
```

`bar`는 여전히 `'foo'`를 담고 있습니다.  

```py
>>> id(foo)
139746962569840
>>> id(bar)
139746962569456
```

파이썬에서 문자열은 불변이고, 문자열을 변경할 때마다 메모리에 문자열 값을 다시 할당하므로 파이썬은 `'bar'`를 메모리에 할당하고 `foo` 변수만 새롭게 이 값을 바라보게 한 것입니다.  

그 어떤 수단으로 문자열을 변경하든 파이썬은 변경된 문자열을 메모리에 새로 할당할 뿐입니다. 아래 경우만 빼고 말입니다.  

```py
>>> foo[0] = 'p'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## 마무리

마지막으로 살펴본 CPython의 최적화 기법은 사실 문자열에만 쓰이는 것은 아닙니다.  

CPython은 정수 -5 ~ 256 값을 미리 메모리에 할당하므로 아래와 같은 값을 얻을 수 있습니다.  

```py
>>> a = 256
>>> b = 256
>>> id(a) == id(b)
True
>>> a = 257
>>> b = 257
>>> id(a) == id(b)
False
```

사실 위 사항을 모른다고 파이썬 코드를 작성하지 못하는 것은 아닙니다.  

하지만 잠재적으로 발생할 수 있는 버그를 막을 수 있고, 미래의 나에게 조금 더 많은 취침시간을 제공해줄지 모를 일입니다.  
