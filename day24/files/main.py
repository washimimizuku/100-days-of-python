import os

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME = "my_file.txt"

# Read file outside a while
file = open(os.path.join(LOCATION, FILENAME))
contents = file.read()
print(contents)
file.close()

# Read file
with open(os.path.join(LOCATION, FILENAME)) as file:
    contents = file.read()
    print(contents)

# Write file
with open(os.path.join(LOCATION, FILENAME), mode="w") as file:
    file.write("New text that replaces everything.")

# Add to file
with open(os.path.join(LOCATION, FILENAME), mode="a") as file:
    file.write("\nNew text that appends to what we have.")

with open(os.path.join(LOCATION, "new_file.txt"), mode="w") as file:
    file.write("New text on new file.")
