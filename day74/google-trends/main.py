from pandas.plotting import register_matplotlib_converters
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

df_tesla = pd.read_csv(os.path.join(
    LOCATION, 'data/TESLA_Search_Trend_vs_Price.csv'))

df_btc_search = pd.read_csv(os.path.join(
    LOCATION, 'data/Bitcoin_Search_Trend.csv'))
df_btc_price = pd.read_csv(os.path.join(
    LOCATION, 'data/Daily_Bitcoin_Price.csv'))

df_unemployment = pd.read_csv(os.path.join(
    LOCATION, 'data/UE_Benefits_Search_vs_UE_Rate_2004-19.csv'))

# Data Exploration

# Tesla
print(df_tesla.shape)
print(df_tesla.head())

print(
    f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(
    f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

print(df_tesla.describe())
# Unemployemnt

print(df_unemployment.shape)
print(df_unemployment.head())

print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

# Bitcoin
print(df_btc_price.shape)
print(df_btc_price.head())

print(df_btc_search.shape)
print(df_btc_search.head())

print(f'largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

# Data Cleaning

print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')

print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')

print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
print(df_btc_price[df_btc_price.CLOSE.isna()])

df_btc_price = df_btc_price.dropna()
df_btc_price.dropna(inplace=True)  # Alternative, same as above

print(df_tesla.MONTH.head())
print(type(df_tesla.MONTH[0]))

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

print(df_tesla.MONTH.head())

# Resample by last price in the month
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
# Alternative to resample by average price in the month:
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()

print(df_btc_monthly.shape)
print(df_btc_monthly.head())

# Data Visualisation

# Tesla Stock Price vs Search Trend

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price')
ax2.set_ylabel('Search Trend')

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH)

plt.show()

# Register date converters to avoid warning messages
register_matplotlib_converters()

# Tesla Stock Price vs Search Trend with colors

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E')  # hexa color
ax2.set_ylabel('Search Trend', color='skyblue')  # named color

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

plt.show()

# Tesla Stock Price vs Search Trend bigger

# Increases size and resolution
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

# Increase font size
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# Increase line width
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Tesla Stock Price vs Search Trend with axis formating

# Increases size and resolution
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

# Create locators for ticks on the time axis
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim(df_tesla.MONTH.min(), df_tesla.MONTH.max())

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Tesla Stock Price vs Search Trend final

# Increases size and resolution
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

# Create locators for ticks on the time axis
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim(df_tesla.MONTH.min(), df_tesla.MONTH.max())

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Btcoin News vs Resampled Price

plt.figure(figsize=(14, 8), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
         color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
         color='skyblue', linewidth=3, marker='o')

plt.show()

# Unemployment Search vs Actual Unemployment

plt.figure(figsize=(14, 8), dpi=120)
plt.title(
    'Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE,
         color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Rolling Unemployment Search vs Actual Unemployment

plt.figure(figsize=(14, 8), dpi=120)
plt.title(
    'Rolling Monthly US "Unemployment Benefits" Web Search vs UNRate', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(
    window=6).mean()

ax1.plot(df_unemployment.MONTH, roll_df.UNRATE,
         color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()

# Rolling Unemployment Search vs Actual Unemployment including 2020

df_ue_2020 = pd.read_csv(os.path.join(
    LOCATION, 'data/UE_Benefits_Search_vs_UE_Rate_2004-20.csv'))
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14, 8), dpi=120)
plt.title(
    'Monthly US "Unemployment Benefits" Web Searchvs UNRATE incl 2020', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, color='purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH,
         color='skyblue', linewidth=3)

plt.show()
