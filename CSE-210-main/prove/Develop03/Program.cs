using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to Scripture Memorization Program!");

        Console.WriteLine("Enter standard work (e.g., Bible, Book of Mormon, Doctrine and Covenants):");
        string standardWork = Console.ReadLine();

        Console.WriteLine("Enter book:");
        string book = Console.ReadLine();

        Console.WriteLine("Enter chapter:");
        int chapter = int.Parse(Console.ReadLine());

        Console.WriteLine("Enter verse:");
        int verse = int.Parse(Console.ReadLine());

        string verseText = Reference.GetVerse(standardWork, book, chapter, verse);
        Console.WriteLine($"Verse: {verseText}");

        Console.WriteLine("Enter the number of words to remove for memorization:");
        int numWordsToRemove = int.Parse(Console.ReadLine());

        var modifiedVerse = Word.RemoveWords(verseText, numWordsToRemove);
        Console.WriteLine("Modified Verse for Memorization:");
        foreach (string word in modifiedVerse)
        {
            Console.WriteLine(word);
        }

        Console.WriteLine("Memorization complete!");

        // You can add more functionality as needed
    }
}
