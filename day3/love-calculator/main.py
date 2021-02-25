print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
names = names.lower()

true = 0
true += names.count('t')
true += names.count('r')
true += names.count('u')
true += names.count('e')

love = 0
love += names.count('l')
love += names.count('o')
love += names.count('v')
love += names.count('e')

score = true * 10 + love

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")