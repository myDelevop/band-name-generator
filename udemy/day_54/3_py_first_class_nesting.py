def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments e.g. int/string/float

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 2, 3)
print(result)

result = calculate(add, 2, 3)
print(result)


# Nested functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()  # we can only call the nested function inside the outer function tabulation


# How to call the nested function? Scope inside the outer_function. We can't here
outer_function()


# Return function from another function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


# Now we can call the inner function outside from the outside function because it returns a function
nested_fun = outer_function()
nested_fun()
nested_fun()
