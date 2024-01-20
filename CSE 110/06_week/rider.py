"""

group: Unathletic Avengers
teacher: Brother Keers
file: team_6
goal: work as a team to write a program for a fictitious amusement park ride

"""

# The basic rules are as follows:
# 1. No one under 36 inches may ever ride, either by themselves or with another rider.
# 2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# 3. If there are two riders and one of them is at least 18 years old, they may ride together.



# CORE REQUIREMENTS
# 1. Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.
age1 = int(input("What is the first riders age? "))
height1 = int(input("What is the height of the first rider in inches? "))
second_rider = input("is there a second rider (yes/no)?").lower()
can_ride1 = True
can_ride2 = True

if height1 <= 36:
    not can_ride1

if second_rider == "yes":
    age2 = int(input("What is the first riders age? "))
    height2 = int(input("What is the height of the first rider in inches? "))
    if age1 or age2 >= 18:
        pass
    else:
        not can_ride1
else:
    if age1 >= 18 and height1 >= 62:
        pass

# 2. Handle the case of a single rider.

# 3. Finish implementing the basic rules.