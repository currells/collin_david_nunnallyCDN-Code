"""

team: Unathletic Avengers
teacher: Brother Keers
file : team_10.py
assignment: track bank accounts and the balances in each one.

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

# 01. Create two lists, one for the names of the bank accounts, and one for the balances.
bank_name = []
bank_balance = []

while True:

  # 01. Ask the user for the name of the bank account and then for it's current balance. Keep looping until the use says "quit"
  name = input("What is the name of your bank account? ")
  if name == "quit":
    break

  balance = float(input("what is the balance? "))

  # 01. For each one, add the name and the balance to the appropriate list.
for i in range(len(bank_name)):
  ind_name = bank_name[i]
  ind_balance = bank_balance[i]

  print(f"[{i + 1}] {ind_name:<4} = ${ind_balance:,.2f}")

# 02. Loop through the lists using an index and display the name of the account with the balance next to it.

# 03. Compute and display the total balance in all of the accounts and the average balance.

# Stretch Challenge: 💪🥱
# S01. Determine which bank account has the highest balance and display the name and balance of that account.

# S02. Change your display so that it shows the index of the account next to the name.

# S02. After displaying the list, ask the user if they want to update an account. If they respond with yes, ask for the index of the account, and the new balance.
# S03. Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.
# S03. Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.