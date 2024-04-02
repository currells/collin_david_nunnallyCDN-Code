using System;

class Program
{
    static void Main(string[] args)
    {
        Menu menu = new Menu();

        // Adding goals
        menu.AddGoal(new SimpleGoal("Run a marathon", 1000));
        menu.AddGoal(new EternalGoal("Read scriptures", 100));
        menu.AddGoal(new ChecklistGoal("Attend the temple", 50, 10));

    }
}