---
layout: post
title: C#의 컴파일타임 상등 비교와 런타임 상등 비교
date: '2023-02-20'
categories: [language]
tags: [language, csharp]
---

C#에서 각 타입의 상등 비교를 지원하기 위해 구현할 수 있는 것은 크게 세 가지이다.  
 * `==`와 `!=` 연산자
 * `Equals` 메서드 (`virtual object.Equals`, `static object.Equals`)
 * `IEquatable<T>` 인터페이스

## `==`, `!=` 연산자

`==`와 `!=`는 연산자이므로 호출할 메서드가 컴파일 타임에 정적 바인딩(정적으로 결정)된다. 실제로 이 연산자 구현체는 `static` 메서드로 정의된다. 컴파일러는 피연산자의 컴파일 타임 정적 형식을 기준으로 비교 로직을 결정한다.

기본 동작으로 값 형식은 값 상등을, 참조 형식은 참조 상등을 평가한다. (단, `string`이나 `record`처럼 참조 형식이어도 연산자를 오버로딩하여 값 상등을 평가하도록 재정의할 수 있다.)

```cs
int x = 5, y = 5;
Console.WriteLine(x == y); // True (값 상등)
```
_값 상등_

```cs
class Foo { public int x; }

Foo foo = new Foo { x = 5 };
Foo bar = new Foo { x = 5 };
Console.WriteLine(foo == bar); // False (참조 상등)
foo = bar;
Console.WriteLine(foo == bar); // True (참조 상등)
```
_참조 상등_

## 가상 `Object.Equals` 메서드와 정적 `object.Equals` 메서드

`System.Object`에는 `Equals` 가상 메서드가 정의되어 있다. 즉 C#의 모든 형식이 이 메서드를 상속받거나 재정의할 수 있다.  
`Equals`는 연산자와 달리 런타임에 실제 객체의 형식을 기반으로 가상 디스패치(Virtual Dispatch)되어 상등을 평가한다.

```cs
object x = -1, y = -1;
Console.WriteLine(object.Equals(x, y)); // True
x = null;
Console.WriteLine(object.Equals(x, y)); // False
y = null;
Console.WriteLine(object.Equals(x, y)); // True
```

`==` 연산자는 정적 형식을 기준으로 평가되고, `Equals` 메서드는 런타임 인스턴스 형식을 기준으로 평가되므로 동일한 피연산자라도 결과가 상이할 수 있다.

```cs
object x = 5, y = 5;
Console.WriteLine(x == y);       // False (정적 형식인 object의 == 호출 -> 서로 다른 박싱된 참조 비교)
Console.WriteLine(x.Equals(y));  // True (런타임 형식인 int.Equals(object)가 가상 호출됨)
```

## 상등 비교 처리가 다른 이유

상등 연산자 `==`를 가상 메서드로 설계하지 않고 정적 연산자와 가상 메서드로 이원화한 것에는 나름의 이유가 있다. 상황에 따라 참조 식별과 값의 일치라는 서로 다른 의미의 상등 비교가 필요하기 때문이다.

### 1. 부동소수점(`double.NaN`)의 사례

```cs
double x = double.NaN;
Console.WriteLine(x == x);       // False: IEEE 754 표준 준수
Console.WriteLine(x.Equals(x));  // True: .NET 컬렉션의 반사성(Reflexivity) 원칙 준수
```

* `==` 연산자는 IEEE 754 부동소수점 표준을 준수한다. 표준에 따라 `NaN`은 어떤 값과도(심지어 자기 자신과도) 같지 않으므로 `false`를 반환한다.  
* 반면 `Equals`는 .NET의 동등성 핵심 원칙인 반사성(`x.Equals(x) == true`)을 만족해야 한다. 만약 `double.Equals`마저 `false`를 반환한다면 `Dictionary<double, string>`이나 `HashSet<double>`에 `NaN`을 저장했을 때 키를 영영 찾을 수 없는 문제가 발생하기 때문이다.  

### 2. `StringBuilder`의 사례

```cs
var sba = new StringBuilder("foo");
var sbb = new StringBuilder("foo");
Console.WriteLine(sba == sbb);       // False: 참조 상등 (== 연산자가 오버로딩되지 않음)
Console.WriteLine(sba.Equals(sbb));  // True: 값 상등 (StringBuilder.Equals가 문자열 내용을 비교)
```

두 상등이 서로 다른 의미로 사용될 때는 일반적으로 연산자는 기본 참조 상등을, 메서드는 내용(값) 상등을 평가하도록 분리한다.  

### 그 외

* Null 안전성: 가상 인스턴스 메서드 `x.Equals(y)`는 `x`가 `null`일 경우 `NullReferenceException`이 발생한다. 반면 `==` 연산자나 정적 메서드 `object.Equals(x, y)`는 피연산자가 `null`이어도 예외 없이 안전하게 비교할 수 있다.

* 호출 비용: `==` 연산자는 정적으로 바인딩되므로 가상 메서드 테이블(vtable) 조회를 거치지 않고 인라인화(Inlining)될 가능성이 높아 오버헤드가 적다.

## `IEquatable<T>` 인터페이스

`object.Equals(object)`는 매개변수 타입이 `object`이므로, 값 형식을 비교할 때 힙 할당을 유발하는 박싱(Boxing)이 발생한다. 박싱은 GC 압력을 증가시키고 성능을 저하시킨다. `IEquatable<T>`는 제네릭 환경에서 박싱 없는 타입 안정적인 값 비교를 지원하기 위해 제공된다.  

```cs
public interface IEquatable<T>
{
  bool Equals(T other);
}
```

```cs
// 값 형식 T가 IEquatable<T>를 구현하면 박싱 없이 Equals(T)가 직접 호출된다.
class Example<T> where T : IEquatable<T>
{
  public bool IsEqual(T a, T b)
  {
    // null 안전성을 포함한 EqualityComparer<T>.Default.Equals(a, b) 사용이 권장된다.
    return a != null && a.Equals(b);
  }
}
```
