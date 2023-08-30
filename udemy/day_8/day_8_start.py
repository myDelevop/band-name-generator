# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("First print statement")
    print("Second print statement")
    print("Third print statement")


def greet_with_name(name):
    print("Hello " + name)
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today, {name}?")


greet()
greet_with_name("Rocco")
