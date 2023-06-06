import pandas


def phonetic_generator():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please Try Again!!!")
        phonetic_generator()
    else:
        print(output_list)


phonetic_generator()
