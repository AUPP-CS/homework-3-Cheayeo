# HW.3 RPS Game

Your little brother wants you to develop a game of rock-paper-scissors (RPS) for him to practice playing. 

These are the rules:
- Rock✊beats Scissors✌
- Scissors✌️beats Paper🖐
- Paper🖐 beats Rock✊

<br>

## RPS Function Explained

You will be creating the `rps_match` function to simulate a game of Rock, Paper, Scissors between the user and a computer.

The function takes two parameters:
1. `user_choice`: This is the choice made by the user. 
2. `computer_choice`: This is the choice made by the computer.

<br>

The winning conditions for the game:
- Rock (0) beats Scissors (2)
- Paper (1) beats Rock (0)
- Scissors (2) beats Paper (1)

<br>

The function checks the following conditions:

- If the `user_choice` is the same as the `computer_choice`, the game is a tie, and the function returns **0**.  
- If the `user_choice` and the `computer_choice` match any of the winning conditions, the user wins, and the function returns **1**.
- If the `computer_choice` and the `user_choice` match any of the winning conditions, the computer wins, and the function returns **-1**.
- If none of these conditions are met, the function returns an error message **invalid input**.

<br>

## HINT
> - Try to use `randint`, `list`, and `while` to implement the code correctly. 

<br>

## Reminders
1. Your application should not crash when invalid input (non-number) is provided as a game choice.
2. The first player to recieve 3 points will **win.**
3. All choices must be shown on screen.
4. The player should be able to repeat the game after it ends.
5. Be creative in the terminal and keep the UI clean. Examples of this are in Canvas (under homework showcase).
6. Run `pytest` to verify that your function works as expected.
7. Make sure to add **comments** into your code for any new concepts you use that are from outside of class or from the internet.

<br>

## Expected Output:
![image](https://github.com/AUPP-CS/homework_3/assets/80062829/fcdaaea9-3e9e-485c-8161-4e1d91a17656)


