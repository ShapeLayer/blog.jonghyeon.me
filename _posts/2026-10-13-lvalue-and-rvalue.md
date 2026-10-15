---
layout: post
title: 'lvalue와 rvalue'
date: '2026-10-13'
categories: [cpp]
---

```cpp
int y;
1 = y;  // error
```

코딩 학원에서 학생들에게 프로그래밍을 가르치다보면, 학생들은 리터럴 값을 좌측에, 변수 선언을 우측에 배치하곤 한다.  

$$
1 = y
$$

방정식을 사용하면서 숫자 값이 식의 좌변에 위치하는 것이 익숙하지는 않더라도, 수학에서 좌우변의 위치는 큰 의미가 없다. 때문에 같은 행동을 코드 작성에서 반복하는 것이다. 하지만 코드 작성에서는 좌우변의 위치는 중요한 의미가 있고, 오류가 발생하므로, 항상 좌우변 위치를 맞추는 것을 잘 강조하는 수밖에 없다.  

## 일반론

### rvalue와 lvalue

lvalue는 어떤 메모리 위치를 가리킨다. 반면에 rvalue는 아무곳도 가리키지는 않는다. rvalue는 잠시 생성되며 짧은 수명 주기 동안 유효하다.  

```cpp
int x = 1;  // ok: x는 lvalue, 1은 rvalue
```

리터럴 상수 `1`은 rvalue이다. 특별한 메모리 주소가 존재하지는 않고, 프로그램이 동작하는 동안 즉석으로 레지스터에 값이 로드되어 사용될 뿐이다. 반면에 값이 할당되는 `x`는 변수이고, 특별한 메모리 공간을 가지고 있다.  

```cpp
int* y = &x;  // ok: x는 lvalue, &x는 rvalue
```

`x`의 메모리 주소를 `y`에 할당하는 것 역시 `&x` 연산의 결과로 rvalue가 생성되었으므로, 여전히 좌측 오퍼랜드에 lvalue, 우측 오퍼랜드에는 rvalue가 배치된다.  

`&` 연산자는 주소를 반환하므로, 주소 값을 가지고 있는 lvalue를 요구한다. rvalue는 메모리 주소를 가지고 있지 않으므로 `&` 연산을 적용할 수 없다.

```cpp
int* y = &1;  // error
```

clang:
```
error: cannot take the address of an rvalue of type 'int'
```

타입 `'int'`는 rvalue이고, 주소를 취할 수 없다.

### 함수의 반환값으로서 rvalue와 lvalue

할당 연산에서 왼쪽 오퍼랜드는 lvalue여야 했다. 따라서 다음과 같은 할당 연산도 유효하지 않다:

```cpp
int func() { return 1; }

func() = 0;  // error
```

`func()`는 임시 숫자 `1`을 반환한다. 즉 rvalue를 반환하므로 좌측 오퍼랜드에 배치될 수 없다. `func`가 메모리 공간을 가지고 있더라도, 그것은 `func`의 호출과 그 결과로서 반환되는 값이 메모리 공간을 가지는지와는 무관하다.  

```cpp
int var = -1;;

int& set_var() { return var; }

set_var() = 1;  // ok
```

하지만 이 코드에서 `set_var`의 호출을 할당 연산의 좌측 오퍼랜드에 배치하더라도 문제가 발생하지 않는다. `set_var`는 `var`에 대한 lvalue 참조를 반환하므로, 좌측 오퍼랜드에 배치될 수 있다. 이 사용법에서는 `var`의 값을 `1`로 변경한다.  

### lvalue to rvalue 변환

```cpp
int x = 1;
int y = 2;
int z = x + y;  // ok
```

`x`, `y`, `z`는 모두 lvalue이고, `+` 연산은 rvalue 두 개를 요구한다. 그렇다면 `x`와 `y`는 lvalue이므로 오류가 발생하여야 한다. 하지만 실제로는 문제가 발생하지 않았다. 이 코드에서 lvalue는 암시적으로 rvalue로 변환되었다.  

대부분의 경우 lvalue에서 rvalue로의 변환은 논리적으로 문제가 발생하지는 않는다. lvalue가 가리키는 메모리 공간의 값을 임시로 로드하는 것은 직접적이다. 따라서 rvalue를 요구하는 대개의 연산자는 lvalue의 암시적인 rvalue 변환을 지원한다.  

### lvalue 참조

하지만 역으로 rvalue는 lvalue로 변환될 수 없다. 모든 값은 광의의 메모리(메모리, 레지스터 등 어떠한 형태로든 데이터가 실재하는 공간)에 존재해야 하므로, 런타임에 모든 rvalue는 물리적으로 어떤 공간에 존재할 수 있다.  

하지만 rvalue의 주소를 획득한다고 하더라도 의미있지 않다. 그 누구도 런타임에 리터럴 상수가 계산되기 위해 일순간 로드된 레지스터의 주소를 유용하게 활용할 수 없다. 

```cpp
void fn(int& x) { }

int main() {
  int& yref = 0;
  fn(10);  // Nope!
}
```

```
error: non-const lvalue reference to type 'int' cannot bind to a temporary of type 'int'
```

`int& yref = 0`과 `fn(10)`은 모두 변수 선언을 거쳐 유의미한 메모리 공간을 가지는 과정이 동반되지 않았다. `0`과 `10`은 단지 어느 한 순간 레지스터에 잠시 설정되어 사용된다.  

```cpp
void fn(int& x) { }

int main() {
  int y;
  int& yref = y;  // ok

  int x = -1;
  fn(x);  // ok
}
```

### 상수 lvalue 참조

```
error: non-const lvalue reference to type 'int' cannot bind to a temporary of type 'int'
```

앞에서는 컴파일러가 `int`의 임시값을 바인딩할 수 없다고 했기 때문에, 값이 제대로 된 메모리 주소값을 가지도록 조정하여 컴파일 오류를 해결했다.  

하지만 컴파일러는 `int`의 임시값을 비상수(non-const) lvalue 참조에 바인딩할 수 없다고 했다. 그렇다면 상수 참조는 어떨까.

```cpp
const int& ref = 10;  // ok
```

```cpp
void fn(const int& x) { }
int main() {
  fn(10);  // ok
}
```

분명 리터럴 상수 `10`은 휘발적이다. 대신 값이 불변하므로, 컴파일러는 필요한 순간에 임시 메모리 공간을 생성하여 고정된 값을 메모리 공간에 할당할 수 있다.

```cpp
// the following...
const int& ref = 10;

// ... would translate to:
int __internal_unique_name = 10;
const int& ref = __internal_unique_name;
```

`ref`는 스코프를 벗어날 때까지 메모리 공간상에 실재한다.  

## C++ 11 이후

이후에는 이 분류가 조금 더 세분화되었다.  

![](/static/posts/2026-10-13-lvalue-and-rvalue/cpp17.jpg)  

표현식은 `glvalue`(Generalized L-Value)이거나 `rvalue`이다. `glvalue`는 `lvalue`이거나 `xvalue`(eXpiring value)이다. `rvalue`는 `prvalue`(pure rvalue)이거나 `xvalue`이다.  

- `glvalue`는 실제로 메모리 공간을 차지하고 있어, 어떠한 수단으로든 그 메모리 공간에 접근할 수 있는 표현식이다.
    - '메모리 공간에 접근할 수 있다'는 '식별자가 있다'고 표현한다.  
- `xvalue`는 "만료되어가는 값"으로, 식별자를 가지고 있으면서, 동시에 자원을 이동시킬 수 있는 표현식이다.  
- `prvalue`는 "순수한 rvalue"로, 식별자가 없다. 객체를 초기화하거나 오퍼랜드 값을 계산하는 데 사용된다.  
    - C++17부터는 특정한 상황이 아니면 메모리에 실제로 존재하지 않다가, 필요할 때 객체로 구체화(materialize)된다.  
- `lvalue`는 `xvalue`가 아닌 모든 `glvalue`이다.

### prvalue

```cpp
int x = 10;
int y = x + 5;
```

`10`과 `x + 5`는 `x`와 `y`를 설정하는 데 사용되는 값으로, `x`와 `y`의 실제 메모리 공간에 그러한 값이 설정되고 나면 더 이상 필요하지 않다.  

이들 값은 연산의 중간 결과이거나, 단순한 리터럴 값 그 자체이므로, 할당된 고유한 메모리 주소가 없다. 한번 사용하고 나면 정확히 같은 값은 프로그램이 다시 찾아갈 방법이 없다.  

```cpp
&(10);  // error
&(x + 5);  // error
```

`&10`과 `&(x + 5)`은 모두 실체가 없다.  

### xvalue

C++11 이전에는 메모리 주소가 있으면 데이터는 무조건 lvalue였다. 더 이상 사용하지 않음이 확실한 lvalue는 자원을 이동시키더라도 크게 문제되지 않는다.  

그래서 식별자가 존재함에도 불구하고, 곧 사라질 예정이라 안에 들어있는 데이터를 다른 곳으로 이동해도 무방한 값을 새롭게 xvalue로 분류하였다.  

```cpp
std::string str = "Hello, World!";

// std::move(str) : xvalue
std::string str2 = std::move(str);
```

`std::move`는 새로운 식별자를 생성하지 않고, 기존의 lvalue를 rvalue 참조 `T&&`로 변환한다. 변환된 결과는 xvalue이다.


> `a.m`에서 `a`가 rvalue이고 `m`이 정적이 아닌 데이터 멤버라면 `a.m`은 xvalue이다.  
> 
> [cppreference, Value Category [basic.lval]](https://en.cppreference.com/cpp/language/value_category)

```cpp
struct vector { int x; int y; };

vector{1, 2};
vector{1, 2}.x;
```

또한 이 코드에서도 rvalue이면서 xvalue인 사례를 찾을 수 있다. `vector{1, 2}` 는 식별자를 가지지 않는 임시 객체를 생성하는 표현식이다. 따라서 prvalue이다.  

`vector{1, 2}.x`는 임시 객체의 멤버 `x`를 참조하는 표현식이다. 임시 객체는 곧 만료될 예정이므로, 그 안에 속한 멤버 `x` 역시 곧 만료될 값으로 취급된다. 따라서 이동이 허용된다.
