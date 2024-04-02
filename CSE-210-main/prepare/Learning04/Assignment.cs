public class Assignment
{
    private string _studentNameCDN;
    private string _topicCDN;

    public Assignment(string student_name, string topic)
    {
        _studentNameCDN = student_name;
        _topicCDN = topic;
    }

    public string GetStudentName()
    {
        return _studentNameCDN;
    }

    public string GetTopic()
    {
        return _topicCDN;
    }

    public string GetSummary()
    {
        return _studentNameCDN + " " + _topicCDN;
    }
}