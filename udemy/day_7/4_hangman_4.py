import random
from function import from_array_of_char_to_string

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


# Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
# or for _ in range(len(chosen_word)):

for _ in chosen_word:
    display.append('_')

win = False

while win is False and lives > 0:
    guess = input("Guess a letter: ").lower()

    # TODO-2: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print("You lose.")
    elif from_array_of_char_to_string(display) == chosen_word and "_" not in display:
        win = False
        print("You win!")

    print(stages[lives])
