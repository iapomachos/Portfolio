#Ioannis Apomachos

import random

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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice=random.randint(0,2)
deck=[rock, paper, scissors]

print("You Chose:\n" +deck[user_choice])
print("Computer Chose:\n" +deck[computer_choice])


if (user_choice==0 and computer_choice==0) or (user_choice==1 and computer_choice==1) or (user_choice==2 and computer_choice==2):
    print("Its a draw")
elif (user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
    print("You win!")
else:
    print("You lose")