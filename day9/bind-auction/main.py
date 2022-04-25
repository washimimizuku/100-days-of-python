from art import logo

print(logo)
print("Welcome to the secret auction program")

bids = []
bidding = True

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    bids.append({
        "name": name,
        "bid": bid
    })
    
    if more_bidders == 'no':
        bidding = False

highest_bid = 0
winner = {}
for bid in bids:
    if bid["bid"] > highest_bid:
        highest_bid = bid["bid"]
        winner = bid

print("The winner is " + winner["name"] + " with a bid of $" + str(winner["bid"]) +".")