from random import randint

logo = '''
   ___                       _   _                __                 _               
  / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
'''
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")

number = randint(1, 100)

difficulty = input("Choose a difficulty between 'easy' and 'hard': ")
number_of_guesses = 5
if (difficulty == 'easy'):
    number_of_guesses = 10

for guess_try in range(number_of_guesses):
    guess = int(input("Make a guess: "))

    if guess == number:
        print("You guessed it!")
        print(f"The number is {number}")
        break
    else:
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

        tries_left = number_of_guesses - guess_try - 1
        if tries_left == 0:
            print("Game over!")
        else:
            print("Guess again.")
            print(f"You have {tries_left} tries left.")
