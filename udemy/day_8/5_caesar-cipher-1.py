alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text: str, shift_amount: int):
    encrypted_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = (pos + shift_amount) % len(alphabet)
        encrypted_text += alphabet[new_pos]
        # e.g.
        # plain_text = "hello"
        # shift = 5
        # cipher_text = "mjqqt"
        # print output: "The encoded text is mjqqt"
    print(f"The encoded text is {encrypted_text}")

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


encrypt(plain_text=text, shift_amount=shift)  # No Bug with civilization & CO 😊
