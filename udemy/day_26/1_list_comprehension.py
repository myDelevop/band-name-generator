# List comprehension
numbers = [1, 2, 3]  # instead of create a new list for loop add each item+1
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Rocco"
new_name = [letter for letter in name]
print(new_name)

doubled_numbers = [n*2 for n in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Get names only if the length is less or equal to 4
new_names = [name for name in names if len(name) <= 4]
print(new_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
