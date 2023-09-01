game_level = 3
enemies = ["Skeleton", "Zombie", "Alies"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # OK

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alies"]
    if game_level < 5:
        new_one = enemies[0]
    print(new_one)  # OK

create_enemy()

# print(new_one) # NOT POSSIBLE
