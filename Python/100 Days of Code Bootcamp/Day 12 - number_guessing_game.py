#Ioannis Apomachos

import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


print(logo)
print("Welcome ot the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty_level=input("Choose a diffuculty type 'easy' or 'hard': ")
random_number=random.randint(1,100)
remaining_lives=0
user_guess=0

if difficulty_level=='easy':
    remaining_lives=10
elif difficulty_level=='hard':
    remaining_lives=5
else:
    print("Wrong input")



while remaining_lives>0 and user_guess!=random_number:
    print(f"You have {remaining_lives} attempts remaining to guess the number.")
    user_guess=int(input("Make a guess: "))

    if user_guess<random_number:
       remaining_lives-=1
       print("Too low.")
    elif user_guess>random_number:
        remaining_lives-=1
        print("Too High.")
    else:
        print("You Won")

    if remaining_lives>0 and user_guess!=random_number:
        print("Guess again.")

print(f"The secret number was {random_number}")

