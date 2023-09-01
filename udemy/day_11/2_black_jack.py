import random
import art
from replit import clear


def deal_card(deck):
    """Returns a random card from the deck"""
    return random.choice(deck)


def calculate_score(deck):
    if len(deck) == 2 and sum(deck) == 21:
        # blackjack
        return 0
    total = sum(deck)

    loop = True
    while loop is True and total <= 21:
        if deck.count(11) > 0:
            deck.remove(11)
            deck.append(1)
        else:
            loop = False
    return total


def compare(user_score, computer_score):
    user_win = None
    if user_score == computer_score:
        user_win = 2
    elif computer_score == 0:
        user_win = 0
    elif user_score == 0:
        user_win = 1
    elif user_score > 21:
        user_win = 0
    elif computer_score > 21:
        user_win = 1
    else:
        if user_score > computer_score:
            user_win = 1
        else:
            user_win = 0
    return user_win


def print_final_output(user_cards, user_tot, computer_cards, computer_tot):
    print(f"\nYour final hand: {user_cards}, final score: {user_tot}")
    print(f"\nComputer's final hand: {computer_cards}, final score: {computer_tot}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True

while play is True:

    user_cards = []
    computer_cards = []

    choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n':").lower()
    clear()

    if choice == 'y':
        print(art.blackjack_logo)

        for _ in range(2):
            user_cards.append(deal_card(cards))
            computer_cards.append(deal_card(cards))

        user_tot = calculate_score(user_cards)
        computer_tot = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_tot}")
        print(f"Computer's first card {computer_cards[0]}")

        if user_tot == 0:
            print_final_output(user_cards, user_tot, computer_cards, computer_tot)
            print(art.user_win_string)
            break
        elif computer_tot == 0 or user_tot >= 21:
            print_final_output(user_cards, user_tot, computer_cards, computer_tot)
            print(art.computer_win_string)
            break
        else:
            again = True
            while again is True:
                user_in = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_in == 'y':
                    user_cards.append(deal_card(user_cards))
                    user_tot = calculate_score(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_tot}")

                    if user_tot == 0:
                        print(art.user_win_string)
                    elif computer_tot == 0 or user_tot >= 21:
                        print(art.computer_win_string)
                elif user_in == 'n':
                    again = False

        while calculate_score(computer_cards) <= 17:
            computer_cards.append(deal_card(cards))

        print_final_output(user_cards, user_tot, computer_cards, computer_tot)
        if compare(user_tot, computer_tot) == 0:
            print(art.computer_win_string)
        elif compare(user_tot, computer_tot) == 1:
            print(art.user_win_string)
        elif compare(user_tot, computer_tot) == 2:
            print(art.draw_string)

    elif choice == 'n':
        play = False
    else:
        print("Invalid Input!")
