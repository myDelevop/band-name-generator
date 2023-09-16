# Python Decorator  Function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        print("After two seconds:")
        # Do something before
        function()
        # function() uncomment to call the function twice

        # Do something after
        print("\n")

    return wrapper_function


@delay_decorator
def say_hello():
    # time.sleep(2) sleeps inside the decorator
    print("Hello")


@delay_decorator
def say_bye():
    # time.sleep(2) sleeps inside the decorator
    print("Bye")


def say_greeting():
    # This doesn't sleep because it hasn't the decorator
    print("How are you?")


say_hello()
say_bye()
say_greeting()


# if we want decorate say_greeting(), of course we can use the @ syntax but the long way to do thinks is:
print("*******************************************************")
decorated_function = delay_decorator(say_greeting)
decorated_function()
