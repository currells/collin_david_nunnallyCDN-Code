"""

students: unathletic avengers
teacher: brother keers
assignment: 05 Teach: Team Activity
file: grading.py

"""

percent = float(input("What is your grade percent? "))

# setting the default grade and status to A and passing
status = "passing"

# determine what the letter grade should be based on the percentage given
if percent >= 90:
    letter_grade = ("A")
elif percent >= 80:
    letter_grade = ("B")
elif percent >= 70:
    letter_grade = ("C")
elif percent >= 60:
    letter_grade = ("D")
else:
    letter_grade = ("F")

# figure out the symbol, if any, to follow the letter grade
sign = ""
if percent % 10 <= 3:
    sign = "-"
elif (percent % 10) >= 7:
    sign = "+"

# remove A+ and F-
if percent >= 93 or letter_grade == "F":
    sign = ""

# return the grade to the user
print(f"\nYour letter grade is: {letter_grade}{sign}")


# inform the user whether or not they passing the course or not
if percent <= 69:
    status = "failing"
    print(f"You have a {status} grade.")
else:
    print(f"You have a {status} grade!")

