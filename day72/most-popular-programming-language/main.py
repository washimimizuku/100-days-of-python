import os
import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.float_format = '{:,.2f}'.format

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
FULL_PATH = os.path.join(LOCATION, 'QueryResults.csv')

df = pd.read_csv(FULL_PATH,
                 header=0, names=['DATE', 'TAG', 'POSTS'])

# Data exploration

print(df.head())
print(df.tail())
print(df.shape)
print(df.count())
print(df.groupby('TAG').sum().sort_values('POSTS', ascending=False))
print(df.groupby('TAG').count().sort_values('POSTS', ascending=False))

# Data cleaning

print(df['DATE'][1])
print(df.DATE[1])
print(type(df['DATE'][1]))
print(pd.to_datetime(df.DATE[1]))
print(type(pd.to_datetime(df.DATE[1])))

df.DATE = pd.to_datetime(df.DATE)
print(df.head())

# Data manipulation

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.head())
print(reshaped_df.tail())
print(reshaped_df.count())

reshaped_df.fillna(0, inplace=True)
print(reshaped_df.head())
print(reshaped_df.isna().values.any())

# Data Visualisaton with with Matplotlib

plt.plot(reshaped_df.index, reshaped_df.java)
plt.show()


plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.show()


plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
plt.show()


plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# Plot all languages using for loop
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)
plt.show()


roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# Plot all languages using for loop
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()
