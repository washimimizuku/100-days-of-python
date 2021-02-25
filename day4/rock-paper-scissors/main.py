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

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))

if user_choice < 0 or user_choice > 2:
    print("Wrong number, you lose!")
else:
    print(choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("There's a draw")
    else:
        if user_choice > computer_choice:
            if user_choice == 2 and computer_choice == 0:
                print("Computer won :(")
            else:
                print("You win!")
        else:
            if user_choice == 0 and computer_choice == 2:
                print("You win!")
            else:
                print("Computer won :(")
      