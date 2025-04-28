import pandas as pd

df = pd.read_csv('ai_computer_vision_dataset.csv')
print(df.head(5))
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')
print(df)
print(df.info())
print(df.describe())
average_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()
print(average_salary_by_city)
df.to_csv('average_salary_by_city.csv', index=False)