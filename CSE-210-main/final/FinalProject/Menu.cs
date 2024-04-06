// Menu.cs
using System;

public class Menu
{
    public static void DisplayMenu()
    {
        Console.WriteLine("Menu:");
        Console.WriteLine("1. New Workout");
        Console.WriteLine("2. Load Workout");
        Console.WriteLine("3. Save Workout");
        Console.WriteLine("4. Exit");
    }

    public static void ProcessChoice(int choice)
    {
        switch (choice)
        {
            case 1:
                NewWorkout();
                break;
            case 2:
                LoadWorkout();
                break;
            case 3:
                SaveWorkout();
                break;
            case 4:
                ExitProgram();
                break;
            default:
                Console.WriteLine("Invalid choice. Please select again.");
                break;
        }
    }

    private static void NewWorkout()
    {
        Console.WriteLine("Creating a new workout...");
        // Call function to create a new workout
    }

    private static void LoadWorkout()
    {
        Console.WriteLine("Loading a workout...");
        // Call function to load a workout
    }

    private static void SaveWorkout()
    {
        Console.WriteLine("Saving the workout...");
        // Call function to save the workout
    }

    private static void ExitProgram()
    {
        Console.WriteLine("Exiting the program...");
        Environment.Exit(0);
    }
}
