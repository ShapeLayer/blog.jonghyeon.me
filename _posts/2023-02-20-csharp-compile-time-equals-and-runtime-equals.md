---
layout: post
title: C#의 컴파일타임 상등 비교와 런타임 상등 비교
date: '2023-02-20'
categories: [language, csharp]
tags: [language, csharp]
---

C#에서 각 타입의 상등 비교를 지원하기 위해 구현할 수 있는 것은 크게 세가지이다.  
 * `==`와 `!=` 연산자
 * `Equals` 메서드
 * `IEquatable<T>` 인터페이스

## `==`, `!=` 연산자
`==`와 `!=`는 연산자이므로 결과가 정적으로 결정되어야 한다. 실제로 이 연산자 구현체는 `static` 키워드가 포함된다. 컴파일러는 컴파일 중 비교를 수행할 형식을 미리 결정해둔다. 값 형식은 값 상등을, 참조 형식은 참조 상등을 평가한다.  

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

`System.Object`에는 `Equals` 가상 메서드가 정의되어 있습니다. 즉 모든 형식이 이 메서드를 갖는다. `Equals`는 상등 연산자와 달리 런타임에서 상등을 평가한다. 따라서 형식에 구애받을 필요가 없다.  

```cs
object x = -1, y = -1;
Console.WriteLine(object.Equals(x, y)); // True
x = null;
Console.WriteLine(object.Equals(x, y)); // False
y = null;
Console.WriteLine(object.Equals(x, y)); // True
```

<br />

`Equals` 메서드가 런타임에서 상등을 평가하니 컴파일 타임에서 평가하는 연산자의 상등 평가와 결과가 상이할 수 있다.  

```cs
object x = 5, y = 5;
Console.WriteLine(x == y); // False
Console.WriteLine(x.Equals(y)); // True
```

## 상등 비교 처리가 다른 이유

상등 연산자 `==`를 가상으로 구현해서 `Equals`와 같은 방식으로 런타임에서 상등을 평가했다면 비교 처리가 달라지지 않았을 것이다. 하지만 상등 연산자와 상등 메서드의 작동 방식을 구분한 것은 나름의 이유가 있다.  

우선 두 상등 비교 수단이 같은 역할을 수행한다면 둘 중 하나는 존재하지 않아도 될 것다. 실제로 `Equals`를 상등 비교 수단으로 채택하지 않는 언어도 꽤 있다. 이 둘이 각자 다른 의미의 상등 비교를 수행하게 하는 것이 종종 유용한 경우가 있다.  

```cs
double x = double.NaN;
Console.WriteLine(x == x); // False: 값 상등
Console.WriteLine(x.Equals(x)); // True: 참조 상등 (반사적 상등)
```

수학적으로 `NaN`은 다른 그 어떤 수와도 같지 않다. 즉, `NaN`의 값 상등 평가는 항상 `false`여야 한다. 하지만 `x` 변수는 실제로 메모리 상의 `x` 변수를 참조하므로 `x`와 `x`의 참조 상등 평가는 `true`여야 한다. 실제로 두 변수는 같은 것이기 때문이다.  

```cs
var sba = new StringBuilder("foo");
var sbb = new StringBuilder("foo");
Console.WriteLine(sba == sbb); // False: 값 상등
Console.WriteLine(sba.Equals(sbb)); // True: 값 상등
```

`NaN` 사례처럼 연산자가 값 상등, 메서드가 참조 상등을 처리하는 경우는 꽤 드물다. 두 상등이 서로 다른 의미로 적용된다면 이 사례처럼 연산자가 참조 상등, 메서드가 값 상등을 적용하는 것이 더 흔하다.  

연산자와 메서드를 달리 작동하도록 하데에는 또 다른 이유도 있다.  
 * 당연하지만 상등 메서드는 첫번째 피연산자가 널이면 `NullReferenceException`이 발생한다. `null` 아래에는 `Equals`가 없다.  
 * 상등 연산자는 정적으로 처리되므로 실행 속도가 빠르다. 즉, 실행 시간이 이미 충분히 길 수 있는 코드에서, 혹은 `Equals` 처리가 상대적으로 오래 걸리는 형식에서 상등 연산자는 사용해도 성능상 피해가 없거나 미비함을 보장한다.

## `IEquatable<T>` 인터페이스

`object.Equals`는 값 형식 피연산자들에 박싱을 적용한다. 박싱은 비싼 연산이므로 성능에 큰 피해를 입을 수 있다. `IEquatable<T>` 인터페이스는 이 문제를 완화하기 위해 도입된다.  

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

**Refining Terminology**

I'm currently revisiting the use of "규약" and exploring alternative phrasing. My focus is on identifying instances where it appears, like in the phrase "객체 상등 규약 준수," and considering more appropriate replacements to ensure clarity and precision in my output.

'규약'이라는 단어를 문맥에 맞게 **'원칙'**, **'규칙'**, **'계약'** 등으로 대체한 수정판입니다.

---

```markdown
---
layout: post
title: C#의 컴파일타임 상등 비교와 런타임 상등 비교
date: '2023-02-20'
categories: [language, csharp]
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
