# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

true_count = 0
love_count = 0

true_count += (lowercase_name1.count("t") + lowercase_name2.count("t"))
true_count += (lowercase_name1.count("r") + lowercase_name2.count("r"))
true_count += (lowercase_name1.count("u") + lowercase_name2.count("u"))
true_count += (lowercase_name1.count("e") + lowercase_name2.count("e"))

love_count += (lowercase_name1.count("l") + lowercase_name2.count("l"))
love_count += (lowercase_name1.count("o") + lowercase_name2.count("o"))
love_count += (lowercase_name1.count("v") + lowercase_name2.count("v"))
love_count += (lowercase_name1.count("e") + lowercase_name2.count("e"))

score = true_count * 10 + love_count

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
