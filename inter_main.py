import random

BEATS = {'paper': 'rock', 'scissor': 'paper', 'rock': 'scissor'}
CHOICES = list(BEATS.keys())

def get_user_choice():
    while True:
        choice = input(f"Choose among {'/'.join(CHOICES)}: ").lower().strip()
        if choice in CHOICES:
            return choice
        print(f"Invalid, Options are: {CHOICES}")

def get_result(user, program):
    if user == program:
        return 'draw'
    return 'win' if BEATS[user] == program else 'lose' ## this logic works like this
# As the beats list is mapped to what beats it so if user chooses rock so the program knows rock beats paper and if the prgram also picks paper and they both match then user wins.
#

def play():
    user = get_user_choice()
    program = random.choice(CHOICES)
    result = get_result(user, program)
    print(f"Program chose {program}, You {result}")

play()