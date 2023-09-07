# The next line ALWAYS goes in KeyError
# raise KeyError("This is an error that I made up.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
