from rps import rps_match
from random import randint
import os
import platform

def clear_screen():
    # Get the operating system
    operating_system = platform.system()
    # Clear screen based on the operating system
    if operating_system == 'Linux':
        os.system('clear')  # For Linux
    elif operating_system == 'Windows':
        os.system('cls')   # For Windows
    else:
        print("Unsupported operating system: {}".format(operating_system))


welcome_screen = """

\t\t+----------------------------------------------------------------------------------------------------------------------------------------------------+
\t\t|.-------.    .-------.    .-'''-.            _______   .---.  .---.    ____      .---.     .---.       .-''-.  ,---.   .--.  .-_'''-.       .-''-.  |
\t\t||  _ _   \   \  _()_ \  / _     \          /   __  \  |   |  |_ _|  .'  __ .   | ,_|     | ,_|     .'_ _   \ |    \  |  | '_( )_   \    .'_ _   \ |
\t\t|| ( ' )  |   | (_ o._)| (' )/--'         | ,_/  \__) |   |  ( ' ) /   '  \  \,-./  )   ,-./  )    / (  )   '|  ,  \ |  ||(_ o _)|  '  / (  )   '|
\t\t||(_ o _) /   |  (_,_) /(_ o _).          ,-./  )       |   '-(_{;}_)|___|  /  |\  '_ ') \  '_ ') . (_ o _)    |\_ \|  |. (_,_)/___| . (_ o _)  
\t\t|| (_,_).'  |   '-.-'  (_,_). '.        \  '_ '`)     |      (_,_)    _.-`   | > (_)  )  > (_)  ) |  (_,_)___||  _( )_\  ||  |  .-----.|  (_,_)___||
\t\t||  |\ \  |  ||   |     .---.  \  :        > (_)  )   | _ _--.   | .'   _    |(  .  .-' (  .  .-' '  \   .---.| (_ o _)  |'  \  '-   .''  \   .---.|
\t\t||  | \ '   /|   |     \    -'  |       (  .  .-'_/  )|( ' ) |   | |  _( )_  | -'-'|___`-'-'|___\  -'    /|  (_,_)\  | \  -'   |  \  `-'    /|
\t\t||  |  \    / /   )      \       /         -'-'     / (_{;}_)|   | \ (_ o _) /  |        \|        \\       / |  |    |  |  \        /   \       / |
\t\t|''-'   '-'  ---'       -...-'            ._____.'  '(_,_) '---'  '.(_,_).'   --------``-------- '-..-'  '--'    '--'   '-...-'     `'-..-'  |
\t\t+----------------------------------------------------------------------------------------------------------------------------------------------------+
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       __________)
      (____)
---.(___)
'''

# store RPS print sign in a list call option

options = [rock, paper, scissors]
print(welcome_screen)
computer_count = 0
player_count = 0

while not(computer_count == 3 or player_count == 3):
    print("1. rock\n2. paper \n3. scissors")
    user_choice = int(input ("Enter your options: "))
    computer_choice = randint(0,2)
    print("\n")
    print("Player:\n" + options[user_choice-1])
    print("Computer:\n" + options[computer_choice-1])
    result = rps_match(user_choice, computer_choice)
    if result == "1":
        player_count += 1
    elif result == "-1":
        computer_count += 1      
    print(f"result P:{player_count} C:{computer_count}")
    
    if player_count == 3 or computer_count == 3: 
        if player_count == 3:
            print("You win!🤩")
        elif computer_count == 3: 
            print("Bot win!🤖")

        # Ask user if they want to play again
        continue_again = input("Do you want to play again? (Y/N): ")
        if continue_again.lower() == "y":
            computer_count = 0
            player_count = 0
        clear_screen()