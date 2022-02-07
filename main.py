# Name: Ruben Sanduleac
# Date: 02-07-2022
import letter as letter
import pandas

alphabet_data = pandas.read_csv("data/nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
words = [alphabet_dict[letter] for letter in word]
print(words)



