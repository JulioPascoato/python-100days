#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(phonetic_data)

phonetic_alphabet = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}
# print(phonetic_alphabet)

word = input("Enter a word: ")

result = [phonetic_alphabet[letter] for letter in word.upper()]
print(result)