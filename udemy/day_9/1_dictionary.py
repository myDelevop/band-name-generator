programming_dictionary = {
    "Bug": "An error in a program that prevents the program for running as expected.",
    "Function": "A piece of code that you can easily  call over and over again",
    # "Loop": "The action of doing something over and over again",
}

#  Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Loop"])

# Create an empty dictionary
empty_list = []
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "a moth in your computer"

print(programming_dictionary)

print("************************")
# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
print("************************")

# Wipe an existing dictionary
programming_dictionary = {}
