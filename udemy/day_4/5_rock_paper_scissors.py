import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

PC_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
images = [rock, paper, scissors]

print("PC choice: " + images[PC_choice])
print("\n\n")
print("User choice: " + images[user_choice])

if PC_choice == 0:
    # PC with Rock
    if user_choice == 0:
        print("Draw")
    elif user_choice == 1:
        print("You win!")
    elif user_choice == 2:
        print("You lose")

elif PC_choice == 1:
    # PC with Paper
    if user_choice == 0:
        print("You lose")
    elif user_choice == 1:
        print("Draw")
    elif user_choice == 2:
        print("You Win!")

elif PC_choice == 2:
    # PC with Scissors
    if user_choice == 0:
        print("You win!")
    elif user_choice == 1:
        print("You lose")
    elif user_choice == 2:
        print("It's a Draw")
