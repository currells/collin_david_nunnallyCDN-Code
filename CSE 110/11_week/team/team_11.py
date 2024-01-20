"""
Author: Unathletic Avengers
Teacher: Brother Keers
File: team_11.py
Assignment: write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.

"""

# 01. Download the file and save it to your computer. In VS Code, open the folder that contains this file. Then, create a new Python script in that folder.

NAME_INDEX = 0
ID_INDEX = 1
JOB_INDEX = 2
SAL_INDEX = 3

with open("hr_system.txt", "r") as hr_file:
  # 01. Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.
  for line in hr_file:
    column = line.split(" ")
    # 02. Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
    # S01: Strip off any leading and trailing whitespace from each line.
    employee_name = column[NAME_INDEX].strip()
    employee_id = column[ID_INDEX].strip()
    # 03. For each line, get the name and the job title for each person, and display those to the screen.
    employee_job = column[JOB_INDEX].strip()
    employee_sal = int(column[SAL_INDEX].strip())
    if employee_job == "Engineer":
      employee_sal = employee_sal + 1000

    # S01: In addition to the name and the job title, also access the salary and the ID number and save them into variables. Display all four values in this format: name (ID: id_number), job_title - $salary. Don't forget to convert the salary to a number and display it with two decimals.
    print(
      f"{employee_name} (ID: {employee_id}), {employee_job} - ${employee_sal / 24:,.2f}"
    )
# S02: Instead of displaying the salary information, calculate and display a paycheck amount for the employee. Assume that they are paid twice a month.

# S03: Change the program so that it generates bonuses for anyone who is an engineer. For each of these employees, add $1000 to their paycheck amount.
