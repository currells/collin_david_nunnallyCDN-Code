// NewWorkout.cs
using System;
using System.Collections.Generic;

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
