file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

print("\n******************************************************************\n")

# if we usually forget to close the file we can use with clause
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# Write a file. Be careful mode=w gives you the permission to write the file. It overrides all the content
with open("my_file.txt", mode="w") as file:
    file.write("New text from python")

# If we use mode=a, it means append. The file is not deleted and it writes from the end
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is a new line")

#  mode=w allows also to create a new file from scratch
with open("my_file_m.txt", mode="w") as file:
    file.write("New File from python")
