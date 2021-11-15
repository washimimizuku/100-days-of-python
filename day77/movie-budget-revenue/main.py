import os
from pandas.plotting import register_matplotlib_converters
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()


LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

data = pd.read_csv(os.path.join(LOCATION, 'data/cost_revenue_dirty.csv'))

# Explore Data

print(data.shape)
print(data.head())
print(data.tail())

print(f'NaN values present? {data.isna().values.any()}')
print(f'Duplicated values present? {data.duplicated().values.any()}')

duplicated_rows = data[data.duplicated()]
print(f'Number of duplicated rows? {len(duplicated_rows)}')

print(data.info())

# Data Type Conversions

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

data.Release_Date = pd.to_datetime(data.Release_Date)

print(data.head())
print(data.info())
print(data.describe())
print(data[data.USD_Production_Budget == 1100.00])
print(data[data.USD_Production_Budget == 425000000.00])

# Zero Revenue Films

zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))

# Filter on Multiple Conditions

international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]
print(f'Number of international releases: {len(international_releases)}')
print(international_releases.head())

international_releases = data.query(
    'USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
print(international_releases.tail())

# Unreleased Films

# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')

future_releases = data[data.Release_Date >= scrape_date]
print(f'Number of unreleased movies: {len(future_releases)}')
print(future_releases)

# Clean Data (remove future releases)
data_clean = data.drop(future_releases.index)

# Films that lost money

money_losing = data_clean.loc[data_clean.USD_Production_Budget >
                              data_clean.USD_Worldwide_Gross]
print(len(money_losing)/len(data_clean))

money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
print(money_losing.shape[0]/data_clean.shape[0])

# Seaborn bubble charts

sns.scatterplot(data=data_clean,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')
plt.show()

plt.figure(figsize=(8, 4), dpi=200)

sns.scatterplot(data=data_clean,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')

plt.show()

plt.figure(figsize=(8, 4), dpi=200)

ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross')

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')

plt.show()

# Plotting Movie Release Over Time

plt.figure(figsize=(8, 4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross',  # colour
                     size='USD_Worldwide_Gross',)  # dot size

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)

plt.show()

plt.figure(figsize=(8, 4), dpi=200)

# set styling on a single chart
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=data_clean,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

plt.show()

plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross',)

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

plt.show()

# Convert Years to Decades

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

decades = years//10*10
data_clean['Decade'] = decades

# Separate old from new

old_films = data_clean[data_clean.Decade <= 1960]

print(old_films.describe())
print(old_films.sort_values('USD_Production_Budget', ascending=False).head())


new_films = data_clean[data_clean.Decade > 1960]

print(new_films.describe())
print(new_films.sort_values('USD_Production_Budget', ascending=False).head())

# Seaborn Regression Plots

sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')
plt.show()

plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})
plt.show()

plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')
plt.show()

# Calculate regressions with scikit-learn

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)

# Coefficient
print(f'The slope coefficient is: {regression.coef_[0]}')

# Intercept
print(f'The intercept is: {regression.intercept_[0]}')

# R-squared
print(f'The r-squared is: {regression.score(X, y)}')

# Old films
X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)

print(f'The slope coefficient is: {regression.coef_[0]}')
print(f'The intercept is: {regression.intercept_[0]}')
print(f'The r-squared is: {regression.score(X, y)}')

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0, 0]*budget
revenue_estimate = round(revenue_estimate, -6)

print(
    f'The estimated revenue for a $350 million film is around ${revenue_estimate:.10}.')
