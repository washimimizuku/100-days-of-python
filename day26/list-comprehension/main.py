# For loop
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)
print(new_numbers)

# List comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# String as list
name = "Nuno Barreto"
new_list = [letter for letter in name]
print(new_list)

# Range as list
range_list = [n * 2 for n in range(1,5)]
print(range_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie", "Nuno", "Angela"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)