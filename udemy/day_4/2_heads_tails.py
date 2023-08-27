import random

# import my_module
# print(my_module.pi) Not in this exercise

random_number = random.randint(0, 1)
# print(random_number)

if random_number == 1:
    print("Heads")
elif random_number == 0:
    print("Tails")
else:
    print("Error!")
