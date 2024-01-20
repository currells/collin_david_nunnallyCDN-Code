"""
Author: Collin Nunnally
File: checkpoint.py

Appending a list of names
"""
# Ask for the name of a friend. Keep asking unless they type "end."
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
friends = []
friend = ""

print('Type "end" once you listed all your friends. 👌')
while friend != "end":
    friend = input("Type the name of a friend: ")
    if friend != "end":
        friends.append(friend.capitalize())

print("\n")
# Print the list of names
for friend in friends:
    print(friend)
