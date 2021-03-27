import os
import pandas

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = pandas.read_csv(os.path.join(LOCATION,"nato_phonetic_alphabet.csv"))

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

not_a_word = True
while not_a_word:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter of the alphabet please")
    else:
        not_a_word = True
        print(output_list)

