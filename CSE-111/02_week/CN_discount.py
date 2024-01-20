"""
Name: Maidens of Mayham
Class: CSE-111
Comments:
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
CORE:
1. Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer’s operating system.
2. Your program correctly computes and prints the discount amount if applicable.
3. Your program correctly computes and prints the sales tax amount and the total amount due.

STRETCH:
1. Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need to purchase in order to receive the discount.
2. Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.

Ex Output:
> python discount.py
Please enter the subtotal: 42.75
Sales tax amount: 2.56
Total: 45.31

> python discount.py
Please enter the subtotal: 55.20
Sales tax amount: 3.31
Total: 58.51

***
day_of_week = current_date_and_time.weekday()

temporarily add a line of code like this one:
day_of_week = 2
"""
# Grabs the current day of week from OS
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
"""
Testing day of week, remove #
"""
#day_of_week = 2 

sub_total = int(input("Please enter the subtotal: "))

def compute_total():
    sales_tax = float((sub_total * 0.06))
    total = float((sub_total + sales_tax))
    sales_tax = "${:,.2f}".format(sales_tax)
    total = "${:,.2f}".format(total)

def display_total():
    print(f"Sales tax amount: {sales_tax}")
    print(f"Total: {total}")

def compute_discount():
    if day_of_week == 1 or 2 and sub_total >= 50:
        discount = total * 0.1
        discount = "${:,.2f}".format(discount)
        disc_total = total - discount
        disc_total = "${:,.2f}".format(disc_total)
        print(f"Sales tax amount: {sales_tax}")

def display_disc_total():
    print(f"Sales tax amount: {sales_tax}")
    print(f"Discount: {discount}")
    print(f"Total: {disc_total}")

def main():
    compute_total()
    if day_of_week == 1 or 2 and sub_total >= 50:
        compute_discount()
        display_disc_total()
    else:
        display_total()

main()