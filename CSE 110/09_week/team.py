"""
 
student: tristan galloway
teacher: brother keers
file: team_9.py
Assignment: Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0. 
 
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
numbers = []
number = ""
running_total = 0
average = 0
max_num = 0
min_pos = 9999
 
# Ask the user for a series of numbers
while number != 0:
    number = int(input("Enter a number: "))
    # Stop when they enter 0
    if number != 0:
          # Append each one to a list
        numbers.append(number)
print(numbers)
 
# 01. Compute the sum, or total, of the numbers in the list.
for i in numbers:
    running_total += i
 
# 02. Compute the average of the numbers in the list.
average = running_total / len(numbers)
 
# 03. Find the maximum, or largest, number in the list.
for i in numbers:
 
    if i > max_num:
        max_num = i
 
# Show the numbers calculated
print(f"\nSum: {running_total}")
print(f"Average: {average}")
print(f"Max: {max_num}")




 
# Stretch 01. Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).
 
# Stretch 02. Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.