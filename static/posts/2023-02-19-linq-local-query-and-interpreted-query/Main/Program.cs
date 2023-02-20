using System;
using System.Collections.Generic;
using System.Linq;
using System.Data.Linq;
using System.Data.Linq.Mapping;

public class Program
{
  public static void Main (string[] args)
  {
    LocalQuery.Run();
    InterpretedQuery.Run();
    MixedQuery.Run();
  }
}

public class LocalQuery
{
  public static void Run ()
  {
    string[] languages = { "C", "C++", "Java", "C#", "Go", "Rust", "Python" };
    IEnumerable<string> query =
      from language in languages
      select language.Replace("+", "p")
                     .Replace("#", "sharp")
      into langNoSymbol
        where   langNoSymbol.Length > 2
        orderby langNoSymbol
        select  langNoSymbol;
    foreach (string lang in query) Console.WriteLine(lang);
  }
}

public class InterpretedQuery
{
  public static void Run ()
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

public static class Extension
{
  public static IEnumerable<string> Pair (this IEnumerable<string> source)
  {
    string prev = null;
    foreach (string each in source)
    {
      if (prev == null) prev = each;
      else
      {
        yield return $"{prev}, {each}";
        prev = null;
      }
    }
  }
}

public class MixedQuery
{
  public static void Run ()
  {
    DataContext dataContext = new DataContext("");
    Table<Account> accounts = dataContext.GetTable<Account>();

    IEnumerable<string> query = accounts  // 해석식 질의 시작: IQueryable<string>
      .OrderBy (a => -(a.ID))
      .Select  (a => a.displayName)
      .Pair()                             // 지역 질의 시작: IEnumerable<string>
      .Select((n, i) => $"[{i}] {n}");

    foreach (string row in query) Console.WriteLine(row);
  }
}
