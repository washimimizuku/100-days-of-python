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

# Percentage of Male vs. Female Winners
biology = df_data.sex.value_counts()
fig = px.pie(labels=biology.index,
             values=biology.values,
             title="Percentage of Male vs. Female Winners",
             names=biology.index,
             hole=0.4,)

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

fig.show()

# First 3 Women
print(df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3])

# Who won more than once
is_winner = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner]
print(f'There are {multiple_winners.full_name.nunique()}'
      ' winners who were awarded the prize more than once.')

col_subset = ['year', 'category', 'laureate_type', 'full_name']
print(multiple_winners[col_subset])

# Number of prizes per category
print(df_data.category.nunique())

prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale='Aggrnyl',
    title='Number of Prizes Awarded per Category')

v_bar.update_layout(xaxis_title='Nobel Prize Category',
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
v_bar.show()

# First Economics Prize
print(df_data[df_data.category == 'Economics'].sort_values('year')[:3])

# Male and Female winners by category
cat_men_women = df_data.groupby(['category', 'sex'],
                                as_index=False).agg({'prize': pd.Series.count})
cat_men_women.sort_values('prize', ascending=False, inplace=True)

print(cat_men_women)

v_bar_split = px.bar(x=cat_men_women.category,
                     y=cat_men_women.prize,
                     color=cat_men_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')
v_bar_split.show()

# Prizes Over Time

prize_per_year = df_data.groupby(by='year').count().prize
moving_average = prize_per_year.rolling(window=5).mean()

plt.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100,)

plt.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3,)

plt.show()

np.arange(1900, 2021, step=5)

plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax = plt.gca()  # get current axis
ax.set_xlim(1900, 2020)

ax.scatter(x=prize_per_year.index,
           y=prize_per_year.values,
           c='dodgerblue',
           alpha=0.7,
           s=100,)

ax.plot(prize_per_year.index,
        moving_average.values,
        c='crimson',
        linewidth=3,)

plt.show()

# Prizes Shared
yearly_avg_share = df_data.groupby(
    by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()  # create second y-axis
ax1.set_xlim(1900, 2020)

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100,)

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3,)

# Adding prize share plot on second axis
ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3,)

plt.show()

plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

# Can invert axis
ax2.invert_yaxis()

ax1.scatter(x=prize_per_year.index,
            y=prize_per_year.values,
            c='dodgerblue',
            alpha=0.7,
            s=100,)

ax1.plot(prize_per_year.index,
         moving_average.values,
         c='crimson',
         linewidth=3,)

ax2.plot(prize_per_year.index,
         share_moving_average.values,
         c='grey',
         linewidth=3,)

plt.show()
