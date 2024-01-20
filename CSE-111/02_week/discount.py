"""
Name: Maidens of Mayham (BC, CN, PT, JH, ZM)
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


from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
print(day_of_week)

# day_of_week = 1

def main():

  def get_sub_total():
    sub_total = 'no'
  #loop will run till user enters a valid input.  
    while sub_total == 'no':
      #try and ecxpet used here to make sure the user inputs a number and no 
      #error codes stop the program from crashing
      try:
        sub_total = int(input("Please enter the subtotal: "))
      except ValueError:
        # 'sub_total = 'no' is used to make sure the loop will run again if the user enters
        # a non number value.
        sub_total = 'no'
      print('That is not a valid response.')
    return sub_total

  def compute_discount(sub_total, day_of_week):
    #the 'and' operator seems to be needed twice for each 'or' operator stipulation
    #to make sure the program will run the code properly if the day of the week is Tuesday
    #or wendnesday 
    if day_of_week == 1 and sub_total >= 50 or day_of_week ==2 and sub_total >= 50:
      discount = float(sub_total*0.1)
    else:
      discount = 'none'
    return discount


  #keeps me from having to do math to display sales tax properly
  def compute_total_sales_tax(sub_total, discount, day_of_week):
    if day_of_week == 1 and sub_total >= 50 or day_of_week ==2 and sub_total >= 50: 
       total_sales_tax = ((sub_total-discount) *0.06)
    else:
      total_sales_tax = sub_total*0.06
    return total_sales_tax             



  def compute_total(sub_total, total_sales_tax, day_of_week, discount):
    #day of the week is needed to properly take out the discount
    if day_of_week == 1 and sub_total >= 50 or day_of_week ==2 and sub_total >= 50: 
      total = float((sub_total-discount) + total_sales_tax)
    else:
      total =float(sub_total+ total_sales_tax)
    return total


  def display(total,total_sales_tax, sub_total, discount):
    if day_of_week == 1 and sub_total >= 50 or day_of_week ==2 and sub_total >= 50:
      print(f'sales tax: {(total_sales_tax):,.2f}')
      print(f'Weekly discount: -{discount}')
      print(f'Total: {total:,.2f}')


    else:
      print(f'Sales Tax: {(total_sales_tax):,.2f}')        
      print(f'Total: {total:,.2f}')



  #program starts here
  sub_total = get_sub_total()

  discount = compute_discount(sub_total, day_of_week)

  total_sales_tax = compute_total_sales_tax(sub_total, discount, day_of_week) 

  total = compute_total(sub_total, total_sales_tax, day_of_week, discount)

  display(total, total_sales_tax, sub_total, discount)


main()