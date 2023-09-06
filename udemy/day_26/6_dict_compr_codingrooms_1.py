sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_list = sentence.split(" ")

result = {name: len(name) for name in sentence_list}

print(result)
