import os
import pandas as pd
import plotly.express as px

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

df_apps = pd.read_csv(os.path.join(
    LOCATION, 'data/apps.csv'))

# Data Cleaning

print(df_apps.shape)
print(df_apps.head())
print(df_apps.sample(5))

# Drop unused columns
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
print(df_apps.head())

# Find and Remove NaN values in Ratings
nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
print(nan_rows.head())

df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)

# Find and remove duplicates
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
print(duplicated_rows.head())

print(df_apps_clean[df_apps_clean.App == 'Instagram'])

df_apps_clean = df_apps_clean.drop_duplicates()  # Not enough
print(df_apps_clean[df_apps_clean.App == 'Instagram'])

# We need to specify the subset got identifying duplicates
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
print(df_apps_clean[df_apps_clean.App == 'Instagram'])

print(df_apps_clean.shape)

# Find highest rated Apps
print(df_apps_clean.sort_values('Rating', ascending=False).head())

# Find 5 Largest Apps in terms of Size (MBs)
print(df_apps_clean.sort_values('Size_MBs', ascending=False).head())

# Find the 5 App with Most Reviews
print(df_apps_clean.sort_values('Reviews', ascending=False).head(50))

# Visualise Categorical Data: Content Ratings

ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)

fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()

fig = px.pie(labels=ratings.index, values=ratings.values,
             title="Content Rating", names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

fig = px.pie(labels=ratings.index, values=ratings.values,
             title="Content Rating", names=ratings.index, hole=0.6)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

# Numeric Type Conversion: Examine the Number of Installs

print(df_apps_clean.Installs.describe())

print(df_apps_clean.info())

print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

df_apps_clean.Installs = df_apps_clean.Installs.astype(
    str).str.replace(',', '')
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate

print(df_apps_clean.Price.describe())

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', '')
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

print(df_apps_clean.sort_values('Price', ascending=False).head(20))

# The most expensive apps sub $250
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values('Price', ascending=False).head(50))

# Highest Grossing Paid Apps (ballpark estimate)
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(
    df_apps_clean.Price)
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])

# Analysing App Categories

print(df_apps_clean.Category.nunique())

top10_category = df_apps_clean.Category.value_counts()[:10]
print(top10_category)

# Highest Competition (Number of Apps)
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

# Most Popular Categories (Highest Downloads)
category_installs = df_apps_clean.groupby(
    'Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = px.bar(x=category_installs.Installs,
               y=category_installs.index, orientation="h")
h_bar.show()

h_bar = px.bar(x=category_installs.Installs, y=category_installs.index,
               orientation="h", title='Category Popularity')
h_bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")
h_bar.show()

# Downloads vs. Competition
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
print(cat_number)

cat_merged_df = pd.merge(cat_number, category_installs,
                         on='Category', how='inner')
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
print(cat_merged_df.sort_values('Installs', ascending=False))

scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

scatter.show()

# Extracting Nested Data from a Column

print(len(df_apps_clean.Genres.unique()))
df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5]

# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

# Competition in Genres

bar = px.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')

bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)

bar.show()

# Free vs. Paid Apps per Category

print(df_apps_clean.Type.value_counts())

df_free_vs_paid = df_apps_clean.groupby(
    ["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
print(df_free_vs_paid.head())

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')

g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))

g_bar.show()

# Lost Downloads for Paid Apps

box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box.show()

# Revenue by App Category

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))


box.show()

# Paid App Pricing Strategies by Category

print(df_paid_apps.Price.median())

box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')

box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))

box.show()
