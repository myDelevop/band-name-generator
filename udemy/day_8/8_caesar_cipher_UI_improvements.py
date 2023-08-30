from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(dir_type: str, start_text: str, shift_amount: int):
    new_text = ""
    new_pos = -1
    for letter in start_text:
        if alphabet.__contains__(letter):
            pos = alphabet.index(letter)
            if dir_type == "encode":
                new_pos = (pos + shift_amount) % len(alphabet)
            elif dir_type == "decode":
                new_pos = (pos - shift_amount) % len(alphabet)
            new_text += alphabet[new_pos]
        else:
            new_text += letter

    print(f"Here's the {dir_type}d d result: {new_text}")


print(logo)

restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(dir_type=direction, start_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye")
