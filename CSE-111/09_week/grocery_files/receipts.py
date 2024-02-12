"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Goes through multiple .csv files and gathers info from them
"""
PRODUCT_INDEX = 0
NAME_INDEX = 1
QUANTITY_INDEX = 1
PRICE_INDEX = 2

def read_dictionary(filename, key_column_index):
    dict_products = {}
    with open(filename, "r") as products_file:
        next(products_file) # Skips first line in products.csv
    
        for row in products_file:
            columns = row.strip().split(",") 
            product = columns[PRODUCT_INDEX]
            name = columns[NAME_INDEX]
            price = columns[PRICE_INDEX]
            dict_products[product] = (name, price)  # Use tuple to store name and price together
    return dict_products

def main():
    dict_products = read_dictionary("products.csv", PRODUCT_INDEX)
    print(f"Products Dictionary: {dict_products}") # Prints whole products dictionary
    print("")
    print("Product List:")
    with open("request.csv", "r") as request_file:
        next(request_file)

        for row in request_file:
            columns = row.strip().split(",") # Defines terms of the request.csv
            request_product = columns[PRODUCT_INDEX]
            quantity = columns[QUANTITY_INDEX]
            if request_product in dict_products: # Looks through product ID's of request.csv to match and print those in products.csv
                name, price = dict_products[request_product]
                print(f"Product: {name}, Requested Quantity: {quantity}, Price: {price}")

main()
