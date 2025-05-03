import numpy as np
import matplotlib.pyplot as plt

# 1. Гистограмма для нормального распределения
plt.figure(figsize=(12, 5))

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация данных
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

# 2. Диаграмма рассеяния для случайных данных
plt.subplot(1, 2, 2)

# Генерация двух наборов случайных данных
x = np.random.rand(50)
y = np.random.rand(50)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='red', alpha=0.6)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')

plt.tight_layout()
plt.show()