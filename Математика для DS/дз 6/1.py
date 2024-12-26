import numpy as np

# Данные из таблицы
X = np.array([51, 67, 84, 81, 101, 109, 71, 97, 109, 51, 105, 89])
Y = np.array([25, 30, 43, 44, 57, 58, 43, 46, 62, 45, 55, 45])

# Количество точек
n = len(X)

# Расчёт средних значений X и Y
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Расчёт коэффициента наклона (b1) и свободного члена (b0)
numerator = np.sum((X - mean_X) * (Y - mean_Y))  # Числитель
denominator = np.sum((X - mean_X) ** 2)         # Знаменатель

b1 = numerator / denominator  # Уклон
b0 = mean_Y - b1 * mean_X     # Свободный член

# Сумма модулей коэффициентов
sum_abs_params = abs(b1) + abs(b0)

# Вывод результатов
print("Коэффициент наклона (b1):", b1)
print("Свободный член (b0):", b0)
print("Сумма модулей коэффициентов:", sum_abs_params)