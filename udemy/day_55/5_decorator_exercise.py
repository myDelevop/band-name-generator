# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        return_method = function(*args)
        fun_name = function.__name__
        args_str = "("
        for arg in args:
            args_str = args_str + str(arg) + ", "
        args_str = args_str + ")"
        args_str = args_str.replace(", )", ")")

        print(f"You called {fun_name}{args_str}\n")
        print(f"It returned {return_method}")

    return wrapper


# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(2, 2, 6)
