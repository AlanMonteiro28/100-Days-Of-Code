import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows() if row.letter != "letter" or row.code != "code"}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()

    try:
        user_phonetic_alphabet = [phonetic_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet, please!")
        generate_phonetic()
    else:
        print(user_phonetic_alphabet)


generate_phonetic()
