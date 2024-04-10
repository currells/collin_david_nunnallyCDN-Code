using System;
using System.Collections.Generic;
using System.IO;

abstract class Workout
{
    public string Exercise { get; set; }
    public int Sets { get; set; }
    public int Reps { get; set; }
    public double Weight { get; set; }
    public DateTime Date { get; set; }

    public abstract double CalculateTotalVolume();
}

class StrengthWorkout : Workout
{
    public override double CalculateTotalVolume()
    {
        return Sets * Reps * Weight;
    }
}

class CardioWorkout : Workout
{
    public double Distance { get; set; }
    public TimeSpan Duration { get; set; }

    public override double CalculateTotalVolume()
    {
        return 0;
    }
}

class Program
{
    static List<Workout> workouts = new List<Workout>();
    const string dataFilePath = "workout_data.txt";

    static void Main(string[] args)
    {
        LoadWorkoutData();

        Console.WriteLine("Welcome to the Gym Workout Tracker!");
        Console.WriteLine("Select an option from below:");

        while (true)
        {
            Console.WriteLine("\n1. Add Workout");
            Console.WriteLine("2. View Workouts");
            Console.WriteLine("3. Exit");
            Console.Write("Select an option: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    AddWorkout();
                    SaveWorkoutData();
                    break;
                case "2":
                    ViewWorkouts();
                    break;
                case "3":
                    Console.WriteLine("Exiting program...");
                    return;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
        }
    }

    static void AddWorkout()
    {
        Console.WriteLine("\nEnter workout details:");

        Console.Write("Exercise name: ");
        string exercise = Console.ReadLine();

        Console.Write("Number of sets: ");
        int sets = int.Parse(Console.ReadLine());

        Console.Write("Number of reps: ");
        int reps = int.Parse(Console.ReadLine());

        Console.Write("Weight (in lbs): ");
        double weight = double.Parse(Console.ReadLine());

        char workoutType;

        while (true)
        {
            Console.WriteLine("Is this a strength workout or cardio workout? [Uppercase](S/C)");
            string input = Console.ReadLine().ToUpper();

            if (input == "S" || input == "C")
            {
                workoutType = input[0];
                break;
            }
            else
            {
                Console.WriteLine("Invalid workout type. Please enter 'S' for strength workout or 'C' for cardio workout.");
            }
        }

        Workout workout;
        switch (workoutType)
        {
            case 'S':
                workout = new StrengthWorkout();
                break;
            case 'C':
                workout = new CardioWorkout();
                break;
            default:
                Console.WriteLine("Invalid workout type. Defaulting to strength workout.");
                workout = new StrengthWorkout();
                break;
        }

        workout.Exercise = exercise;
        workout.Sets = sets;
        workout.Reps = reps;
        workout.Weight = weight;
        workout.Date = DateTime.Now;

        workouts.Add(workout);

        double totalWeight = CalculateTotalWeight(workout);
        Console.WriteLine($"\nTotal weight lifted for this workout: {totalWeight} lbs");

        Console.WriteLine("\nWorkout added successfully!");
    }

    static double CalculateTotalWeight(Workout workout)
    {
        return workout.Weight * workout.Reps * workout.Sets;
    }

    static void ViewWorkouts()
    {
        if (workouts.Count == 0)
        {
            Console.WriteLine("No workouts added yet.");
            return;
        }

        Console.WriteLine("\n-- Your Workouts --");
        foreach (var workout in workouts)
        {
            Console.WriteLine($"\nDate: {workout.Date.ToShortDateString()}");
            Console.WriteLine($"Exercise: {workout.Exercise}\nSets: {workout.Sets}\nReps: {workout.Reps}\nWeight: {workout.Weight}lbs");

            double totalWeight = CalculateTotalWeight(workout);
            Console.WriteLine($"Accumulated weight lifted: {totalWeight} lbs");

            Console.WriteLine();
        }
    }

    static void SaveWorkoutData()
    {
        using (StreamWriter writer = new StreamWriter(dataFilePath))
        {
            foreach (var workout in workouts)
            {
                string type = (workout is StrengthWorkout) ? "S" : "C";
                writer.WriteLine($"{type},{workout.Exercise},{workout.Sets},{workout.Reps},{workout.Weight},{workout.Date}");
            }
        }
    }

    static void LoadWorkoutData()
    {
        if (File.Exists(dataFilePath))
        {
            string[] lines = File.ReadAllLines(dataFilePath);
            foreach (var line in lines)
            {
                string[] parts = line.Split(',');
                if (parts.Length >= 6)
                {
                    char typeChar = parts[0][0];
                    string exercise = parts[1];
                    int sets = int.Parse(parts[2]);
                    int reps = int.Parse(parts[3]);
                    double weight = double.Parse(parts[4]);
                    DateTime date = DateTime.Parse(parts[5]);

                    Workout workout;
                    switch (typeChar)
                    {
                        case 'S':
                            workout = new StrengthWorkout();
                            break;
                        case 'C':
                            workout = new CardioWorkout();
                            break;
                        default:
                            workout = new StrengthWorkout();
                            break;
                    }

                    workout.Exercise = exercise;
                    workout.Sets = sets;
                    workout.Reps = reps;
                    workout.Weight = weight;
                    workout.Date = date;

                    workouts.Add(workout);
                }
            }
        }
    }
}
