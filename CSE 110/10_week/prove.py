"""
Author: Collin Nunnally
File: prove.py


"""
print("""
                             .!!!!.               
                            .&@@@@^               
                       ... ^&@@@@@^               
                 ^JG#&&&&&&@@@@@@@:               
              !B@&BJ~:.  J@@@@@@@@#!              
            J&@P^       J@@@@?&@@@#@&J            
          ^&@5.        5@@@&^ &@@@: 5@&^          
         7@@^         G@@@&.  &@@@^  ^@@7         
        ^@@:        .#@@@#.   @@@@^   :@@^        
        #@J        .&@@@G     7G@@^    J@#        
       .@@.       :&@@@@J????JBJ!Y:    .@@.       
       :@@.      ~@@@@@@@@@@@@@@&7     .@@:       
        &@!     7@@@@PJYYYYYY5#Y!J.    !@&        
        ?@&    J@@@@!         !P&@^    &@?        
         P@B  5@@@&^          @@@@^   B@P         
          57 G@@@&:           &@@@: ~&@Y          
            B@@@#.               .!#@#^           
          .&@@@B ~?:          :7G&@G^             
         .B&&&P  Y#&&&#BGGB#&&&#5~                
                    .^~!77!~^.     

                 Avengers Assemble                          
                                                            """)

import math
menu =["Add item", "See contents" ,"Remove item" , "See total", "Quit"]
cart = []
prices = []
total = 0


while True:
# Printing the available items
    for i in range(len(menu)):
        menu_item = menu[i]
        print(f"[{i + 1}] {menu_item}")
    print(menu_item)
    option = input("\nWhat would you like to do? ").strip()
    if option == "1":
        add = input("What item would you like to add? ")
        cart.append(add.capitalize())
        cost = float(input(f"What is the cost of <{add.capitalize()}>? Ex.[3.23] "))
        prices.append(cost)
    elif option == "2":
        print("Your current cart:")
        for i in range(len(cart)):
            ind_item = cart[i]
            ind_price = prices[i]
            print(f"{i + 1}. {ind_item:.<10}${ind_price:,.2f}")
    elif option == "3":
        print("\n")
        for i in range(len(cart)):
            ind_item = cart[i]
            print(f"[{i + 1}] {ind_item}")
        num_change = int(input("What item [number] would you like to take out? "))
        cart[num_change - 1] = "[Removed]"
        prices[num_change - 1] = 0
        print("Your item was removed!\n")
    elif option == "4":
            total = math.fsum(prices)
            print(f"\nTotal: {total:,.2f}\n")
    elif option == "5": # Sets running to false, not making the while loop run
        break
    else:
        print("Please choose a valid option.😡")

print("Have a great day! 😉")

# When displaying the items, display a number in front of each item. The numbers should start with 1.

# Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)

# Remove both the item and the price of the item (test removing first and last item)