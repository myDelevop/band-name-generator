# positional arguments
def greet_with(name, location):
    print("Hello " + name)
    print(f"What is it like in {location}?")


# functions with keyword arguments
# def my_function(c=3, b=2, a=1) it is exactly the same, the position doesn't matter
def my_function(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)
    print("\n")


def greet_with_kw_args(location="Dublin", name="Rocco"):  # switched parameters
    print("Hello " + name)
    print(f"What is it like in {location}?")
    print("\n")


greet_with("Rocco", "Dublin")

my_function()  # with default values
my_function(4, 8, 3)  # with custom values

greet_with_kw_args()
greet_with_kw_args("New York", "Ciccio")