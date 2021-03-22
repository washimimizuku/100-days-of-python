import os


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME = "weather_data.csv"
FULL_PATH = os.path.join(LOCATION, FILENAME)


# Using CSV lib
import csv

with open(FULL_PATH) as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Using pandas lib
import pandas

data = pandas.read_csv(FULL_PATH)
print(data["temp"])
