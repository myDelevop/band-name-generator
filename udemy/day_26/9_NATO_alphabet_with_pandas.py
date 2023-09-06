import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

user_input = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]

print(output_list)
