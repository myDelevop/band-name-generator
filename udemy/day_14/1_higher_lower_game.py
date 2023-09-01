import random
import art
import game_data


def get_random_name(is_a):
    random_data = random.choice(game_data.data)

    if is_a:
        print(f"Compare A: {random_data['name']}, a {random_data['description']}, from {random_data['country']}.")
    else:
        print(f"Against B: {random_data['name']}, a {random_data['description']}, from {random_data['country']}.")

    return random_data['follower_count']


score = 0
you_win = True

while you_win:
    print(art.logo)

    num_a_followers = get_random_name(True)
    print(art.vs)
    num_b_followers = get_random_name(False)

    choice = input("Who has more followers? Type 'A' or 'B': ")
    winner = ''

    if num_a_followers >= num_b_followers:
        winner = 'A'
    elif num_b_followers < num_a_followers:
        winner = 'B'
    else:
        print("There is some error in the code")

    if winner == choice:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        you_win = False
