# Name: Ruben Sanduleac
# Date: 02-07-2022
import pandas


def generate_phonetic_alphabet():
    """imports the csv using pandas library and then
    imports them into a dictionary where the words are read using a for loop
    where each letter in the word is looped through and checked as key in the dictionary
    try, except, else are used to validate the input"""

    alphabet_data = pandas.read_csv("data/nato_phonetic_alphabet.csv")
    alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

    word = input("Enter a word: ").upper()
    try:
        words = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Enter, only letter in the alphabet.")
        generate_phonetic_alphabet()
    else:
        print(words)


def main():
    """Main entry point"""
    generate_phonetic_alphabet()


if __name__ == '__main__':
    main()
