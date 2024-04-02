using System;
using System.Collections.Generic;

// Base class for all types of goals
public abstract class Goal
{
    public string Name { get; set; }
    public int Points { get; protected set; }

    // Method to record completion of the goal
    public abstract void RecordCompletion();
}

// Simple goal class
public class SimpleGoal : Goal
{
    public SimpleGoal(string name, int points)
    {
        Name = name;
        Points = points;
    }

    // Record completion of the simple goal
    public override void RecordCompletion()
    {
        Console.WriteLine($"Completed simple goal: {Name}. You gained {Points} points.");
    }
}

// Eternal goal class
public class EternalGoal : Goal
{
    public EternalGoal(string name, int points)
    {
        Name = name;
        Points = points;
    }

    // Record completion of the eternal goal
    public override void RecordCompletion()
    {
        Console.WriteLine($"Recorded completion of eternal goal: {Name}. You gained {Points} points.");
    }
}

// Checklist goal class
public class ChecklistGoal : Goal
{
    public int TargetCount { get; private set; }
    private int completedCount;

    public ChecklistGoal(string name, int points, int targetCount)
    {
        Name = name;
        Points = points;
        TargetCount = targetCount;
    }

    // Record completion of the checklist goal
    public override void RecordCompletion()
    {
        completedCount++;
        Console.WriteLine($"Completed {Name} ({completedCount}/{TargetCount}). You gained {Points} points.");
        if (completedCount == TargetCount)
        {
            Console.WriteLine($"Congratulations! You have achieved the checklist goal {Name} and earned a bonus.");
            Points += 500; // Bonus points
        }
    }
}

// Menu class to handle user interactions
public class Menu
{
    private List<Goal> goals = new List<Goal>();
    private int totalScore = 0;

    // Add new goal
    public void AddGoal(Goal goal)
    {
        goals.Add(goal);
    }

    // Record completion of a goal
    public void RecordCompletion(int index)
    {
        if (index >= 0 && index < goals.Count)
        {
            goals[index].RecordCompletion();
            totalScore += goals[index].Points;
        }
        else
        {
            Console.WriteLine("Invalid goal index.");
        }
    }

    // Display user's score and list of goals
    public void DisplayStatus()
    {
        Console.WriteLine($"Your total score: {totalScore}");
        Console.WriteLine("List of goals:");
        for (int i = 0; i < goals.Count; i++)
        {
            Console.WriteLine($"[{i + 1}] {goals[i].Name}");
        }
    }
}
