"""
Author: Collin Nunnally
File: prove_03.py

Ask the user for the price of a child and an adult meal 
and store these values properly into variables as 
floating point numbers.

Ask the user for the number of adults and children and 
store these values properly into variables as integers.

Ask the user for the sales tax rate and 
store the value properly as a floating point number.

Compute and display the subtotal 
(don't worry about rounding to two decimals at this point).

Ask the user for the the payment amount (floating point)

Compute and display the change.
"""
white = "\033[0;37m"
gray = "\033[39m"
blue = "\033[0;34m"
red = "\033[0;31m"

# Asks the questions to get prices
child = float(input("\nWhat is the child's meal price? $"))
adult = float(input("What is the adult's meal price? $"))
child_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))
print(f"{white}Values is divided by 100, so 6% Sales Tax is 6.{gray}")
tax = float(input("What is the sales tax? "))

# Calculating price of adult and child totals
child_price = child * child_count
adult_price = adult * adult_count

# Adds totals together
sub_total = child_price + adult_price
sales_tax = (tax / 100) * sub_total
total = sub_total + sales_tax

# Rounding values so there is 2 decimals
sales_tax = round(sales_tax, 2)
sub_total = round(sub_total, 3)
total = round(total, 2)

# Displays totals
print(f"\n{blue}Subtotal: ${sub_total}")
print(f"\nSales Tax: ${sales_tax}")
print(f"\nTotal: ${total}{gray}")

payment = float(input("\nWhat is the payment amount? "))

# Displays change 
change = payment - total
owe = total - payment
grand = '%.2f' % change #Makes the change only have 2 decimals

# Only 2 decimals
owe = round(owe, 2)

# Statement to make sure they pay enough
if payment < total:
    print(f"{red}You still owe ${owe}{gray}.")
else:
    print(f"\n{blue}Change: ${grand}{gray}\n")