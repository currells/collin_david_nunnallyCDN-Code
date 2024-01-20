"""
Author: Collin Nunnally
File: 02_prove.py

Creating a MadLib program. I used ChatGPT for the story to
keep it creative! :)
"""

print("\nThe Avenger's shawarma incident...\n")
print("Answer the Following Questions: \n")

adj_1 = input("Adjective: ")
bad_guy = input("Name of a bad guy: ")
adj_2 = input("Another Adjective: ")
ing_adj = input("Adjective ending in -ing: ")
verb = input("Verb: ")
verb_2 = input("Another Verb: ")
ing_adj_2 = input("Another Adjective ending in -ing: ")
noun = input("Noun: ")

#These are to add colors to the responses
red = "\033[0;31m"
blue = "\033[0;34m"
white = "\033[0;37m"

#Reverts it back to the normal terminal gray
ending = "\033[39m"


"""
I decided to use the string format I learned from Bro. Keers
here because it made the most sense.
the {red+[word]+white} is how I found to change the color of only
the word without changing the rest of the text


"""
story = f"""
{white}Once upon a time, the Avengers were feeling {red+adj_1+white} after 
a grueling battle with their arch-nemesis, {blue+bad_guy+white}. They 
decided to {red+adj_2+white} in some shawarma, but they couldn't stop 
themselves and ended up {blue+ing_adj+white} way too much. Iron Man {red+verb+white}
loudly, while Thor complained about feeling {blue+verb_2+white}. Black 
Widow and Hawkeye were {red+ing_adj_2+white} in discomfort, while the Hulk 
looked like he was about to {blue+verb+white}. Suddenly, Captain America 
shouted, "Avengers {red+verb_2+white}! We need to find a {blue+noun+white}, 
stat!" The team rushed off, hoping to make it in time 
before their overindulgence caught up with them.{ending}
"""

print(f"{story}")