// Program.cs
using System;

class Program
{
    static void Main(string[] args)
    {
        Introduction.DisplayIntroduction();

        bool exitProgram = false;
        while (!exitProgram)
        {
            Menu.DisplayMenu();

            int choice;
            if (!int.TryParse(Console.ReadLine(), out choice))
            {
                Console.WriteLine("Invalid input. Please enter a number.");
                continue;
            }

            Menu.ProcessChoice(choice);
        }

        Console.WriteLine("Exiting the program...");
    }
}
