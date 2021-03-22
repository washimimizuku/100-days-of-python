import os
import pandas


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME_SQUIRREL_CENSUS = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
FILENAME_SQUIRREL_COUNT = "squirrel_count.csv"
FULL_PATH_SQUIRREL_CENSUS = os.path.join(LOCATION, FILENAME_SQUIRREL_CENSUS)
FULL_PATH_SQUIRREL_COUNT = os.path.join(LOCATION, FILENAME_SQUIRREL_COUNT)


data = pandas.read_csv(FULL_PATH_SQUIRREL_CENSUS)

fur_color_column = data["Primary Fur Color"]

gray_squirrels_count = len(data[fur_color_column == "Gray"])
red_squirrels_count = len(data[fur_color_column == "Cinnamon"])
black_squirrels_count = len(data[fur_color_column == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count] 
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv(FULL_PATH_SQUIRREL_COUNT)
