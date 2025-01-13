import numpy as np
import matplotlib.pyplot as plt

# N = 21, интервал [-N, N+1]
N = 21
interval = (-N, N + 1)

# Генерация случайных вещественных значений (100 значений)
data = np.random.uniform(interval[0], interval[1], 100)

# A) Описательная статистика
mean_value = np.mean(data)  # Среднее значение
median_value = np.median(data)  # Медиана
std_dev = np.std(data)  # Стандартное отклонение
min_value = np.min(data)  # Минимальное значение
max_value = np.max(data)  # Максимальное значение
range_value = max_value - min_value  # Размах (Range)
q1 = np.percentile(data, 25)  # Первый квартиль (Q1)
q3 = np.percentile(data, 75)  # Третий квартиль (Q3)
iqr = q3 - q1  # Межквартильный размах (IQR)

# Вывод описательных статистик
print(f"Среднее значение: {mean_value}")
print(f"Медиана: {median_value}")
print(f"Стандартное отклонение: {std_dev}")
print(f"Минимальное значение: {min_value}")
print(f"Максимальное значение: {max_value}")
print(f"Размах: {range_value}")
print(f"Первый квартиль (Q1): {q1}")
print(f"Третий квартиль (Q3): {q3}")
print(f"Межквартильный размах (IQR): {iqr}")

# B) "ящик с усами"
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("Boxplot: Random Data in Interval [-21, 22]")
plt.xlabel("Value")
plt.grid(True)
plt.show()