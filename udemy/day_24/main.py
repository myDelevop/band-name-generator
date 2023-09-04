# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

string_letter = ""

with open("./Input/Names/invited_names.txt") as names_file:
    for line in names_file.readlines():
        name = line.strip()
        with open("./Input/Letters/starting_letter.txt") as template:
            string_letter = template.read()
            string_letter = string_letter.replace("[name]", name)

        with open(f"./Output/ReadyToSend/for_{name}.txt", mode="w") as letter:
            letter.write(string_letter)

