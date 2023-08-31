from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 -n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("It's impossible to divide by 0")
        return
    return n1 / n2

print(logo)

dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for key in dictionary:
    print(key)

operation = input("Pick an operation from the line above: ")
if dictionary.__contains__(operation):
    first_answer = dictionary[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {first_answer}")


operation = input("Pick another operation")
num3 = int(input("What's the next number?: "))
if dictionary.__contains__(operation):
    seconnd_answer = dictionary[operation](first_answer, num3)
    print(f"{first_answer} {operation} {num3} = {seconnd_answer}")
