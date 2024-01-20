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
bank_names = []
bank_bal = []
max_bal = -9999999
max_acc = ""

print(
  "Welcome to the Avengers Assemble™️. Type your account names and balances. Type [quit] when finished.\n"
)
while True:

  # 01. Ask the user for the name of the bank account and then for it's current balance. Keep looping until the use says "quit"
  name = input("What is the name of your bank account? ")

  if name == "quit":
    break

  balance = float(input("what is the balance? "))

  if balance > max_bal:
    max_bal = balance
    max_acc = name

  bank_bal.append(balance)
  bank_names.append(name)

running_total = 0

# S03. Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.
while True:
  # 01. For each one, add the name and the balance to the appropriate list.
  print("\n")
  for i in range(len(bank_names)):
    ind_name = bank_names[i]
    ind_bal = bank_bal[i]

    running_total += ind_bal

  for i in range(len(bank_bal)):
    if bank_bal[i] > max_bal:
      max_bal = bank_bal[i]
      max_acc = bank_names[i]
    # 02. Loop through the lists using an index and display the name of the account with the balance next to it.
    # S02. Change your display so that it shows the index of the account next to the name.
    print(f"[{i + 1}] {ind_name:<4} = ${ind_bal:,.2f}")

  # 03. Compute and display the total balance in all of the accounts and the average balance.
  print(f"\nTotal account balance: ${running_total:,.2f}")
  print(f"Average account balance: ${running_total / len(bank_names):,.2f}")

  # S01. Determine which bank account has the highest balance and display the name and balance of that account
  print(
    f"Your highest account is: {max_acc} and the balance is: ${max_bal:,.2f}")

  # S02. After displaying the list, ask the user if they want to update an account. If they respond with yes, ask for the index of the account, and the new balance.
  edit_acc = input(
    "\nWould you like to edit an account balance (Yes/No)? ").lower()

  if edit_acc == "no":
    break

  number_change = int(input("What [number] would you like to edit? "))
  new_name = input("What is the new account name? ")
  new_bal = float(input("What is the new balance? "))

  bank_names[number_change - 1] = new_name
  bank_bal[number_change - 1] = new_bal

print("\nThank you for checking your $$$ with Avengers Assemble™️.")
