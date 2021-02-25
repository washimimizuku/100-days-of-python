print('''
***********************************
         __________
        /\\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \\ | %  ))   |
      %  \\|%________|
       %%%%
***********************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at at a road outside the town, and you have two possible paths: Through the forest or around the forest. Where do you want to go? Type "forest" or "around" \n').lower()
if choice1 == "around":
    choice2 = input('You\'ve come to a beach. You can see an island far away. Type "build" to build a raft. Type "swim" to swim across. \n').lower()
    if choice2 == "build":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room full of poisonous gas. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by a shark. Game Over.")
else:
    print("You were eaten by a tiger. Game Over.")
