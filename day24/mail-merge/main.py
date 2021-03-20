import os

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
LETTER_FILE = "Input/Letters/starting_letter.txt"
NAMES_FILE = "Input/Names/invited_names.txt"

names = []
with open(os.path.join(LOCATION, NAMES_FILE)) as names_file:
    for name in names_file.readlines():
        names.append(name.strip())

with open(os.path.join(LOCATION, LETTER_FILE)) as template_file:
    template = template_file.read()
    for name in names:
        letter_filename = f"Output/ReadyToSend/{name}_letter.txt"
        letter_text = template.replace("[name]", name)
        with open(os.path.join(LOCATION, letter_filename), mode="w") as letter_file:
            letter_file.write(letter_text)



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp