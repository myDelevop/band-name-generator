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
