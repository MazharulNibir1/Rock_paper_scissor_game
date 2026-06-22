import random

#lists
beats = {'rock': "scissor", 'paper': "rock", 'scissor': "paper"}
choice_list = ['rock', 'paper', 'scissor']

#PROGRAM CHOICE
program_choice = random.choice(choice_list)

#USER PROMPT

while True:
    user_choice= input("Choose between Rock, Paper and Scissor: ").lower().strip() # strip removes all the whitespaces
    #input validation
    if user_choice in choice_list:
        break
    else:
        print("Wrong input! try Again")

#GAME LOGIC
if user_choice == program_choice:
    result = 'draw'
elif beats[user_choice] == program_choice:
    result = 'win'
else:
    result = 'lost'

print(f"You have {result}, program chose {program_choice}")






