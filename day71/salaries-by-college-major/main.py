import os
import pandas as pd


LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
FULL_PATH = os.path.join(LOCATION, 'salaries_by_college_major.csv')

df = pd.read_csv(FULL_PATH)
print(df.head())
