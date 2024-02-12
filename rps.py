# rps_match uses 2 parameters. 
# - user_choice = You
# - computer_choice = Computer

# The choices are represented like this: 
# 0 = Rock 
# 1 = Paper 
# 2 = Scissors

# This function will compare the user's choice with the computer's choice
# and return a result (see README for instructions) 
    
def rps_match(user_choice, computer_choice):
    if user_choice >= 3 or computer_choice >= 3:
        return "invalid input"
    else:
        # Add your code here
        if user_choice == computer_choice:
            return 0
        elif user_choice == 1 and computer_choice == 0:
            return "1"
        elif user_choice == 2 and computer_choice == "1":
            return "1"
        elif user_choice == 0 and computer_choice == 2:
            return "1"
        else:
            return "-1"
    
    
