import numpy as np

# Данные
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([0.10, 0.21, 0.43, 0.51, 0.62, 0.81, 1.01, 1.23, 1.47, 1.53, 1.75, 2.25])

# Вычисление z = e^(0.1 * x)
z = np.exp(0.1 * x)

# Количество наблюдений
n = len(x)

# Вычисление сумм
sum_z = np.sum(z)
sum_y = np.sum(y)
sum_zy = np.sum(z * y)
sum_z2 = np.sum(z**2)

# Формула для β1
beta_1 = (n * sum_zy - sum_z * sum_y) / (n * sum_z2 - sum_z**2)

# Формула для β0
beta_0 = (sum_y - beta_1 * sum_z) / n

# Сумма модулей
sum_of_modulus = abs(beta_0) + abs(beta_1)

# Вывод результатов
print(f"Оценки параметров: β0 = {beta_0:.5f}, β1 = {beta_1:.5f}")
print(f"Сумма модулей параметров: {sum_of_modulus:.3f}")