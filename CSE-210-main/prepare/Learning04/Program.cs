using System;

class Program
{
    static void Main(string[] args)
    {
        Assignment a1 = new Assignment("Collin Nunnally" , "Geometry");
        Console.WriteLine(a1.GetSummary());

        MathAssignment a2 = new MathAssignment("Jacob Mymony" , "Fractions" , "5.1" , "7.2");
        Console.WriteLine(a2.GetSummary);
        Console.WriteLine(a2.GetHomeworkList);

        WritingAssignment a3 = new WritingAssignment("Who Dinie" , "World Lit" , "Emancipation Proclamation");
        Console.WriteLine(a3.GetSummary);
        Console.WriteLine(a3.GetWritingInformation);
    }
}