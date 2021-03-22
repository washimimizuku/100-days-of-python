import os
import pandas


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME_WEATHER_DATA = "weather_data.csv"
FILENAME_NEW_DATA = "new_data.csv"
FULL_PATH_WEATHER_DATA = os.path.join(LOCATION, FILENAME_WEATHER_DATA)
FULL_PATH_NEW_DATA = os.path.join(LOCATION, FILENAME_NEW_DATA)


data = pandas.read_csv(FULL_PATH_WEATHER_DATA)
print(data)

# Transform CSV data to dictionary
data_dict = data.to_dict()
print(data_dict)

# Transform column to list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculate valies based on columns
average = data["temp"].mean()
print(average)

max = data["temp"].max()
print(max)

# Get data in columns
print(data['condition'])
print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# Save dataframe as CSV
data.to_csv(FULL_PATH_NEW_DATA)