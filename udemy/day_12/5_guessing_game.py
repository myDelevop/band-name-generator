import random
import art

NUMBER_TO_GUESS = random.randint(1, 100)


guesses = {
    "easy": 10,
    "hard": 5
}

print("Spoiler " + str(NUMBER_TO_GUESS))

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = guesses[difficulty]

win = False
while attempts > 0 and win is False:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))

    if guess == NUMBER_TO_GUESS:
        print(f"You got it! The answer was {NUMBER_TO_GUESS}.")
        win = True
    elif guess < NUMBER_TO_GUESS:
        print("Too low.\nGuess again.")
    elif guess > NUMBER_TO_GUESS:
        print("Too high.\nGuess again.")

    attempts -= 1

# print(f"You got it! The answer was {NUMBER_TO_GUESS}.")
# print("You've run out of guesses, you lose."
