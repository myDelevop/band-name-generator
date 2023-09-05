file_1 = open("file1.txt", "r")
lines_1 = file_1.readlines()

file_2 = open("file2.txt", "r")
lines_2 = file_2.readlines()

# Cleaning
lines_1 = [int((line.strip())) for line in lines_1]
lines_2 = [int((line.strip())) for line in lines_2]
print(lines_1)
print(lines_2)

result = [num for num in lines_1 if num in lines_2]

# Write your code above 👆

print(result)


