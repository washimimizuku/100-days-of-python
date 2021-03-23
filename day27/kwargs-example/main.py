def calculate(n, **kwargs):
    print(n)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

total = calculate(2, add=3, multiply=5)
print(total)
