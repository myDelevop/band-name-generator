import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


valid_input = False

while valid_input is False:
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letter in the alphabet, please.")
    else:
        valid_input = True
        print(output_list)
