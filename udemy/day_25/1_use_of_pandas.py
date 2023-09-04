# WORK MANUALLY, NOO
# with open("./weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)
#

import csv

# WORK csv module, Maybe
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# WORK with pandas! Yes, also for data analysis

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

print(data.to_dict())
temp_list = data["temp"].tolist()
print(temp_list)

total = sum(temp_list)
avg_tmp = round(float(total / len(temp_list)), 2)

print(f"AVG: {avg_tmp}")

# By using pandas
print(f"AVG: {round(data['temp'].mean(), 2)}")
print(f"Max: {data['temp'].max()}")

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get data in a specific row
print(data[data.day == "Monday"])
# Output: "0  Monday    12     Sunny"

print("**************************")
#  Get data in the row with max temp
maximum = data.temp.max()
print(data[data.temp == maximum])
print("**************************")

monday = data[data.day == "Monday"]
print(monday.condition)

# monday's temperature in Faranait not Celcius
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
