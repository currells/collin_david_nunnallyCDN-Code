using System;
using System.Security.Cryptography.X509Certificates;

// Class: Job
    // Responsibilities:
        // Keeps track of the company, job title, start year, and end year.
    // Behaviors:
        // Displays the job information in the format "Job Title (Company) StartYear-EndYear", for example: "Software Engineer (Microsoft) 2019-2022".
// Class: Resume
    // Responsibilities:
        // Keeps track of the person's name and a list of their jobs.
    // Behaviors:
        // Displays the resume, which shows the name first, followed by displaying each one of the jobs.


// Resume class
// _name :String
// _jobs : List<Job>

// Display() : void
public class Job
{
        public string _name;
        public List<Job>
        public void Display()

}

// Job class
// _company : String
// _jobTitle : String
// _startYear : int
// _endYear : int

// Display : void
public class Resume
{
    public string _company;
    public string _jobTitle;
    public int _startYear;
    public int _endYear;
    public void Display()
}