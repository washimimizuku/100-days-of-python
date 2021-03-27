import os

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    # FileNotFoundError
    file = open(os.path.join(LOCATION, "a_file.txt"))

    # KeyError
    a_dictonary = {"key": "value"}
    value = a_dictonary["key"]
except FileNotFoundError:
    file = open(os.path.join(LOCATION, "a_file.txt"), "w")
    file.write("Something")
except KeyError as error:
    print(f"The key {error} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Hunan Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)