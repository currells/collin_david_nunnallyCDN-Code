using System;
using System.IO;
using System.Collections.Generic;

namespace WorkoutTracker
{
    public class Introduction
    {
        public static void DisplayIntroduction()
        {
            Console.WriteLine("Welcome to the Workout Tracker Program!");
            System.Threading.Thread.Sleep(500); // Pause for 0.5 seconds
        }
    }

    public class LoadWorkout
    {
        public static void LoadFromFile()
        {
            Console.WriteLine("Enter the file name to load the workout:");
            string fileName = Console.ReadLine();

            try
            {
                // Read workout data from the file
                using (StreamReader reader = new StreamReader(fileName))
                {
                    string workoutData = reader.ReadToEnd();
                    Console.WriteLine($"Workout loaded successfully from {fileName}");
                    Console.WriteLine("Workout Data:");
                    Console.WriteLine(workoutData);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error loading workout: {ex.Message}");
            }
        }
    }

public class Menu
{
    public static void DisplayMenu()
    {
        Console.WriteLine("Menu:");
        Console.WriteLine("1. Create a New Workout");
        Console.WriteLine("2. Load a Workout");
        Console.WriteLine("3. Save the Current Workout");
        Console.WriteLine("4. Exit");
    }

    public static void ProcessChoice(int choice)
    {
        switch (choice)
        {
            case 1:
                CreateNewWorkout();
                break;
            case 2:
                LoadWorkout.LoadFromFile();
                break;
            case 3:
                SaveWorkout.SaveToFile();
                break;
            case 4:
                ExitProgram();
                break;
            default:
                Console.WriteLine("Invalid choice. Please select again.");
                break;
        }
    }

    private static void CreateNewWorkout()
    {
        NewWorkout newWorkout = new NewWorkout();
        // You may want to add logic here to interact with the new workout object,
        // such as adding exercises to it.
    }

    private static void ExitProgram()
    {
        Console.WriteLine("Exiting the program...");
        Environment.Exit(0);
    }
}


    public class MuscleGroupLoader : LoadWorkout
    {
        public static void LoadByMuscleGroup(string fileName, string muscleGroup)
        {
            // Implement loading exercises by muscle group logic here
            Console.WriteLine($"Loading exercises for muscle group: {muscleGroup} from file: {fileName}");
        }
    }

    public class NewExercise
    {
        public string MuscleGroup { get; set; }
        public string Name { get; set; }
        public int Weight { get; set; }
        public int Sets { get; set; }

        public NewExercise()
        {
            Console.WriteLine("Enter muscle group:");
            MuscleGroup = Console.ReadLine();

            Console.WriteLine("Enter exercise name:");
            Name = Console.ReadLine();

            Console.WriteLine("Enter weight (in pounds):");
            // Input validation for weight
            int weight;
            while (!int.TryParse(Console.ReadLine(), out weight) || weight <= 0)
            {
                Console.WriteLine("Invalid input. Please enter a positive integer for weight:");
            }
            Weight = weight;

            Console.WriteLine("Enter number of sets:");
            // Input validation for sets
            int sets;
            while (!int.TryParse(Console.ReadLine(), out sets) || sets <= 0)
            {
                Console.WriteLine("Invalid input. Please enter a positive integer for sets:");
            }
            Sets = sets;
        }
    }

    public class NewWorkout
    {
        public List<NewExercise> Gains { get; private set; }
        public DateTime Date { get; private set; }

        public NewWorkout()
        {
            Gains = new List<NewExercise>();
            Date = DateTime.Now;
        }

        public void AddExercise(NewExercise exercise)
        {
            Gains.Add(exercise);
        }
    }

    public class SaveWorkout
    {
        public static void SaveToFile()
        {
            Console.WriteLine("Enter the file name to save the workout:");
            string fileName = Console.ReadLine();

            try
            {
                // Write workout data to the file
                using (StreamWriter writer = new StreamWriter(fileName))
                {
                    // Write workout data here
                    writer.WriteLine("Workout data goes here...");
                }

                Console.WriteLine($"Workout saved successfully to {fileName}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error saving workout: {ex.Message}");
            }
        }
    }
}
