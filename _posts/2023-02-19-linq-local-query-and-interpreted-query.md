---
layout: post
title: LINQ에서의 지역 질의와 해석식 질의
date: '2023-02-19'
categories: [language, csharp]
tags: [language, csharp, dotnetframework]
---

LINQ는 닷넷프레임워크에 포함된 기능이라 그런지 C#뿐 아니라 SQL Server와 같은 MS의 다른 제품군을 대상으로도 작성할 수 있습니다.  

SQL Server처럼 코드 외부의 데이터 소스에 대해 작성하는 LINQ 질의를 해석식 질의 (Interpreted Query)라고 합니다. 이와 대비해서 코드 내부의 컬렉션을 대상으로 작성하는 LINQ 질의는 지역 질의 (Local Query)입니다.

## 지역 질의와 `IEnumerable<T>`
지역 질의는 데이터를 참조하기 위해 LINQ가 직접 코드 범위 바깥으로 나가지 않습니다. 따라서 전적으로 IL 코드 범위 내에서 실행됩니다.

```cs
string[] languages = { "C", "C++", "Java", "C#", "Go", "Rust", "Python" }
IEnumerable<string> query =
  from language in languages
  select language.Replace("+", "p")
                 .Replace("#", "sharp")
  into langNoSymbol
    where   langNoSymbol.Length > 2
    orderby langNoSymbol
    select  langNoSymbol;
foreach (string lang in query) Console.WriteLine(lang);
```

```txt
Cpp
Csharp
Java
Python
Rust
```

C#의 모든 이터레이터는 `IEnumerable<T>`를 구현하므로 지역 질의는 `IEnumerable<T>`를 구현하는 모든 컬렉션들에 대해 작동합니다.  

## 해석식 질의와 `IQueryable<T>`
해석식 질의는 `IQueryable<T>`를 구현하는 순차열에 대해 작동합니다. `IQueryable<T>`를 구현하는 닷넷프레임워크의 구성 요소는 LINQ to SQL(L2S)과 Entity Framework(EF) 두 가지로 LINQ to DB로 통칭하기도 합니다.  
해석식 질의는 IL 코드 범위에서 작동하는 지역 질의와 달리, Queryable 클래스의 질의 연산자를 통해 산출된 표현식 트리를 닷넷프레임워크가 런타임에 실행합니다.

```sql
create table Account
(
  ID int not null primary key,
  loginName varchar(30),
  displayName varchar(20)
)
insert Account values (1, 'ShapeLayer', '박종현')
insert Account values (2, 'dalcw',      '문성수')
insert Account values (3, 'happyoung',  '오다영')
insert Account values (4, 'Leopard',    '성홍념')
```

```cs
using System;
using System.Linq;
using System.Data.Linq;
using System.Data.Linq.Mapping;

[Table] public class Account
{
  [Column(IsPrimaryKey = true)] public int ID;
  [Column]                      public string loginName;
  [Column]                      public string displayName;
}

class Program
{
  static void Main ()
  {
    DataContext dataContext = new DataContext("");
    Table<Account> accounts = dataContext.GetTable<Account>();

    IQueryable<string> query = from a in accounts
      where   a.loginName.ToUpper().Contains("L")
      orderby a.loginName.Length
      select  a.displayName.SubString(1, 2);

    foreach (string name in query) Console.WriteLine(name);
  }
}
```

L2S는 쿼리를 SQL 쿼리로 변환하고 실행합니다.  
```sql
SELECT [t0].[displayName] AS [value]
FROM [Account] AS [t0]
WHERE UPPER([t0].[loginName]) LIKE @P0
ORDER BY LEN([t0].[loginName])
```

```txt
문성수
성홍념
박종현
```

## 지역 질의와 해석식 질의의 혼용
하나의 쿼리 안에 지역 질의와 해석식 질의를 혼용할 수도 있습니다.  
일반적으로 지역 연산자를 외부에, 해석식 연산자를 내부에 작성합니다. 해석식 질의 결과를 지역 질의의 입력으로 사용하는 것입니다.  

```cs
public static IEnumerable<string> Pair (this IEnumerable<string> source)
{
  string prev = null;
  foreach (string each in source)
  {
    if (prev == null) prev = each;
    else
    {
      yield return $"{prev}, {each}";
      prev = null
    }
  }
}
```

```cs
DataContext dataContext = new DataContext("");
Table<Account> accounts = dataContext.GetTable<Account>();

IEnumerable<string> query = accounts  // 해석식 질의 시작: IQueryable<string>
  .OrderBy (a => -(a.ID))
  .Select  (a => a.displayName)
  .Pair()                             // 지역 질의 시작: IEnumerable<string>
  .Select((n, i) => $"[{i}] {n}");

foreach (string row in query) Console.WriteLine(row);
```

