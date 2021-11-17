import os
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

df_data = pd.read_csv(os.path.join(LOCATION, 'data/nobel_prize_data.csv'))

# Data Exploration and Cleaning

print(df_data.shape)
print(df_data.head())
print(df_data.tail())
print(df_data.info())

# Check for Duplicates
print(f'Any duplicates? {df_data.duplicated().values.any()}')

# Check for NaN Values
print(f'Any duplicates? {df_data.duplicated().values.any()}')
print(df_data.isna().sum())

col_subset = ['year', 'category', 'laureate_type',
              'birth_date', 'full_name', 'organization_name']
print(df_data.loc[df_data.birth_date.isna()][col_subset])

col_subset = ['year', 'category', 'laureate_type',
              'full_name', 'organization_name']
print(df_data.loc[df_data.organization_name.isna()][col_subset])

# Type Conversions

# Birth Date
df_data.birth_date = pd.to_datetime(df_data.birth_date)

# Prize Share
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

print(df_data.info())
