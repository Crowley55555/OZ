import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Создаем DataFrame с данными
np.random.seed(42)  # Для воспроизводимости результатов
data = {
    'Ученик': [f'Ученик_{i}' for i in range(1, 11)],
    'Математика': np.random.randint(2, 6, size=10),
    'Физика': np.random.randint(2, 6, size=10),
    'Химия': np.random.randint(2, 6, size=10),
    'Литература': np.random.randint(2, 6, size=10),
    'История': np.random.randint(2, 6, size=10)
}

df = pd.DataFrame(data)

# 2. Выводим первые несколько строк DataFrame
print("Первые 5 строк данных:")
print(df.head())
print("\n")

# 3. Вычисляем среднюю оценку по каждому предмету
mean_grades = df.mean(numeric_only=True)
print("Средние оценки по предметам:")
print(mean_grades)
print("\n")

# 4. Вычисляем медианную оценку по каждому предмету
median_grades = df.median(numeric_only=True)
print("Медианные оценки по предметам:")
print(median_grades)
print("\n")

# 5. Вычисляем Q1, Q3 и IQR для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("Статистика по математике:")
print(f"Q1 (25-й перцентиль): {Q1_math}")
print(f"Q3 (75-й перцентиль): {Q3_math}")
print(f"IQR (интерквартильный размах): {IQR_math}")
print("\n")

# 6. Вычисляем стандартное отклонение
std_dev = df.std(numeric_only=True)
print("Стандартное отклонение по предметам:")
print(std_dev)

# Дополнительно: визуализация средних оценок по предметам
plt.figure(figsize=(10, 5))
mean_grades.plot(kind='bar', color='skyblue')
plt.title('Средние оценки по предметам')
plt.xlabel('Предметы')
plt.ylabel('Средняя оценка')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()