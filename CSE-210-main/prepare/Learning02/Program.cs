using System;
using System.Collections.Generic;

public class Job
{
    public string _CDNjobTitle;
    public string _CDNcompany;
    public int _CDNstartYear;
    public int _CDNendYear;

    public void Display()
    {
        Console.WriteLine($"{_CDNjobTitle} ({_CDNcompany}) {_CDNstartYear}-{_CDNendYear}");
    }
}

public class Resume
{
    public string _CDNname;
    public List<Job> _CDNjobs = new List<Job>();

    public void Display()
    {
        Console.WriteLine($"Name: {_CDNname}");
        Console.WriteLine("Jobs:");

        foreach (Job job in _CDNjobs)
        {
            job.Display();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Resume myResume = new Resume();

        Console.Write("Enter your name: ");
        myResume._CDNname = Console.ReadLine();

        for (int i = 1; ; i++)
        {
            Job job = new Job();

            Console.WriteLine($"\nEnter details for job {i} (press Enter to skip):");

            Console.Write("Job title: ");
            job._CDNjobTitle = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(job._CDNjobTitle))
                break;

            Console.Write("Company: ");
            job._CDNcompany = Console.ReadLine();

            Console.Write("Start year: ");
            int.TryParse(Console.ReadLine(), out job._CDNstartYear);

            Console.Write("End year: ");
            int.TryParse(Console.ReadLine(), out job._CDNendYear);

            myResume._CDNjobs.Add(job);
        }

        myResume.Display();
    }
}
