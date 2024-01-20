"""
Name: Maydens of Mayham (BC, CN, PT, JH, ZM)
Class: CSE-111
Comments:

Ex. Output:
> python fitness.py
Please enter your gender (M or F): F
Enter your birthdate (YYYY-MM-DD): 2001-03-21
Enter your weight in U.S. pounds: 125
Enter your height in U.S. inches: 54
Age (years): 19
Weight (kg): 56.70
Height (cm): 137.2
Body mass index: 30.1
Basal metabolic rate (kcal/day): 1315

> python fitness.py
Please enter your gender (M or F): M
Enter your birthdate (YYYY-MM-DD): 2003-11-26
Enter your weight in U.S. pounds: 145
Enter your height in U.S. inches: 58
Age (years): 17
Weight (kg): 65.77
Height (cm): 147.3
Body mass index: 30.3
Basal metabolic rate (kcal/day): 1580
"""
from datetime import datetime

# 1. Asks the user to enter four values:
    # a. gender
    # b. birthdate in this format: YYYY-MM-DD
    # c. weight in U.S. pounds
    # d. height in U.S. inches
def mom_get_gender():
    p_gender = input("Please enter your gender (M or F): ")
    return p_gender
def mom_get_birthdate():
    p_birth = input("Enter your birthdate (YYYY-MM-DD): ")
    return p_birth
def mom_get_weight():
    p_pounds = float(input("Enter your weight in U.S. pounds: "))
    return p_pounds
def mom_get_height():
    p_inches = float(input("Enter your height in U.S. inches: "))
    return p_inches

# 4. Calculates age (From Team Activity Page)
def compute_age(p_birth):
    """ 
    Compute and return a person's age in years. Parameter birth_str: a person's birthdate stored as a string in this format: YYYY-MM-DD 
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(p_birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    print(f"Age (years): ")
    return years

# 2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
def mom_compute_pounds_kg(p_pounds):
    kg = p_pounds * 0.45359237
    return kg

# 3. Converts inches to centimeters (1 in = 2.54 cm).
def mom_compute_inches_cm(p_inches):
    cm = p_inches * 2.54
    return cm

# 4. Calculates BMI, and BMR.
def mom_compute_bmi(kg, cm):
    # Takes kg and cm from above functions and computes BMI
    bmi = (10000 * kg) / (cm * cm)
    return bmi

def mom_compute_basal(kg, cm, years, p_gender):
    # Determines the gender and uses the appropriate equation to determine bmr
    if p_gender == "F":
        bmr = 447.593 + (9.247 * kg) + (3.098 * cm) - (4.330 * years)
    else:
        bmr = 88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * years)
    return bmr

# 5. Prints age, weight in kg, height in cm, BMI, and BMR.
def main():
    # Recalls get and compute functions with its parameters. Prints the info
    p_gender = mom_get_gender()
    p_birth = mom_get_birthdate()
    p_weight = mom_get_weight()
    p_height = mom_get_height()

    years = compute_age(p_birth)
    kg = mom_compute_pounds_kg(p_weight)
    cm = mom_compute_inches_cm(p_height)
    bmi = mom_compute_bmi(kg, cm)
    bmr = mom_compute_basal(kg, cm, years, p_gender)

    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.2f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

main()
