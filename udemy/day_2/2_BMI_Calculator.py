# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# print(type(height))  str
# print(type(weight)) # str

float_height = float(height)
float_weight = float(weight)


BMI = float_weight / (float_height ** 2)

int_BMI = int(BMI)
print(int_BMI)
