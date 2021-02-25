from art import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    is_calculating = True
    while is_calculating:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]

        num2 = float(input("What is the next number? "))

        solution = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {solution}")


        continue_calculating = input("Press 'y' if you want to continue, 'n' if you want to start again: ")

        if continue_calculating == "y":
            num1 = solution
        else:
            is_calculating = False
            calculator()

calculator()