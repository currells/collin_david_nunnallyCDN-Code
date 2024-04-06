// MuscleGroupLoader.cs
using System;

public class MuscleGroupLoader : LoadWorkout
{
    public static void LoadByMuscleGroup(string fileName, string muscleGroup)
    {
        // Implement loading exercises by muscle group logic here
        Console.WriteLine($"Loading exercises for muscle group: {muscleGroup} from file: {fileName}");
    }
}
