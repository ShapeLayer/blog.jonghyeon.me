---
layout: post
title: OOP에서 "속성"이 갖는 두가지 의미
date: '2021-07-09'
categories: [language]
tags: [oop, language, csharp, terms]
---

OOP에서, 어떤 클래스가 갖는 변수를 "속성"이라고 합니다.

```cs
class TextBox {
  public string value;
  public int width;
  public int height;
}
```

위 `TextBox` 클래스는 `value`, `width`, `height` 속성을 갖고 있습니다.  
이 속성은 attribute로 번역할 수 있을까요? property로 번역할 수 있을까요? 여느 번역이나 다 그렇듯, 원어가 갖고 있는 의미를 번역으로 정확히 전달하기란 어렵습니다.  

속성은 영어로 attribute 혹은 property이므로 겉으로는 똑같은 의미를 내포하고 있는 것으로 보입니다. 하지만 두 용어는 꽤 차이를 가지고 있습니다. attribute와 property는 엄연히 다른 용어입니다.  

## 가상의 UI 애플리케이션 작성해보기
위 `TextBox` 클래스로 UI 애플리케이션을 작성한다고 생각해봅시다.  

```cs
TextBox heroNotificationControl = new TextBox("새 공지사항이 없습니다.");
```

애플리케이션을 작성하다보니 텍스트 박스의 문자열 값의 길이를 따로 기록하고 싶어졌습니다. `String.Length`로 문자열 값의 길이를 확인할 수 있음에도 말입니다.  

```cs
class TextBox {
  ...
  public int length;
  public TextBox(string value) {
    this.value = value;
    this.length = value.Length;
  }
}
```

`value` 속성과 `length` 속성은 상황 맥락적으로 의미가 있을지 모르지만, 코드상에서는 연관이 없습니다. 두 속성은 각자 독립적이어서 만약 `value` 속성을 변경하게 된다고 하면 `length` 속성도 별도로 처리를 해야할 것입니다.  

```cs
class TextBox {
  public updateTextValue(string value) {
    this.value = value;
    this.length = value.Length;
  }
}
```

이러한 코드는 코드를 수정할 다른 사람이나 미래의 나와 잘 소통이 된다면 문제가 발생하지 않을 겁니다. 하지만 전 항상 과거의 저와 소통이 잘 된적이 없었습니다.  

아마 높은 확률로 이런 코드를 어딘가에 추가할 것입니다.  

```cs
class TextBox {
  public updateTextValueOnly(string value) {
    this.value = value;
  }
}
```

위쪽의 UI 애플리케이션 코드를 가져와서 이번엔 한번 `value` 속성을 수정해보겠습니다.  

```cs
TextBox heroNotificationControl = new TextBox("새 공지사항이 없습니다.");
Console.Writeline($"value: {heroNotificationControl.value}, length: {heroNotificationControl.length}");
// value: 새 공지사항이 없습니다., length: 13
heroNotificationControl.updateTextValue("새 공지사항을 가져오는 중입니다.");
Console.Writeline($"value: {heroNotificationControl.value}, length: {heroNotificationControl.length}");
// value: 새 공지사항을 가져오는 중입니다., length: 18
heroNotificationControl.updateTextValueOnly("새 공지사항이 없습니다.");
Console.Writeline($"value: {heroNotificationControl.value}, length: {heroNotificationControl.length}");
// value: 새 공지사항이 없습니다., length: 18
```

`updateTextValue` 메서드는 `value`의 변화를 `length`에 잘 반영했지만, `updateTextValueOnly` 메서드는 그렇지 못했습니다. 이러한 Human-error는 누구나 일으킬 수 있습니다.  

물론 이러한 사례를 충분한 코딩 전략과 디자인 패턴을 활용하여 방지할 수 있습니다. 그리고 또 다른 좋은 방법을 사용할 수 있습니다.  

## 프로퍼티(Property), 속성을 메서드처럼
서두에서 attribute와 property는 엄연히 다른 용어라고 했습니다. 둘 다 한국어로는 속성으로 번역되나 지금까지 살펴본 속성은 attribute입니다. 그리고 attribute는 property와 구분하기 위해 "일반 속성"이라고 표현하겠습니다.  

프로퍼티는 변수(정확히는 필드) getter와 setter를 두고 값을 가져오거나 설정하려 할 때 getter나 setter를 실행합니다. 즉, getter와 setter는 함수입니다.  

```cs
class TextBox {
  public string value;
  public int width;
  public int height;
  public int length {
    get { return value.Length; }
  }
}
```

위와 같이 정의한다면 `length` 프로퍼티는 `value`의 길이를 항상 잘 나타낼 것입니다.  

```cs
TextBox t = new TextBox("hello");
Console.WriteLine(t.length);
// 5
t.value = "hello world";
Console.WriteLine(t.length);
// 11
```

또 getter와 setter라고 표현했으나, 위 코드에서는 getter만 작성했습니다. 이렇게 작성하면 `length`를 수정하려 할 때 오류를 반환할 것입니다.

```cs
TextBox t = new TextBox("hello");
t.length = 3;
```

```
error CS0200: Property or indexer 'TextBox.length' cannot be assigned to -- it is read only
```

## getter와 get~ 메서드
프로퍼티에는 getter와 setter가 존재하고, 그것들은 함수이며, 실제로 "실행"한다는 사실은 차라리 자바에서 널리 쓰이는 `getField()` `setField()` 패턴을 채택해도 문제 없지 않나 싶을겁니다.  

실제로 그럴 수도 있습니다. 관점에 따라서 프로퍼티는 눈속임일 뿐이므로 getter setter 메서드를 작성하여 사용할 수도 있습니다.  

하지만 프로퍼티는 메서드를 일반 속성처럼 블랙박스화하고 "겉보기로는 일반 속성"에 읽기/쓰기 권한을 따로 따로 부여할 수 있습니다. (바로 위에서 getter만 작성하여 쓰기 권한을 제거한 것 같은 효과를 낸 것처럼) 이러한 활용법들은 클래스 사용자가 코드를 좀 더 유연하게 작성할 수 있도록 도울 수 있을지도 모릅니다.  
