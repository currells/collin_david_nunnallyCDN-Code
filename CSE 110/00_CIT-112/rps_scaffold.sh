#!/bin/bash

# Rock Paper Scissors, you against the computer.


    #                          .!!!!.               
    #                         .&@@@@^               
    #                    ... ^&@@@@@^               
    #              ^JG#&&&&&&@@@@@@@:               
    #           !B@&BJ~:.  J@@@@@@@@#!              
    #         J&@P^       J@@@@?&@@@#@&J            
    #       ^&@5.        5@@@&^ &@@@: 5@&^          
    #      7@@^         G@@@&.  &@@@^  ^@@7         
    #     ^@@:        .#@@@#.   @@@@^   :@@^        
    #     #@J        .&@@@G     7G@@^    J@#        
    #    .@@.       :&@@@@J????JBJ!Y:    .@@.       
    #    :@@.      ~@@@@@@@@@@@@@@&7     .@@:       
    #     &@!     7@@@@PJYYYYYY5#Y!J.    !@&        
    #     ?@&    J@@@@!         !P&@^    &@?        
    #      P@B  5@@@&^          @@@@^   B@P         
    #       57 G@@@&:           &@@@: ~&@Y          
    #         B@@@#.               .!#@#^           
    #       .&@@@B ~?:          :7G&@G^             
    #      .B&&&P  Y#&&&#BGGB#&&&#5~                
    #                 .^~!77!~^.     

    #              Avengers Assemble      


# script global variables to hold choices
computer_choice=-1
user_choice=-1

# generates the computer response
compute_computer_choice () {
	computer_choice=$(( RANDOM % 3 + 1 ))
}

# prints the user's selection
print_menu() {
	echo -e "\n1. Rock\n2. Paper\n3. Scissors\n4. Exit"
}

print_user_choice () {
	read -p "Choose your option: " input
	user_choice=$input
}

# decide who won the round.
compute_winner () {
	if (( user_choice == computer_choice )); then
		echo "You tied. Try again."
	elif (( user_choice == 1 && computer_choice == 3 )); then
		echo "You win!"
	elif (( user_choice == 2 && computer_choice == 1 )); then
		echo "You win!"
	elif (( user_choice == 3 && computer_choice == 2 )); then
		echo "You win!"
	elif (( user_choice == 2 && computer_choice == 3 )); then
		echo "You lose. Try again."
	elif (( user_choice == 3 && computer_choice == 1 )); then
		echo "You lose. Try again."
	elif (( user_choice == 1 && computer_choice == 2 )); then
		echo "You lose. Try again."
	else
		echo "Invalid input. Try again."
	fi
}

# main game loop
while true; do
	print_menu
	print_user_choice
	if (( user_choice == 4 )); then
		break
	fi
	compute_computer_choice
	compute_winner
done

echo "Thanks for playing, goodbye."
