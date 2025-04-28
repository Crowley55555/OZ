import pandas as pd

# Создание простого Series (одномерного массива с индексами)
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

# Создание DataFrame (таблицы данных) из словаря
# Ключи словаря становятся названиями колонок
# Значения словаря - это списки данных для каждой колонки
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}

df = pd.DataFrame(data)
print(df)

# Чтение данных из CSV-файла в DataFrame
df = pd.read_csv('World-happiness-report-2024.csv')

# Вывод первых 3 строк таблицы
print(df.head(3))
# Вывод последних 3 строк таблицы
print(df.tail(3))
# Вывод общей информации о таблице (количество строк, типы данных и т.д.)
print(df.info())
# Вывод статистической информации по числовым колонкам
print(df.describe())
# Фильтрация данных - вывод строк, где значение в колонке 'Healthy life expectancy' > 0.7
print(df.loc[df['Healthy life expectancy'] > 0.7])

# Чтение другого CSV-файла
df = pd.read_csv('hh.csv')

# Добавление новой колонки 'Test' со значениями от 0 до 28
df['Test'] = [new for new in range(29)]
print(df)

# Удаление колонки 'Test' (axis=1 означает работу с колонками, inplace=True - изменение исходного DataFrame)
df.drop('Test', axis=1, inplace=True)
print(df)

# Удаление строки с индексом 28 (axis=0 означает работу со строками)
df.drop(28, axis=0, inplace=True)
print(df)

# Чтение CSV-файла с данными о животных
df = pd.read_csv('animal.csv')
print(df)

# Замена всех пропущенных значений (NaN) на 0
df.fillna(0, inplace=True)
print(df)

# Альтернативный вариант: удаление строк с пропущенными значениями
# df.dropna(inplace=True)
# print(df)

# Группировка данных по колонке 'Пища' и расчет среднего значения продолжительности жизни для каждой группы
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

# Сохранение DataFrame в CSV-файл (index=False - не сохранять индексы)
df.to_csv('out_animal.csv', index=False)
