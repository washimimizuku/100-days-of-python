def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

total = add(3, 5, 6, 3, 7, 9, 3, 4, 6)
print(total)
