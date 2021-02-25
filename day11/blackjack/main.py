import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(player_cards):
    total_min = 0
    total_max = 0

    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0

    for card in player_cards:
        if card == 11:
            total_min += 1
            total_max += 11
        else:
            total_min += card
            total_max += card
        
    if total_max > 21:
        return total_min
    else:
        return total_max

def calculate_final_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("Bust!")
    elif user_score == computer_score:
        print("You draw!")
    elif user_score == 0:
        print("You win with blackjack!")
    elif computer_score == 0:
        print("Computer wins with blackjack!")
    elif user_score > 21:
        print("Bust!")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")

def play():
    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    while user_score < 21 and user_score > 0 and computer_score > 0 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)

        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")
    
    while computer_score > 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")

    calculate_final_score(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print(logo)
    play()