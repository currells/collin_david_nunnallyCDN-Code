"""
File:   reminders.py
Author: Brother Keers

Purpose: This file serves as a general reminder of what is expected from your
code submissions. I also demonstrate some additional concepts that I forget to
mention in class.

NOTE: Every file you submit should have a header comment like this one
explaining what the does. You can omit the "Purpose" part if you wish and
begin explaining the file after the Author line. Make sure to leave an empty
line of space for readability.
"""

# You can use the string formatter to duplicate strings.
print(f"\n{'-' * 78}")
print("This line is sandwiched between characters you didn't have to manually type.")
print(f"{'-' * 78}\n")

# You can use the formatter to add space after a variable.
name   = "Brother Keers"
office = "ETC 125"
email  = "keersc@byui.edu"
phone  = "(208) 496-7604"
print("These lines do not use any additional spacing:")
print(f"Name: {name} Office: {office}")
print(f"Email: {email} Phone: {phone}\n")

print("These lines use additional spacing to print (look) nicer:")
print(f"Name:  {name:<20} Office: {office}")
print(f"Email: {email:<20} Phone:  {phone}\n")