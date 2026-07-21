---
layout: post
title: C++ std::vector\<bool>
date: 2026-07-21
categories: [c++]
tags: [c++, std]
---

## 도입

`std::vector<bool>`을 사용하면서 컴파일러 warning이 발생하는 것을 확인했다. 문제의 코드는 `printf`로 `std::vector<bool>`의 인덱스 접근을 int로 출력했다.  

```c++
std::vector<bool> is_contained(10);
// ...
for (int i = 0; i < 10; i++) {
  printf("is_contained[%d]: %d\n", i, is_contained[i]);
}
/**
 * warning: format specifies type 'int' but the argument has type 'reference' (aka
 *      '__bit_reference<vector<bool, std::allocator<bool>>>') [-Wformat]
 */
```

경고문은 reference 타입을 int로 출력하려고 했다는데, 잠시 납득하다가도 이해되지 않는 부분이 있었다. 다른 타입의 `std::vector`는 값으로 반환하지 않았나? 다른 타입에서 인덱스 연산자로 접근했을 땐 경고문을 받은 적이 없었다.  

```c++
std::vector<int> int_container;
int_container.push_back(1);
printf("int_container[0]: %d\n", int_container[0]);
std::vector<long long int> lld_container;
lld_container.push_back(1);
/**
 * warning: format specifies type 'int' but the argument has type 'value_type' (aka 'long long') [-Wformat]
 */
```

실제로 `std::vector<int>`에서는 경고가 발생하지 않았고, `std::vector<long long int>`에서는 `std::vector<bool>`와는 조금 다른 경고문이 발생했다. int와 lld에서는 값으로 반환되었는데 bool은 참조로 반환되고 있었다.  

## `std::vector<bool>`은 데이터를 비트 단위로 저장한다

`std::vector<bool>` 타입은 메모리를 최적화하기 위해 데이터를 비트 단위로 저장하도록 특수화되어있다. (specialized로 표현하고 있다.) 라이브러리 차원에서 비트마스킹을 하고 있는 셈이다.  

그래서 `std::vector<bool>`의 데이터는 8개 단위로 같은 주소를 공유한다.(현대 컴퓨터에서 byte마다 주소를 할당하므로) 같은 이유에서 `std::vector<bool>`의 데이터는 포인터 `bool*`나 참조 `bool&`로 직접 가리킬 수 없다.  

```
flag_vec[0]: 20668176
flag_vec[1]: 20668176
flag_vec[2]: 20668176
flag_vec[3]: 20668176
flag_vec[4]: 20668176
flag_vec[5]: 20668176
flag_vec[6]: 20668176
flag_vec[7]: 20668176
flag_vec[8]: 20668176
flag_vec[9]: 20668176
```
_런타임에서 `std::vector<bool>(10)`에 대해 인덱스로 접근한 결과_  

그러나 실제로 `std::vector<bool>`의 인덱스 접근은 8개 단위로 인덱스를 묶어 8개씩 같은 주소를 가리키지는 않는다. 8개씩 묶어 같은 주소를 가리키더라도 그 이후에 몇 번째 비트인지를 적절히 표현할 수 없기 때문에 `[0]`, `[3]`, `[7]` 모두 `[0]` 값의 주소가 반환되기 때문이다.

그보다는 모든 인덱스 범위에서 같은 주소를 가리키는데, `std::vector<bool>::reference` 타입을 새롭게 두어, 이 타입이 비트 단위로 저장된 데이터로의 접근을 제공하도록 구현되어있다.

## 이로부터 촉발되는 문제

이와 같이 특화 구현된 `std::vector<bool>`은 메모리에 직접 접근하는 함수 구현에서 잠재적으로 undefined behavior를 발생시킬 수 있다. 대표적인 구현으로는 `std::swap`이 있다고 알려져있다.  

```c++
swap(flag_vec[0], flag_vec[1]);

// 구현에 따라서
// 0번 인덱스 값과 1번 인덱스 값이 서로 바뀌지 않고,
// 0~7번 인덱스 값과 8~15번 인덱스 값이 서로 바뀔 수도 있다.
```

<br />

다만 확인 가능한 범위 내(Apple `clang-2100.1.1.101`, GDB 온라인: [`g++ 11.4.0 -std=c++11`, `g++ 11.4.0 -std=c++14`](https://www.onlinegdb.com/faq))에서는 `std::swap`이 `std::vector<bool>`에 대해 특화 구현되어 예상 가능하게 0번 인덱스 값과 1번 인덱스 값이 서로 바뀌도록 되어있었다.  

```c++
flag_vec.push_back(false);
flag_vec.push_back(true);
flag_vec.push_back(false);
printf("flag_vec.at(0): %d\n", (int)flag_vec.at(0));
printf("flag_vec.at(1): %d\n", (int)flag_vec.at(1));
printf("flag_vec.at(2): %d\n", (int)flag_vec.at(2));
swap(flag_vec[1], flag_vec[2]);
printf("\n");
printf("flag_vec.at(0): %d\n", (int)flag_vec.at(0));
printf("flag_vec.at(1): %d\n", (int)flag_vec.at(1));
printf("flag_vec.at(2): %d\n", (int)flag_vec.at(2));
```

```
flag_vec.at(0): 0
flag_vec.at(1): 1
flag_vec.at(2): 0

flag_vec.at(0): 0
flag_vec.at(1): 0
flag_vec.at(2): 1
```

<br />

> std::vector should not be specialized with bool. 

이와 같이 예측 불가능한 동작으로 인해 MISRA C++에서는 `std::vector<bool>`의 사용을 금지하기까지 했다. [MISRA C++2023 Rule 26.3.1](https://kr.mathworks.com/help/bugfinder/ref/misracpp2023rule26.3.1.html)

## 대안

bool 타입을 다른 데이터와 함께 구조체를 이루지 않고, 벡터(혹은 리스트)로 처리하는 대부분의 경우는 여러 개의 플래그를 한 데 모아 다루는 시나리오일 것이므로, 가변 길이의 벡터는 불필요하다. 배열로 데이터를 정의하거나 직접 비트마스킹을 하는 편이 제일 안전할 것으로 보인다. (개인적으로도 지금까지 배열 데이터 데이터나 비트마스킹이 아니면 가변 길이의 `std::vector<bool>`을 사용하려고 하지는 않아, 이제서야 알게 되었다.)  

혹 정말 예외적으로 가변 길이 bool 리스트가 필요하다면, `std::vector<bool>` 대신 1바이트 단위로 데이터를 핸들링하는 `std::vector<uint8_t>`, `std::vector<char>`를 사용하거나, bool 타입을 구조체로 래핑해서 바이트 단위로 주소를 받을 수 있도록 처리할 수도 있다.  

```c++
typedef struct bool_w {
  bool value;
} bool_t;
```
