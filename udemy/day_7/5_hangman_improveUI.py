import random
import hangman_art
import hangman_words
from replit import clear
from function import from_array_of_char_to_string

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []

# or for _ in range(len(chosen_word)):
for _ in chosen_word:
    display.append('_')

win = False

while win is False and lives > 0:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(f"{' '.join(display)}")

    if lives == 0:
        print("You lose.")
    elif from_array_of_char_to_string(display) == chosen_word and "_" not in display:
        win = False
        print("You win!")

    print(hangman_art.stages[lives])
