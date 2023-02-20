using System;
using System.Text;
using System.Collections;

public class Program
{
  public static void Main (string[] args)
  {
    Console.WriteLine("값 상등");
    ValueEquals.Run();
    Console.WriteLine("참조 상등");
    ReferenceEquals_.Run();
    Console.WriteLine("Object.Equals 상등 1");
    ObjectEqualsBasic.Run();
    Console.WriteLine("Object.Equals 상등 2");
    ObjectEqualsAndOperEquals.Run();
    Console.WriteLine("double.NaN 상등");
    NaNEquals.Run();
    Console.WriteLine("StringBuilder 상등");
    StringBuilderEquals.Run();
  }
}

public class ValueEquals
{
  public static void Run ()
  {
    int x = 5, y = 5;
    Console.WriteLine(x == y); // True
  }
}

public class ReferenceEquals_
{
  class Foo { public int x; }
  public static void Run ()
  {
    Foo foo = new Foo { x = 5 };
    Foo var = new Foo { x = 5 };
    Console.WriteLine(foo == var); // False
    foo = var;
    Console.WriteLine(foo == var); // True
  }
}

public class ObjectEqualsBasic
{
  public static void Run ()
  {
    object x = -1, y = -1;
    Console.WriteLine(object.Equals(x, y)); // True
    x = null;
    Console.WriteLine(object.Equals(x, y)); // False
    y = null;
    Console.WriteLine(object.Equals(x, y)); // True
  }
}

public class ObjectEqualsAndOperEquals
{
  public static void Run ()
  {
    object x = 5, y = 5;
    Console.WriteLine(x == y); // False
    Console.WriteLine(x.Equals(y)); // True
  }
}

public class NaNEquals
{
  public static void Run ()
  {
    double x = double.NaN;
    Console.WriteLine(x == x); // False: 값 상등
    Console.WriteLine(x.Equals(x)); // True: 참조 상등 (반사적 상등)
  }
}

public class StringBuilderEquals
{
  public static void Run ()
  {
    var sba = new StringBuilder("foo");
    var sbb = new StringBuilder("foo");
    Console.WriteLine(sba == sbb); // False: 값 상등
    Console.WriteLine(sba.Equals(sbb)); // True: 값 상등
  }
}
