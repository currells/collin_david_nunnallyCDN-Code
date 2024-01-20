"""
Author: Collin Nunnally
File: prepare_06.py

Creating a program to see if someone qualifies for a loan

Requirements:
First, ask for a rating from 1–10 on the following:
How large is the loan?
How good is your credit history?
How high is your income?
How large is your down payment?

    First, check if the loan size is at least 5. If it is, use the following rules:
If the credit history and income are both at least 7, then the decision is "yes"
If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
    Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
    Otherwise (if the loan is not 5 or greater), use these rules:
If the credit is less than 4, then the decision is "no"
    Otherwise, check the following:
If either the income or the down payment is at least 7, the decision is "yes"
If both the income and the down payment are at least 4, then the answer is "yes"
    Otherwise, the decision is "no"
"""
# input colors and then coloring the pass green and fail red
red = "\033[0;31m"
green = "\033[0;32m"
gray = "\033[39m"

yes = ("You passed! 😄")
no = ("You did not pass. 🥺")
yes = (f"{green}{yes}{gray}") 
no = (f"{red}{no}{gray}")

#Asking questions
print("Answer the following questions, rating them 1-10:\n")
loan = float(input("How large is the loan? "))
credit = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down = float(input("How large is your down payment? "))


if loan >= 5:
    if credit >= 7 and income >= 7:
        print(f"{yes}")
    elif credit >= 7 or income >= 7:
        if down >= 5:
            print(f"{yes}")
        else:
            print(f"{no}")
    else:
        print(f"{no}")
elif loan <= 5:
    if credit <= 4:
        print(f"{no}")
    else:
        if income  >= 7 or down >= 7:
            print(f"{yes}")
        elif income >= 4 and down >= 4:
            print(f"{yes}")
        else:
            print(f"{no}")

else:
    print(f"{no}")

