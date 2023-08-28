import random

# Write your code below this line 👇
print("Hello World!")
print("Hello World!\nHello World!")
print("Hello " + "Rocco")  # print("Hello" + " Rocco") # print("Hello " + " " + "Rocco")

# input("What is your name?")
# print("Hello " + input("What is your name? "))


# Use of variables to save the input name
name = input("What is your name? ")
print(name)
print(len(name))
# print(len(8)) Error

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.") ERROR!
print(type(num_char))
print("Your name has " + str(num_char) + " characters.")

# String
print("Hello"[0])  # returns H, we start from 0
print("Hello"[4])  # returns o, we start from 0pr
int("123" + "345")  # string concatenation

# Integer
print(123 + 345)  # sum is OK
print(123_456_122)  # in Python, we can use _ like the comma thousands separator

# Float, floating point (it is how the PC really deals with numbers in the lowest level)
print("Pi is: + " + str(3.14159))

# Boolean (True or False)
if True:
    print("Of course I'll print it! It's true")
else:
    print("Never here")

a = 123
b = float(123)
c = str(123)
print(type(a))
print(type(b))
print(type(c))

print(70 + float("100.5"))  # It prints a float num
print(str(70) + str(100))  # It prints the string 70100

print(3 * 3 + 3 / 3 - 3)  # maths precedences

print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)  # floating division

result = 4 / 2
result /= 2
print(result)

score = 0
# User scores a point
score = score + 1
score += 1
score -= 1
# ....

score = 5
height = 1.84
isWinning = True
print("Your score is " + str(score) + ".......... BORING! Let's use f-String")  # BORING
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")  # OK

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm?"))

'''
if height >= 120:
    print("You can ride the roller-coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''

'''
if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''

'''
if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''

bill = 0

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do tou want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()  # it goes between 0 and 1
print(random_float)

# how can we create a decimal between 0 and 5?
random_0_5 = random.randint(0, 5) + random.random()
print(random_0_5)

# we can do the same by multiplying random by 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# lists in which order is important
states = ["Delaware", "Pennsylvania", "...", "Hawaii"]

print(states[0])  # is the first US State
print(states[len(states)-1])  # is the last US State

states.append("RoccoLand")  # RoccoLand join the USA
print(states[len(states)-1])  # is the last US State

states.extend(["state_2031", "state_2032", "state_future"])
print(states[len(states)-1])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
               "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen_1 = [fruits, vegetables]

print(dirty_dozen_1[0][3])

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
