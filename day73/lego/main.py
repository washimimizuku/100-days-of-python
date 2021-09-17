import os
import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.float_format = '{:,.2f}'.format

LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

# Data Exploration
colors = pd.read_csv(os.path.join(LOCATION, 'data/colors.csv'))
print(colors.head())
print(colors['name'].nunique())
print(colors.groupby('is_trans').count())
print(colors.is_trans.value_counts())

# Understanding LEGO Themes vs. LEGO Sets
sets = pd.read_csv(os.path.join(LOCATION, 'data/sets.csv'))
print(sets.head())
print(sets.tail())
print(sets.sort_values('year').head())
print(sets[sets['year'] == 1949])
print(sets.sort_values('num_parts', ascending=False).head())

# Sets per year
sets_by_year = sets.groupby('year').count()
print(sets_by_year['set_num'].head())
print(sets_by_year['set_num'].tail())

plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.show()

plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show()

# Aggregate data
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
print(themes_by_year.head())
print(themes_by_year.tail())

plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.show()

# Line charts with 2 separate axis
ax1 = plt.gca()  # get the axis
ax2 = ax1.twinx()  # create another axis that shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
plt.show()

# Parts per set
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})

print(parts_per_set.head())
print(parts_per_set.tail())

# Scatter plots
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
plt.show()

# Number of sets per lego theme
set_theme_counts = sets["theme_id"].value_counts()

print(set_theme_counts.head())

# Themes
themes = pd.read_csv(os.path.join(LOCATION, 'data/themes.csv'))

print(themes.head())
print(themes[themes.name == 'Star Wars'])
print(sets[sets.theme_id == 18])
print(sets[sets.theme_id == 209])

# Merging
set_theme_count = sets["theme_id"].value_counts()

print(set_theme_count[:5])

set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})

print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, themes, on='id')

print(merged_df[:3])

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()
