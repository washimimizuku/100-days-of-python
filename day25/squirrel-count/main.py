import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

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

df.to_csv("squirrel_count.csv")
