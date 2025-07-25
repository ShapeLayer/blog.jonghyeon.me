---
layout: post
title: C#의 컴파일타임 상등 비교와 런타임 상등 비교
date: '2023-02-20'
categories: [language, csharp]
tags: [language, csharp]
---

C#에서 각 타입의 상등 비교를 지원하기 위해 구현할 수 있는 것은 크게 세가지입니다.  
 * `==`와 `!=` 연산자
 * `Equals` 메서드
 * `IEquatable<T>` 인터페이스

## `==`, `!=` 연산자
`==`와 `!=`는 연산자이므로 결과가 정적으로 결정되어야 합니다. 실제로 이 연산자 구현체는 `static` 키워드가 포함됩니다. 컴파일러는 컴파일 중 비교를 수행할 형식을 미리 결정해둡니다.  
값 형식은 값 상등을, 참조 형식은 참조 상등을 평가합니다.  

```cs
int x = 5, y = 5;
Console.WriteLine(x == y); // True
```
_값 상등_

```cs
class Foo { public int x; }

Foo foo = new Foo { x = 5 };
Foo var = new Foo { x = 5 };
Console.WriteLine(foo == var); // False
foo = var;
Console.WriteLine(foo == var); // True
```
_참조 상등_

## 가상 `Object.Equals` 메서드와 정적 `object.Equals` 메서드
`System.Object`에는 `Equals` 가상 메서드가 정의되어 있습니다. 즉 모든 형식이 이 메서드를 갖습니다.  
`Equals`는 상등 연산자와 달리 런타임에서 상등을 평가합니다. 따라서 형식에 구애받을 필요가 없습니다.  

```cs
object x = -1, y = -1;
Console.WriteLine(object.Equals(x, y)); // True
x = null;
Console.WriteLine(object.Equals(x, y)); // False
y = null;
Console.WriteLine(object.Equals(x, y)); // True
```

`Equals` 메서드가 런타임에서 상등을 평가하니 컴파일타임에서 평가하는 연산자의 상등 평가와 결과가 상이할 수 있습니다.  

```cs
object x = 5, y = 5;
Console.WriteLine(x == y); // False
Console.WriteLine(x.Equals(y)); // True
```

## 상등 비교 처리가 다른 이유
프로그래밍을 학습하는 과정에서 값과 참조의 개념은 익숙하지 않은 사람에게 충분히 혼선을 줍니다. 이 개념을 혼동하면 코드가 의도와 달리 작동할 가능성이 농후하고, 잠재적으로 버그가 됩니다.  

만약 상등 연산자 `==`를 가상으로 구현해서 `Equals`와 같은 방식으로 런타임에서 상등을 평가했다면 이러한 문제를 피할 수 있었을 것입니다. 하지만 상등 연산자와 상등 메서드의 작동 방식을 구분한 것은 나름의 이유가 있습니다.  

우선 두 상등 비교 수단이 같은 역할을 수행한다면 둘 중 하나는 존재하지 않아도 될 것입니다. 실제로 `Equals`를 상등 비교 수단으로 채택하지 않는 언어도 꽤 있습니다. 이 둘이 각자 다른 의미의 상등 비교를 수행하게 하는 것이 종종 유용한 경우가 있습니다.  

```cs
double x = double.NaN;
Console.WriteLine(x == x); // False: 값 상등
Console.WriteLine(x.Equals(x)); // True: 참조 상등 (반사적 상등)
```

수학적으로 `NaN`은 다른 그 어떤 수와도 같지 않습니다. 즉, `NaN`의 값 상등 평가는 항상 `false`여야 합니다.  
하지만 `x` 변수는 실제로 메모리 상의 `x` 변수를 참조하며로 `x`와 `x`의 참조 상등 평가는 `true`입니다. 실제로 두 변수는 같은 것이기 때문입니다.  

```cs
var sba = new StringBuilder("foo");
var sbb = new StringBuilder("foo");
Console.WriteLine(sba == sbb); // False: 값 상등
Console.WriteLine(sba.Equals(sbb)); // True: 값 상등
```

`NaN` 사례처럼 연산자가 값 상등, 메서드가 참조 상등을 처리하는 경우는 꽤 드뭅니다. 두 상등이 서로 다른 의미로 적용된다면 이 사례처럼 연산자가 참조 상등, 메서드가 값 상등을 적용하는 것이 더 흔합니다.  

연산자와 메서드를 달리 작동하도록 하는 또 다른 이유도 있습니다.  
 * 당연하지만 상등 메서드는 첫번째 피연산자가 널이면 `NullReferenceException`이 발생합니다. `null` 아래에는 `Equals`가 없습니다.  
 * 상등 연산자는 정적으로 처리되므로 실행 속도가 빠릅니다. 즉, 실행 시간이 이미 충분히 길 수 있는 코드에서, 혹은 `Equals` 처리가 상대적으로 오래 걸리는 형식에서 상등 연산자는 사용해도 성능상 피해가 없거나 미비함을 보장합니다.

## `IEquatable<T>` 인터페이스
`object.Equals`는 값 형식 피연산자들에 박싱을 적용합니다. 박싱은 비싼 연산이므로 성능상 큰 피해를 입을 수 있습니다.  
`IEquatable<T>` 인터페이스는 이 문제를 해결하고자 도입됩니다.  

```cs
public interface IEquatable<T>
{
  bool Equals (T other);
}
```

```cs
class Example<T> where T: IEquatable<T>
{
  public bool IsEqual(T a, T b) { return a.Equals(b); }
}
```