using System;

class Program
{
    static void Main(string[] args)
    {
        Fraction f1 = new Fraction();
        Console.WriteLine(f1.GetFractionStringCDN());
        Console.WriteLine(f1.GetDecimalValueCDN());

        Fraction f2 = new Fraction(10);
        Console.WriteLine(f2.GetFractionStringCDN());
        Console.WriteLine(f2.GetDecimalValueCDN());

        Fraction f3 = new Fraction(5 , 6);
        Console.WriteLine(f3.GetFractionStringCDN());
        Console.WriteLine(f3.GetDecimalValueCDN());

        Fraction f4 = new Fraction(5 , 10);
        Console.WriteLine(f4.GetFractionStringCDN());
        Console.WriteLine(f4.GetDecimalValueCDN());
    }
}