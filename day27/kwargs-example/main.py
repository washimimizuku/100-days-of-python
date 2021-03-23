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

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] # With dictionary key is mandatory
        self.model = kw.get("model") # With get it's optional
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Dacia", model="Duster")
print(my_car.make)
print(my_car.model)

my_car2 = Car(make="Nissan", color="cherry")
print(my_car2.make)
print(my_car2.model)
print(my_car2.color)
