using System;
using System.Collections.Generic;
using System.Threading;

public class Timer
{
    public void ShowSpinner(int durationInSeconds)
    {
        int durationInMilliseconds = durationInSeconds * 1000;
        int spinnerDuration = 500; // milliseconds
        int iterations = durationInMilliseconds / spinnerDuration;

        for (int i = 0; i < iterations; i++)
        {
            Console.Write("+");
            Thread.Sleep(spinnerDuration);
            Console.Write("\b \b"); // Erase the + character
            Console.Write("-"); // Replace it with the - character
        }
    }

    public void ShowCountdown(int durationInSeconds)
    {
        for (int i = durationInSeconds; i > 0; i--)
        {
            Console.WriteLine($"Time remaining: {i} seconds");
            Thread.Sleep(1000); // 1 second delay
        }
    }
}

public abstract class Activity
{
    protected string name;
    protected string description;
    protected int duration;

    public Activity(string name, string description)
    {
        this.name = name;
        this.description = description;
    }

    public void StartActivity()
    {
        Console.WriteLine($"Starting {name} activity:");
        Console.WriteLine(description);
        Console.Write("Enter duration (in seconds): ");
        duration = int.Parse(Console.ReadLine());

        Timer timer = new Timer();
        timer.ShowCountdown(3); // Pause for 3 seconds before starting
    }

    public abstract void DoActivity();

    public void EndActivity()
    {
        Console.WriteLine("Good job!");
        Console.WriteLine($"You have completed {name} activity in {duration} seconds.");

        Timer timer = new Timer();
        timer.ShowCountdown(3); // Pause for 3 seconds before ending
    }
}

public class BreathingActivity : Activity
{
    public BreathingActivity() : base("Breathing", "This activity will help you relax by walking you through breathing in and out slowly. Clear your mind and focus on your breathing.")
    {
    }

    public override void DoActivity()
    {
        Console.WriteLine("Breathe in...");
        Timer timer = new Timer();
        timer.ShowCountdown(duration);

        Console.WriteLine("Breathe out...");
        timer.ShowCountdown(duration);

        EndActivity();
    }
}

public class Reflection
{
    public string Prompt { get; }
    public List<string> Questions { get; }

    public Reflection(string prompt, List<string> questions)
    {
        Prompt = prompt;
        Questions = questions;
    }
}

public class ReflectionActivity : Activity
{
    private List<Reflection> reflectionPrompts;

    public ReflectionActivity() : base("Reflection", "This activity will help you reflect on times in your life when you have shown strength and resilience. This will help you recognize the power you have and how you can use it in other aspects of your life.")
    {
        InitializeReflectionPrompts();
    }

    private void InitializeReflectionPrompts()
    {
        reflectionPrompts = new List<Reflection>
        {
            new Reflection("Think of a time when you stood up for someone else.", new List<string>
            {
                "Why was this experience meaningful to you?",
                "Have you ever done anything like this before?",
                "How did you get started?",
                "How did you feel when it was complete?",
                "What made this time different than other times when you were not as successful?",
                "What is your favorite thing about this experience?",
                "What could you learn from this experience that applies to other situations?",
                "What did you learn about yourself through this experience?",
                "How can you keep this experience in mind in the future?"
            }),
            // Add more prompts as needed
        };
    }

    public override void DoActivity()
    {
        Random random = new Random();
        int index = random.Next(reflectionPrompts.Count);
        Reflection selectedPrompt = reflectionPrompts[index];

        Console.WriteLine(selectedPrompt.Prompt);

        Timer timer = new Timer();

        foreach (string question in selectedPrompt.Questions)
        {
            Console.WriteLine(question);
            timer.ShowSpinner(3); // Pause for 3 seconds with spinner
        }

        EndActivity();
    }
}

public class ListingActivity : Activity
{
    public ListingActivity() : base("Listing", "This activity will help you reflect on the good things in your life by having you list as many things as you can in a certain area.")
    {
    }

    public override void DoActivity()
    {
        string[] prompts = {
            "Who are people that you appreciate?",
            "What are personal strengths of yours?",
            "Who are people that you have helped this week?",
            "When have you felt the Holy Ghost this month?",
            "Who are some of your personal heroes?"
        };

        Random random = new Random();
        int index = random.Next(prompts.Length);

        Console.WriteLine(prompts[index]);
        Console.WriteLine("You have 10 seconds to list as many items as you can:");

        Timer timer = new Timer();
        timer.ShowCountdown(10); // Give 10 seconds for listing items

        Console.WriteLine("Time's up!");

        // Simulated count of listed items
        int itemCount = random.Next(1, 11);
        Console.WriteLine($"You listed {itemCount} items.");

        EndActivity();
    }
}

public class Menu
{
    public void ShowMenu()
    {
        while (true)
        {
            Console.WriteLine("Menu:");
            Console.WriteLine("1. Breathing Activity");
            Console.WriteLine("2. Reflection Activity");
            Console.WriteLine("3. Listing Activity");
            Console.WriteLine("4. Exit");

            Console.Write("Enter your choice: ");
            int choice = int.Parse(Console.ReadLine());

            Activity activity = null;

            switch (choice)
            {
                case 1:
                    activity = new BreathingActivity();
                    break;
                case 2:
                    activity = new ReflectionActivity();
                    break;
                case 3:
                    activity = new ListingActivity();
                    break;
                case 4:
                    Console.WriteLine("Exiting...");
                    return;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }

            if (activity != null)
            {
                activity.StartActivity();
                activity.DoActivity();
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Menu menu = new Menu();
        menu.ShowMenu();
    }
}
