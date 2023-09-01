from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("It's impossible to divide by 0")
        return
    return n1 / n2


dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for key in dictionary:
        print(key)

    should_continue = True
    while should_continue == True:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        if dictionary.__contains__(operation):
            answer = dictionary[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
