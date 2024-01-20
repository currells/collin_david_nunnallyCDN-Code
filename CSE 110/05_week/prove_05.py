"""
Author: Collin Nunnally
File: prove_05.py

Create Your Own Adventure:
# create 3 levels of scenarios (if ,elif, else)
    # 1 scenario must have 2+ choices
# Standardize Choices to CAPS [uppercase.()]
# Choices should be related to the question
# Always have an "else" statement
# STRETCH : Nest an if else statement inside 3 scenarios 
"""
# Start telling story
print("Avengers: Pathway to Destiny")
print("\nYou are a new recruit in the Avengers and must undergo training as a result.")

# Asking first Choice
choice = input("\nYou have a choice to train with Captain America in HAND-to-hand combat, work with Black Widow in STEALTH and espionage training, or with Hawkeye in ARCHERY reconnaissance. What do you choose? ").upper()

# Story based on these choices
if choice == "HAND": # 1st choice : Hand-to-Hand
    choice = input("\nBy choosing to train with Captain America, you become extremely strong and desireable by the opposite gender. A lady asks you to goto dinner, but it is the same night as a routine Night-OP mission. Do you chose the MISSION or the GIRL? ").upper() # 2nd nest in one scenario
    if choice == "MISSION":
        choice = input("\nYour choices prove fruitful to you and develop your skills. Now, An ancient artifact with immense power has been discovered. The Avengers must retrieve it before it falls into the wrong hands. Do you work with team A, which consists of Captain America and Black Widow or team B, which consists of Hawkeye and Ironman? ").upper() # 3rd nest in scenario. Every beginning choice has 3 "story lines" to it
        if choice == "A":
            print("\nYou chose the safe option, which is what is needed in this situation. You recover the artifact, called Triple Gooberberry Sunrise. It treats you to an ice cream sundae, but you felt you could have done more to get a better reward.")
        elif choice == "B":
            print("\nYour decision suited the team the best. With the strength of Captain America on both teams, you swiftly defeat HYDRA trying to take the artifact, Triple Gooberberry Sunrise, and are able to use the technology to make unlimited ice cream sundaes for the US.")
        else:
            print("\nYou did not decide a team and stayed at HQ. Your skills were needed at the battle and the artifact was destroyed, resulting in the world covered in ice cream, suffocating mankind. You survive knowing you could have changed humanity.")
    elif choice == "GIRL":
        choice = input("\nYou decide to meet with the girl, assuming it to be only dinner. It proves to be a set-up and you are knocked out. You come to and realize that your identification to the base is stolen. Do you INFORM headquarters or keep QUIET about your mistake? ").upper()
        if choice == "INFORM":
            print("\nBy you informing HQ, you are able to flag your card and catch the girl trying to break into HQ. You find that it is Jemisha, who was on the SHIELD wanted list for years. Good job!")
        elif choice == "QUIET":
            print("\nYou decide to act like it never happened. Jemisha, a villain on the SHIELD wanted list, steals multiple documents from HQ and you are pinned to be helping her steal these documents. You goto federal prison and have to slowly watch HYDRA take over SHIELD on TV, knowing you could have stopped it.")
        else:
            print("\nYou did not decide a team and stayed at HQ. Your skills were needed at the battle and the artifact was destroyed, resulting in the world covered in ice cream, suffocating mankind. You survive knowing you could have changed humanity.")
    else:
        print("\nSince you chose neither option, Captain America noticed your indecisiveness. This continued in future actions and, as a result, you were later kicked off the team.")
elif choice == "STEALTH": #2nd choice : Stealth and espionage
    choice = input("\nYou chose to work with the Black Widow and become very good at stealth and espionage. So much so, that the US Government offers you a highly sought after job. You question the ethics of this job, however. Do you chose the AVENGERS or the GOVERNMENT? ").upper()
    if choice == "AVENGERS":
        choice = input("\nYour choices prove fruitful to you. Now, An ancient artifact with immense power has been discovered. The Avengers must retrieve it before it falls into the wrong hands. Do you work with team A, which consists of Captain America and Black Widow or team B, which consists of Hawkeye and Ironman? ").upper()
        if choice == "A":
            print("\nYou chose the safe option, which is what is needed in this situation. You recover the artifact, called Triple Gooberberry Sunrise. It treats you to an ice cream sundae, but you felt you could have done more to get a better reward.")
        elif choice == "B":
            print("\nYour decision suited the team the best. With stealth on both sides of the teams, you swiftly defeat HYDRA trying to take the artifact, Triple Gooberberry Sunrise, and are able to use the technology to make unlimited ice cream sundaes for the US.")
        else:
            print("\nYou did not decide a team and stayed at HQ. Your skills were needed at the battle and the artifact was destroyed, resulting in the world covered in ice cream, suffocating mankind. You survive knowing you could have changed humanity.")
    elif choice == "GOVERNMENT":
        choice = input("\nYour job at the Government persuaded you to do things non-ethical things and gained a bad wrap with the shield. You continue to do a job that you hate, but make bank. Do you try to explain the situation to SHIELD and go back or cut your losses and STAY? ").upper()
        if choice == "SHIELD":
            print("\nYour talk with SHIELD was a difficult one, but turned out well. You had to work back up the ranks, but used the knowledge from the government to propel you up the ranks in SHIELD. You are able to return to your old job in time and are happy with your decision in the end.")
        elif choice == "STAY":
            print("\nYou stay for a couple more years at the government job, but get burned out. You quit and become a manager at a local Best Buy. You wish you would have stayed with SHIELD, but find a subtle comfort working at an easy job.")
        else:
            print("\nYou are not all in on one choice or the other, which affects your work at the government job. You make a critical error in leaking government documents to China of all places, and are arrested for this mistake. You are not able to recover from this mistake as it ruined your reputation.")
    else:
        print("\nSince you chose neither option, Black Widow noticed your indecisiveness. This continued in future actions and, as a result, you were later kicked off the team.")
elif choice == "ARCHERY": #3rd Choice : Archery
    choice = input("\nYou chose to become a second Hawkeye to the Avengers. Your skills are critical to the success towards many missions. You work is noticed by other organizations and would like to take you to brunch. Do you goto BRUNCH with these individuals or continue to TRAIN? ").upper()
    if choice == "BRUNCH":
        choice = input("\nYour brunch turned out well. You gain a liking to these individuals and they offer you a job in the Middle East. You would do recon on a VIP of theirs. This is all you know. Do you ACCEPT the job or DECLINE it? ").upper()
        if choice == "ACCEPT":
            print("\nYou accept the job, and go to the Middle East. While doing recon, you are not aware of an outpost that ruins your plan and missed the EVAC point. You are stuck in the Middle East and are eventually caught and killed after years of hiding.")
        elif choice == "DECLINE":
            print("\nYou decline and stay with your job in SHIELD. You still maintain communication with these individuals, which become and asset to SHIELD. You learn to find out that these individuals went to BYU-I, just like you! You and these individuals speak at BYU-I often and bring many interns to SHIELD as a result. Nick Fury becomes a member and gives a talk in General Conference.")
        else:
            print("\nYou do not decide anything and these individuals move on. Life continues as normal at SHIELD. You still wonder what could have come from those individuals and eventually forget about them.")
    elif choice == "TRAIN":
        choice = input("\nYour choices prove fruitful to you. Now, An ancient artifact with immense power has been discovered. The Avengers must retrieve it before it falls into the wrong hands. Do you work with team A, which consists of Captain America and Black Widow or team B, which consists of Hawkeye and Ironman? ").upper()
        if choice == "A":
            print("\nYour decision suited the team the best. With a skilled archer on both sides of the teams, you swiftly defeat HYDRA trying to take the artifact, Triple Gooberberry Sunrise, and are able to use the technology to make unlimited ice cream sundaes for the US.")
        elif choice == "B":
            print("\nYou chose the safe option, which is what is needed in this situation. You recover the artifact, called Triple Gooberberry Sunrise. It treats you to an ice cream sundae, but you felt you could have done more to get a better reward.")
        else:
            print("\nYou did not decide a team and stayed at HQ. Your skills were needed at the battle and the artifact was destroyed, resulting in the world covered in ice cream, suffocating mankind. You survive knowing you could have changed humanity.")
    else:
        print("\nSince you chose neither option, Hawkeye noticed your indecisiveness. This continued in future actions and, as a result, you were later kicked off the team.")
else:
    print("\nYou chose no training and was kicked out of the team. Living a life of sadness in your parent's basement.")

#Let user know game is over
print("\nGame over my friend.")
