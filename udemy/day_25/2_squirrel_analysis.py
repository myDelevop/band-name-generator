import pandas
import random

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
distinctFurColor = data["Primary Fur Color"].dropna().unique().tolist()

fur_color_list = []
count_list = []

data_dict = {
    "Fur Color": fur_color_list,
    "Count:": count_list
}

for color in distinctFurColor:
    fur_color_list.append(color)
    count_list.append(len(data[data["Primary Fur Color"] == color]))


aggregated_data = pandas.DataFrame(data_dict)
print(aggregated_data)

csv = aggregated_data.to_csv("squirrel_count.csv")

