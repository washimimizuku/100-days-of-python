import random
import art
from game_data import data


def game():
    isCorrect = True
    score = 0

    while isCorrect:
        compareA = data[random.randint(0, len(data) - 1)]
        compareB = data[random.randint(0, len(data) - 1)]

        while compareA == compareB:
            compareB = data[random.randint(0, len(data) - 1)]
        
        print(art.logo)
        if score > 0:
            print(f"You are right! Current score: {score}")

        print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
        print(art.vs)
        print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == 'A' and compareA['follower_count'] > compareB['follower_count']:
            score += 1
        elif guess == 'B' and compareB['follower_count'] > compareA['follower_count']:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            isCorrect = False

game()