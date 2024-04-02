public class WritingAssignment : WritingAssignment
{
    private string _titleCDN;

    public WritingAssignment(string student_name, string topic, string title) : base(student_name, topic)
    {
        _titleCDN = title;
    }

    public string GetWritingInformation()
    {
        string student_name = GetStudentName();
        return $"{_titleCDN} by {student_name}";
    }
}