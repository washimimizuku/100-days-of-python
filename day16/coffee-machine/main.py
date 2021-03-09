from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class CoffeeMachine:

    def __init__(self):
        self.on = False
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def is_on(self):
        return self.on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

coffee_machine = CoffeeMachine()

coffee_machine.turn_on()
while coffee_machine.is_on():
    order = input(f"What would you like? ({coffee_machine.menu.get_items()}): ")

    if order == "off":
        coffee_machine.turn_off()
    elif order == "report":
        coffee_machine.coffee_maker.report()
        coffee_machine.money_machine.report()
    elif coffee_machine.menu.find_drink(order):
        drink = coffee_machine.menu.find_drink(order)
        if coffee_machine.coffee_maker.is_resource_sufficient(drink) and coffee_machine.money_machine.make_payment(drink.cost):
            coffee_machine.coffee_maker.make_coffee(drink)
    else:
        print("We don't have that product, please try again.")