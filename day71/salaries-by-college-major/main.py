import os
import pandas as pd


LOCATION = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
FULL_PATH = os.path.join(LOCATION, 'salaries_by_college_major.csv')

df = pd.read_csv(FULL_PATH)
clean_df = df.dropna()
clean_df.tail()

print('Question 1: What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).')

mid_max = clean_df['Mid-Career Median Salary'].max()
print(f'Mid-Career Median Salary Maximum Value: {mid_max}')
mid_max_id = clean_df['Mid-Career Median Salary'].idxmax()
print(f'Mid-Career Median Salary Maximum ID: {mid_max_id}')
major_with_max_mid_salary = clean_df['Undergraduate Major'][8]
print(
    f'College major with highest mid-career salary: {major_with_max_mid_salary}')
print()

print('Question 2: Which college major has the lowest starting salary and how much do graduates earn after university?')

start_min = clean_df['Starting Median Salary'].min()
print(f'Starting Median Salary Minimum Value: {start_min}')
start_min_id = clean_df['Starting Median Salary'].idxmin()
print(f'Starting Median Salary Maximum ID: {mid_max_id}')
major_with_min_start_salary = clean_df['Undergraduate Major'].loc[start_min_id]
print(
    f'College major with lowest starting salary: {major_with_min_start_salary}')
print()

print('Question 3: Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?')

mid_min = clean_df['Mid-Career Median Salary'].min()
print(f'Mid-Career Median Salary Minimum Value: {mid_min}')
mid_min_id = clean_df['Mid-Career Median Salary'].idxmin()
print(f'Mid-Career Median Salary Lowest ID: {mid_min_id}')
major_with_min_mid_salary = clean_df['Undergraduate Major'].loc[mid_min_id]
print(
    f'College major with lowest mid-career salary: {major_with_min_mid_salary}')

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - \
    clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

print('Question 4: Find the top 5 degrees with the highest values in the 90th percentile.')
highest_potential = clean_df.sort_values(
    'Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential[['Undergraduate Major',
      'Mid-Career 90th Percentile Salary']].head())

print('Question 5: Which majors have the largest difference between high and low earners after graduation?')
highest_spread = clean_df.sort_values('Spread', ascending=False)
print(highest_spread[['Undergraduate Major', 'Spread']].head())
