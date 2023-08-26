# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

two_digit_int = int(two_digit_number)
float_division = two_digit_int / 10

division_str = str(float_division)

first_int = int(division_str[0])
second_int = int(division_str[2])

print(first_int + second_int)
