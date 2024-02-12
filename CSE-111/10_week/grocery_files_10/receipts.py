"""
Name: Collin Nunnally, Maidens of Mayhem (BC, CN, PT, JH, ZM)
Class: CSE-111
Comments:
Worked together as a team on this prove assignment
"""


import csv
from datetime import datetime

def read_dictionary(filename, key_column_index, value_column_indices):
    # this creates an empty dictionary that will later have the contents in the csv file appended to
    products_dict = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            # 'if len(row_list) != 0:' checks to see if the line in the reader file actually has any values
            if len(row_list) != 0:
                key = row_list[key_column_index]
                values = [row_list[i] for i in value_column_indices]
                products_dict[key] = values
    return products_dict

def main():
    # read_dictionary reads a csv file as a dictionary and '0,[1,2] tells the computer how to split it up
    products_dict = read_dictionary("products.csv", 0, [1, 2])
    print("Products Dictionary:")
    print(products_dict)

    print("\nMaidens of Mayhem Grocery")

    print("\nRequested Items:")

    total_items = 0
    subtotal = 0

    try:
        with open("request.csv", "r") as csv_file_2:
        #   line 31 skips the first line in the csv file
            next(csv_file_2)
            for line in csv_file_2:
                try:
                    # this assigns each index within the list to its own variable
                    product_number, quantity = line.strip().split(",")
                    # this changes the values under quantity from a string to a float
                    value = float(quantity)
                    # this takes the number in each line under quantity and adds it the the 'total_items' variable
                    total_items += value
                except ValueError:
                    print(f'Invalid value found in row: {line}')

            #   This calculates the subtotal of the requested items
                product_info = products_dict.get(product_number)
                if product_info:
                    product_name, price = product_info
                    total_price = float(price) * int(quantity)
                    subtotal += total_price
                    print(f'{product_name}: {quantity} @ {price}')
                else:
                    print(f"Error: Unknown Product ID in the request.csv file.\n'{product_number}'")

    except FileNotFoundError:
        print("File not found error occurred.")
    except KeyError as e:
        print(f"Key error occurred while processing the files: {e}")

    discount = 0
    added_discount = False
    #   This calculates the sales tax
    if total_items > 0:
        sales_tax = subtotal * 0.06
        total_amount_due = subtotal + sales_tax

    #   STRETCH CHALLENGE
    #   This calculates a discount based on the day of the week
        current_date = datetime.now()
        day_of_week = current_date.weekday()
        day_of_week = 1

    #   This assigns the discount to the desired day of the week
        if day_of_week == 1 or day_of_week == 2:
            discount = .1
            added_discount = True

    #   This calculates the discounted day into the total amount
        discounted_total = subtotal * discount
        total_amount_due = (subtotal + sales_tax) - discounted_total



        print()
        print(f"Total Items: {total_items}")
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales Tax (6%): ${sales_tax:.2f}')
        if added_discount == True:
            print(f'Day of Week Discount: -${discounted_total:.2f}')
        print(f'Total: ${total_amount_due:.2f}')
        print()

        current_date_and_time = datetime.now()
        print(f"Date and Time: {current_date_and_time.strftime('%A, %B %d, %Y %I:%M %p')}")
        print()

if __name__ == "__main__":
    main()