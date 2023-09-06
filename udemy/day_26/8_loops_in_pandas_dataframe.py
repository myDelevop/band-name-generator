import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for(key, value) in student_dict.items():
    print(value)

# What's about pandas dataframe?
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#  Loop through dataframe
for (key, value) in student_data_frame.items():
    print(value)


print("***********************************")
# Not useful, pandas has in-built loop
# Loops through rows of a dataframe
print("indexes:")
for(index, row) in student_data_frame.iterrows():
    print(index)
print("***********************************")
print("rows:")
for(index, row) in student_data_frame.iterrows():
    print(row)
    print("")
    print(row.student)
    print(row.score)

print("***********************************")
