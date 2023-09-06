with open("nato_phonetic_alphabet.csv") as phonetic_file:
    lines = phonetic_file.readlines()

file_dict = {line.strip().split(",")[0]: line.strip().split(",")[1]
             for line in lines if line.strip().split(",")[0] != 'letter'}

user_input = input("Enter a word: ")
for letter in user_input:
    print(file_dict.get(letter.upper()))
