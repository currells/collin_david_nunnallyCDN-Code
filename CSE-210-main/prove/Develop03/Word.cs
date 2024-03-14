using System;
using System.Collections.Generic;

public class Word
{
    public static List<string> RemoveWords(string verse, int numWordsToRemove)
    {
        List<string> words = new List<string>(verse.Split(' '));
        if (numWordsToRemove >= words.Count)
        {
            return new List<string>(); // Return empty list if trying to remove more words than available
        }
        words.RemoveRange(0, numWordsToRemove);
        return words;
    }
}
