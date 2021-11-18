import os
from pandas.plotting import register_matplotlib_converters
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis
register_matplotlib_converters()

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

df_yearly = pd.read_csv(os.path.join(
    LOCATION, 'data/annual_deaths_by_clinic.csv'))
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv(os.path.join(LOCATION, 'data/monthly_deaths.csv'),
                         parse_dates=['date'])

# Data Exploration

print(df_monthly.shape)
print(df_monthly.head())

print(df_yearly.shape)
print(df_yearly.head())

print(df_monthly.info())
print(df_yearly.info())
