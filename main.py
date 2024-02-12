from rps import rps_match
from random import randint
import os
import platform

# function to clear screen after finish 1 round of the game
def clear_screen():
    # ref to get this function: https://www.geeksforgeeks.org/clear-screen-python/
    # Get the operating system
    operating_system = platform.system()
    # Clear screen based on the operating system
    if operating_system == 'Linux':
        os.system('clear')  # For Linux
    elif operating_system == 'Windows':
        os.system('cls')   # For Windows
    else:
        print("Unsupported operating system: {}".format(operating_system))
   
    

# ASCII's website: "Ascii Art Archive"
# 1. font: flower power, Frame: Cat
# 2. Computer category => Commputer by MEPH 

welcome_screen = """

\t /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\t( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
\t > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
\t /\_/\                                                                                                                                                                   /\_/\ 
\t( o.o )  .-------.   .-------.   .-'''-.            _______  .---.  .---.   ____      .---.     .---.      .-''-.  ,---.   .--.  .-_'''-.       .-''-.          .---.   ( o.o )
\t > ^ <   |  _ _   \  \  _(`)_ \ / _     \          /   __  \ |   |  |_ _| .'  __ `.   | ,_|     | ,_|    .'_ _   \ |    \  |  | '_( )_   \    .'_ _   \         \   /    > ^ < 
\t /\_/\   | ( ' )  |  | (_ o._)|(`' )/`--'         | ,_/  \__)|   |  ( ' )/   '  \  \,-./  )   ,-./  )   / ( ` )   '|  ,  \ |  ||(_ o _)|  '  / ( ` )   '        |   |    /\_/\ 
\t( o.o )  |(_ o _) /  |  (_,_) (_ o _).          ,-./  )      |   '-(_{;}_)___|  /  |\  '_ '`) \  '_ '`). (_ o _)  ||  |\_ \|  |. (_,_)/___| . (_ o _)  |         \ /    ( o.o )
\t > ^ <   | (_,_).' __|   '-.-' (_,_). '.        \  '_ '`)    |      (_,_)   _.-`   | > (_)  )  > (_)  )|  (_,_)___||  _( )_\  ||  |  .-----.|  (_,_)___|          v      > ^ < 
\t /\_/\   |  |\ \  |  |   |    .---.  \  :        > (_)  )  __| _ _--.   |.'   _    |(  .  .-' (  .  .-''  \   .---.| (_ o _)  |'  \  '-   .''  \   .---.         _ _     /\_/\ 
\t( o.o )  |  | \ `'   /   |    \    `-'  |       (  .  .-'_/  )( ' ) |   ||  _( )_  | `-'`-'|___`-'`-'|__\  `-'    /|  (_,_)\  | \  `-'`   |  \  `-'    /        (_I_)   ( o.o )
\t > ^ <   |  |  \    //   )     \       /         `-'`-'     /(_{;}_)|   |\ (_ o _) /  |        \|        \       / |  |    |  |  \        /   \       /        (_(=)_)   > ^ < 
\t /\_/\   ''-'   `'-' `---'      `-...-'            `._____.' '(_,_) '---' '.(_,_).'   `--------``--------``'-..-'  '--'    '--'   `'-...-'     `'-..-'          (_I_)    /\_/\ 
\t( o.o )                                                                                                                                                                 ( o.o )
\t > ^ <                                                                                                                                                                   > ^ < 
\t /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
\t( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
\t > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 



\t\t\t\t\t\t\t                                                   .------.------.    
\t\t\t\t\t\t\t    +-------------+                     ___        |      |      |    
\t\t\t\t\t\t\t    |             |                     \ /]       |      |      |    
\t\t\t\t\t\t\t    |             |        _           _(_)        |      |      |    
\t\t\t\t\t\t\t    |             |     ___))         [  | \___    |      |      |    
\t\t\t\t\t\t\t    |             |     ) //o          | |     \   |      |      |    
\t\t\t\t\t\t\t    |             |  _ (_    >         | |      ]  |      |      |    
\t\t\t\t\t\t\t    |             | (O)  \__<          | | ____/   '------'------'    
\t\t\t\t\t\t\t    |             | [/] /   \)        [__|/_                          
\t\t\t\t\t\t\t    |             | [\]|  ( \         __/___\_____                    
\t\t\t\t\t\t\t    |             | [/]|   \ \__  ___|            |                   
\t\t\t\t\t\t\t    |             | [\]|    \___E/%%/|____________|_____              
\t\t\t\t\t\t\t    |             | [/]|=====__   (_____________________)             
\t\t\t\t\t\t\t    |             | [\] \_____ \    |                  |              
\t\t\t\t\t\t\t    |             | [/========\ |   |                  |              
\t\t\t\t\t\t\t    |             | [\]     []| |   |                  |              
\t\t\t\t\t\t\t    |             | [/]     []| |_  |                  |              
\t\t\t\t\t\t\t    |             | [\]     []|___) |                  |              
\t\t\t\t\t\t\t====================================================================

\t\t  **-----~-----**
\t\t |  Instruction  |
\t\t  **-----~-----**
✨ Welcome to "The Rock Paper Scissors RPS Challenge!" 
💪 Can you get 3 points first to win the bot?!
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
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
---.__(___)
'''

# store RPS print sign in a list call option
options = [rock, paper, scissors]

# print welcome screen
print(welcome_screen)

# set both human and bot's score count to 0
computer_count = 0
player_count = 0

# condition is set to False, the game starts
while not(computer_count == 3 or player_count == 3):
    print("------------------------------------------------------")
    print("\n1. rock🪨\n2. paper📜 \n3. scissors✂️\n") 
    
    # player's input choice
    user_choice = int(input ("🫴  Enter your options (1, 2, 3): "))
    
    # let computer randomly choose the 3 options from the list of options to compete with player
    computer_choice = randint(0,2) # the function mean let computer choose between index o, 1, 2 from list of options
    print("\n")
    print("Player 👦:\n" + options[user_choice -1]) # Print out player's choice to terminal
    print("Computer 🤖:\n" + options[computer_choice -1]) # Print out bot's choice to terminal
    result = rps_match(user_choice, computer_choice) # Call function rps_match 
    
    # score count
    
    if result == 1:
        player_count += 1 # player's score increase 1 point each time of winning
    elif result == -1:
        computer_count += 1 # bot's score increase 1 point each time of winning
    print("========================================")
    print(f" Result: 👧 Player: {player_count} VS 💻 Computer: {computer_count} ") # Print score of player and computer
    print("========================================")
    # Winner score condition
    if player_count == 3 or computer_count == 3: 
        if player_count == 3:
            print(" \n 🙆🎉'HERE IS YOUR ANGBAO! GOOD JOB!'🥳🧧\n ")
        elif computer_count == 3:
            print("\n 👾🥇 BOT: I win, try again buddy! 💪🌟\n ")

        # Ask user if they want to play again
        print("========================================")
        continue_again = input("👉 Do you want to play again? 🤩(Y/N): ")
        
        # if player chose y, we want both human and bot's score to return to 0 again (this way, the game restart)
        # we don't put condition for n because the loop will just stop by itself once it reaches the bottom
        if continue_again.lower() == "y":
            computer_count = 0
            player_count = 0
        
        # clear up the game screen, when player want to play again
        clear_screen()
            
      

        
    


    