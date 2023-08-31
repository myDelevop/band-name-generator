from replit import clear
from art import logo

print(logo)

auction_dictionary = {}
play = True

while play:
    player_name = input("What is your name? ")
    player_bid = round(float(input("What is your bid?: ")), 2)

    if len(auction_dictionary) == 0:
        auction_dictionary[player_name] = player_bid
    else:
        for key in list(auction_dictionary.keys()):
            if player_bid > auction_dictionary[key]:
                auction_dictionary[player_name] = player_bid

    play = input("Are there any other bidders? Type 'yes or 'no'\n").lower() == 'yes'
    clear()


to_list = list(auction_dictionary.items())
print(f"The winner is {to_list[-1][0]} with a bid of ${to_list[-1][1]}\n")
