############  DEBUGGING  #####################

from random import randint


# Describe Problem
def my_function():
    # Nothing is printed because the last value of i is = to 19
    # for i in range(1, 20): 🐞
    for i in range(1, 21):  # Bug fixed 😃
        if i == 20:
            print("You got it")


my_function()

dice_img = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) lists go from 0 to n-1 🐞
dice_num = randint(0, 5)  # Bug fixed  😃
print(dice_img[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: 🐞
if year > 1980 and year <= 1994:  # Bug fixed  😃
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")  # the input is not comparable with number 18 🐞
age = int(input("How old are you?"))  # Bug fixed  😃
if age > 18:
    # print("You can drive at age {age}.") => Missing indentation after if statement 🐞
    # print("You can drive at age {age}.") => Missing f in print statement 🐞
    print(f"You can drive at age {age}.")  # Bug fixed  😃

# Print is Your Friend
# pages = 0 we can comment - Bug fixed 😃
# word_per_page = 0 we can comment - Bug fixed 😃
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # this is not an assignment 🐞
word_per_page = int(input("Number of words per page: "))  # Bug fixed  😃
total_words = pages * word_per_page
print(total_words)


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # b_list.append(new_item)  not a correct indentation 🐞
        # print(b_list)  not a correct indentation 🐞
        b_list.append(new_item)  # Bug fixed 😃
        print(b_list)  # Bug fixed 😃


mutate([1, 2, 3, 5, 8, 13])
