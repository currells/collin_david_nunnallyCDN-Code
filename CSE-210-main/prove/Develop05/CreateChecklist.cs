public class CreateChecklist : CreateGoal
{
    private string _checklistGoalCDN;
    private string _checklistDescCDN;
    private int _checklistQntyCDN;
    private int _checklistValueCDN;
    private int _checklistBonusCDN;
    private string _checklistFullReturnCDN;
    private int _checklistCompleted;

    public CreateChecklist(string newchecklist, string description, int quanity, int value, int bonus, int completed)
    {
        _checklistGoalCDN = newchecklist;
        _checklistDescCDN = description
        _checklistQntyCDN = quanity;
        _checklistValueCDN = value;
        _checklistBonusCDN = bonus;
        _checklistCompleted = completed

        Console.WriteLine("What is the name of your goal? ")
        string newchecklist = Console.ReadLine();

        Console.WriteLine("Give a description of your goal. ")
        string description = Console.ReadLine();

        Console.WriteLine("What are the ammount of points associated with this goal? ");
        int value = Console.ReadLine();

        Console.WriteLine("How many times does the goal need to be accomplished for the bonus? ");
        int quanity = Console.ReadLine();

        Console.WriteLine("What is the bonus for accomplishing the goal? ");
        int bonus = Console.ReadLine();

        _checklistFullReturnCDN = $"{newchecklist}:{description}:{value}:{bonus}{quanity}:{completed}";
    }

    public override string NewGoal()
    {
        return _checklistFullReturnCDN
    }
}


// Provide for a checklist goal that must be accomplished a certain number of times to be complete. Each time the user records this goal they gain some value, but when they achieve the desired amount, they get an extra bonus.

// For example, if you set a goal to attend the temple 10 times, you might get 50 points each time you go, and then a bonus of 500 points on the 10th time.