// NewExercise.cs
using System;

public class NewExercise
{
    public string MuscleGroup { get; set; }
    public string Name { get; set; }
    public int Weight { get; set; }
    public int Sets { get; set; }

    public NewExercise(string muscleGroup, string name, int weight, int sets)
    {
        MuscleGroup = muscleGroup;
        Name = name;
        Weight = weight;
        Sets = sets;
    }
}
