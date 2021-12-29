# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

average = data["temp"].mean()
max_number = data["temp"].max()
print(average)
print(max_number)

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data["day"] == "Monday"])
print((data[data.day == "Monday"]))

print((data[data.temp == data.temp.max()]))

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32

print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

