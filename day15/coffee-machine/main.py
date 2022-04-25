MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(ingredients):
    for name, quantity in ingredients.items():
        if quantity > resources[name]:
            print(f"Sorry, there is not enough {name}.")
            return False
    return True


def check_money():
    print("Sorry, you don't have enough money.")

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    return {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies,
        "total": quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    }

def give_change(total, cost):
    change = round(total - cost, 2)
    print(f"Here is ${change} dollars in change.")

def make_coffee(order, ingredients):
    for name, quantity in ingredients.items():
        resources[name] -= quantity
    print(f"Here is your {order}. Enjoy!")

machine_on = True

while machine_on:
    ingredients = {}
    cost = 0.0
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        machine_on = False
        break
    elif order == "report":
        print_report()
        continue
    elif order in MENU:
        ingredients = MENU[order]["ingredients"]
        cost = MENU[order]["cost"]
        if check_resources(ingredients):
            coins = insert_coins()
            if coins["total"] < cost:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif coins["total"] > cost:
                give_change(coins["total"], cost)
        
            resources["money"] += cost
            make_coffee(order, ingredients)

    else:
        print("We don't have that product, please try again.")