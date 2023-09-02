from menu import MENU, resources


def check_enough_resources(drink):
    missing_ingredient = ""

    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > resources[key]:
            missing_ingredient = key

    return missing_ingredient


def compute_total(n_quarters, n_dimes, n_nickles, n_pennies):
    return n_quarters * 0.25 + n_dimes * 0.1 + n_nickles * 0.05 + n_pennies * 0.01


profit = 0

quarters = 0
dimes = 0
nickles = 0
pennies = 0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in ['espresso', 'latte', 'cappuccino']:
        if len(check_enough_resources(choice)) > 0:
            print(f"Sorry there is not enough {choice}.")
        else:  # we are able to do your drink
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))

            user_money = compute_total(quarters, dimes, nickles, pennies)
            drink_price = MENU[choice]['cost']

            if round(drink_price, 2) > round(user_money, 2):
                print("Sorry that's not enough money. Money refunded.")
            elif round(drink_price, 2) == round(user_money, 2):
                profit += drink_price
            elif round(drink_price, 2) < round(user_money, 2):
                change = round(user_money, 2) - round(drink_price,2)
                profit += round(drink_price)
                print(f"Here is ${round(change,2)} dollars in change.")

                print(f"Here is your {choice}. Enjoy!")
