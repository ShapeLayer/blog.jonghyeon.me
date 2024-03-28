---
layout: post
title: C# 이벤트 트리거와 핸들링
date: '2024-03-28'
categories: [language, csharp]
tags: [language, csharp]
---

코드 전체로 이벤트를 브로드캐스팅하는 자바스크립트와 달리, C#은 이벤트 트리거와 핸들링에 관찰자 모델을 채택했습니다. 이벤트를 브로드캐스팅하는 방법은 꽤 직관적이고 편리하지만, 전역 변수가 그러하듯 몇몇 사이드 이펙트가 발생하기도 합니다.

C#, 정확히는 닷넷의 이벤트 처리는 이와 비교해 조금 복잡하고 어려울 수 있지만, 오히려 엄격한 규칙과 조건에 따라 동작하므로 코드 동작 시나리오가 더욱 정제되고 관리가 편해질 수 있으리라 생각합니다.

## 이벤트 발신 측

C#에서 이벤트는 `EventHandler` 를 사용합니다. 자바스크립트에서 이벤트 처리를 해보았다면 혼동이 올 수 있는데, 웹에서 “이벤트 핸들러”라는 표현은 일반적으로 이벤트를 수신하는 측에 사용하기 때문입니다. 

```csharp
public event EventHandler CustomEvent;
CustomEvent?.Invoke(null, EventArgs.Empty);
```

실제로 위의 예문과 같이 사용하게 되는데, `EventHandler` 가 `Invoke` 를 사용하여 이벤트를 발생시킵니다.

## 이벤트 수신 측

하지만 그렇다고 하더라도 이벤트 수신 측을 이벤트 핸들러라고 표현하지 않는 것은 아닙니다.

```csharp
public static void Main()
{
    CustomEvent += _EventHandler;
    CustomEvent?.Invoke(null, EventArgs.Empty);
}

static void _EventHandler(object sender, EventArgs e)
{
    Console.WriteLine($"CustomEvent Invoked: by {sender}");
}
```

이벤트 핸들러는 여전히 이벤트 핸들러입니다. 이러한 혼동은 `EventHandler` 가 대리자로 정의되기 때문에 발생합니다.

`EventHandler`가 `public delegate void EventHandler(object? sender, EventArgs e)` 로 선언된 대리자이기 때문에 이벤트 핸들러의 매개 변수는 `(object?, EventArgs)` 로 강제됩니다.

정리하자면 `EventHandler` 대리자에 1. `(object?, EventArgs)` 를 매개 변수로 받는 이벤트 핸들러 함수를 구독시켜 2. `EventHandler`에서 이벤트를 발생시키면 3. 이벤트 핸들러 함수가 이 이벤트를 수신하는 형식으로 동작한다고 정리할 수 있겠습니다.

## 이벤트 수신과 발신

**코드**

```csharp
using System;

public class Program
{
    public static void Main()
    {
        SimpleEventClass simpleEventObject = new SimpleEventClass();
        // 이벤트 구독
        simpleEventObject.CustomEvent += onCustomEvent;
        // 이벤트 발생 Wrapper 함수 호출
        simpleEventObject.InvokeEvent();
        // 이벤트 구독 해제
        simpleEventObject.CustomEvent -= onCustomEvent;
    }

    static void onCustomEvent(object sender, EventArgs e)
    {
        Console.WriteLine($"CustomEvent Invoked: by {sender}");
    }
}

public class SimpleEventClass
{
    public event EventHandler CustomEvent;
    
    // 이벤트 발생 Wrapper
    public void InvokeEvent()
    {
        CustomEvent?.Invoke(this, EventArgs.Empty);
    }
}

```

**출력**

```
CustomEvent Invoked: by SimpleEventClass
```

## 이벤트에 매개 변수 전달하기

이벤트를 발생시키는 `Invoke()` 에 `EventArgs.Empty`를 넣어서 보내고 있는데, `EventArgs` 는 이벤트 수신자에게 매개 변수를 전달하는 역할을 합니다. `EventArgs.Empty`는 빈 매개변수 구현체이므로 매개 변수를 전달하고자 한다면 매개 변수의 포맷부터 정의해야 합니다.

```csharp
class CustomEventArgs : EventArgs
{
  public int x;
  public CustomEventArgs(int x = -1)
  {
    this.x = x;
  }
}
```

이벤트 핸들러는 `EventArgs` 객체를 매개 변수로 받으므로, 이벤트 핸들러가 매개 변수를 제대로 수신하려면 정의할 매개 변수 포맷도 `EventArgs` 를 상속해야 합니다.

**이벤트 발신 측**

```csharp
public class SimpleEventClass
{
    public event EventHandler CustomEvent;
    
    // 이벤트 발생 Wrapper
    public void InvokeEvent()
    {
        CustomEvent?.Invoke(this, new CustomEventArgs());
    }
}
```

**이벤트 수신 측**

```csharp
public class Program
{
    public static void Main() { ... }

    static void onCustomEvent(object sender, EventArgs e)
    {
        Console.WriteLine($"CustomEvent Invoked: by {sender}, value: {((CustomEventArgs)e).x}");
    }
}
```

이벤트 발신 측에서 생성하고 넘겨준 매개 변수인 `CustomEventArgs`는 수신 측 이벤트 핸들러에 `EventArgs` 로 박싱되어 전달됩니다. 따라서 형변환 연산자를 사용하여 `((CustomEventArgs)e).x`, 언박싱 후 사용합니다.

## `add` 접근자와 `remove` 접근자

`EventHandler`는 마치 클래스의 생성자, 소멸자와 같이 구독, 구독 해제 시의 동작을 정의할 수 있습니다. 주로 `EventHandler`를 숨기고, 외부에 구독, 구독 해제의 “통로”를 만들 때 사용한다는 점에서 마치 `EventHandler`의 getter, setter 같습니다. 

**이벤트 발신 측**

```csharp
public class ComplexAddRemoveEventClass
{
    // 이벤트 핸들러 은닉
    private EventHandler handler;
    
    // 외부에 노출
    public event EventHandler CustomEvent
    {
        add
        {
            Console.WriteLine("Called add accessor in ComplexAddRemoveEventClass.");
            this.handler += value;
        }
        remove
        {
            Console.WriteLine("Called remove accessor in ComplexAddRemoveEventClass.");
            this.handler -= value;
        }
    }

    public void InvokeEvent() { ... }
}
```

**이벤트 수신 측**

```csharp
public class Program
{
    public static void Main()
    {
        ComplexAddRemoveEventClass complexObject = new ComplexAddRemoveEventClass();
        complexObject.CustomEvent += onCustomEvent;
        complexObject.InvokeEvent();
        complexObject.CustomEvent -= onCustomEvent;
    }

    static void onCustomEvent(object sender, EventArgs e)
    {
        Console.WriteLine($"CustomEvent Invoked: by {sender}, value: {((CustomEventArgs)e).x}");
    }
}
```

**출력**

```
Called add accessor in ComplexAddRemoveEventClass.
CustomEvent Invoked: by ComplexAddRemoveEventClass, value: -1
Called remove accessor in ComplexAddRemoveEventClass.
```
