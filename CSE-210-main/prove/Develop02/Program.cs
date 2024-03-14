using System;
using System.Collections.Generic;
using System.IO;

class Entry
{
    public string Prompt { get; set; }
    public string Response { get; set; }
    public DateTime Date { get; set; }

    public Entry(string prompt, string response)
    {
        Prompt = prompt;
        Response = response;
        Date = DateTime.Now; 
    }

    public override string ToString() //Entry layout
    {
        return $"Date: {Date}\nPrompt: {Prompt}\nResponse: {Response}\n";
    } 
}

class JournalApp //This gets the prompts and allows the random generation later in the code
{
    private List<Entry> journal = new List<Entry>();
    private List<string> prompts = new List<string>()
    {
        "Who was the most interesting person I interacted with today?",
        "What was the best part of my day?",
        "How did I see the hand of the Lord in my life today?",
        "What was the strongest emotion I felt today?",
        "If I had one thing I could do over today, what would it be?"
    };

    public void Run()
    {
        while (true)
        {
            Console.WriteLine("\nMENU:");
            Console.WriteLine("1. Write a new entry");
            Console.WriteLine("2. Display the journal");
            Console.WriteLine("3. Save the journal to a file");
            Console.WriteLine("4. Load the journal from a file");
            Console.WriteLine("5. Exit");

            Console.Write("Enter your choice: ");
            string choice = Console.ReadLine();
                
            switch (choice) // switch / case is like else/elif statements in Python
            {
                case "1":
                    WriteNewEntry();
                    break;
                case "2":
                    DisplayJournal();
                    break;
                case "3":
                    SaveJournal();
                    break;
                case "4":
                    LoadJournal();
                    break;
                case "5":
                    return;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    private void WriteNewEntry()
    {
        Random rnd = new Random();
        string prompt = prompts[rnd.Next(prompts.Count)];

        Console.WriteLine($"Prompt: {prompt}"); //Displays a random prompt using the random in code above
        Console.Write("Your response: ");
        string response = Console.ReadLine();

        Entry newEntry = new Entry(prompt, response); //Ties the entry and response to the Entry class. Date comes from 'Date = DateTime.Now;'
        journal.Add(newEntry);
        Console.WriteLine("Entry added successfully.");
    }

    private void DisplayJournal()
    {
        Console.WriteLine("\n--- Journal Entries ---");
        foreach (var entry in journal)
        {
            Console.WriteLine(entry); //Displays the entries in Entry
        }
    }

    private void SaveJournal() //Saves all Entry into the file given
    {
        Console.Write("Enter filename to save: ");
        string filename = Console.ReadLine();

        try
        {
            using (StreamWriter writer = new StreamWriter(filename))
            {
                foreach (var entry in journal)
                {
                    writer.WriteLine($"{entry.Date};{entry.Prompt};{entry.Response}");
                }
            }

            Console.WriteLine("Journal saved successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error saving journal: {ex.Message}");
        }
    }

    private void LoadJournal() //Loads a file 
    {
        Console.Write("Enter filename to load: ");
        string filename = Console.ReadLine();

        try
        {
            journal.Clear();

            using (StreamReader reader = new StreamReader(filename))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] parts = line.Split(';');
                    DateTime date = DateTime.Parse(parts[0]);
                    string prompt = parts[1];
                    string response = parts[2];
                    Entry entry = new Entry(prompt, response);
                    entry.Date = date;
                    journal.Add(entry);
                }
            }

            Console.WriteLine("Journal loaded successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error loading journal: {ex.Message}");
        }
    }
}

class Program //Runs the Journal app, which is the 'Main'
{
    static void Main(string[] args)
    {
        JournalApp app = new JournalApp();
        app.Run();
    }
}
