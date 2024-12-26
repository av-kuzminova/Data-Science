import numpy as np

# Данные
x = np.array([2.11, 2.45, 2.61, 2.73, 2.75, 2.81, 2.87, 2.91, 2.96, 3.03, 3.05, 3.12])
y = np.array([0.10, 0.21, 0.43, 0.51, 0.62, 0.81, 1.01, 1.23, 1.47, 1.53, 1.75, 2.25])

# Считаем необходимые суммы
n = len(x)
sum_x = np.sum(x)
sum_x2 = np.sum(x**2)
sum_sin_8x = np.sum(np.sin(8 * x))
sum_x_sin_8x = np.sum(x * np.sin(8 * x))
sum_sin_8x2 = np.sum(np.sin(8 * x)**2)
sum_y = np.sum(y)
sum_x_y = np.sum(x * y)
sum_sin_8x_y = np.sum(np.sin(8 * x) * y)

# Составляем матрицу системы нормальных уравнений
A = np.array([[n, sum_x, sum_sin_8x],
              [sum_x, sum_x2, sum_x_sin_8x],
              [sum_sin_8x, sum_x_sin_8x, sum_sin_8x2]])

B = np.array([sum_y, sum_x_y, sum_sin_8x_y])

# Решаем систему уравнений
beta = np.linalg.solve(A, B)

# Извлекаем найденные коэффициенты
beta_0, beta_1, beta_2 = beta

# Сумма модулей коэффициентов
sum_of_modulus = abs(beta_0) + abs(beta_1) + abs(beta_2)

# Вывод результатов
print(f"Оценки параметров: β0 = {beta_0:.4f}, β1 = {beta_1:.4f}, β2 = {beta_2:.4f}")
print(f"Сумма модулей параметров: {sum_of_modulus:.4f}")