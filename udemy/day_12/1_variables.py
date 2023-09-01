################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


#  Local Scope

def drink_potion_1():
    potion_strength = 2
    print(potion_strength)


drink_potion_1()

# NameError: name 'potion_strength' is not defined because is Local
# drink_potion(potion_strength)


# Global Scope
player_health = 10


def drink_potion_2():
    potion_strength = 2
    print(player_health)


drink_potion_2()


def game():
    def drink_potion_3():
        potion_strength = 2
        print(potion_strength)
    drink_potion_3()
