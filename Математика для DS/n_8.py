import numpy as np

# Задаем матрицу A и вектор b
A = np.array([
    [4, -1, 0, -1, 0, 0],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
], dtype=float)

b = np.array([0, 5, 0, 6, -2, 6], dtype=float)

# Решаем систему линейных уравнений A y = b
y = np.linalg.solve(A, b)

# Вычисляем L2-норму найденного решения
x_star_norm = np.linalg.norm(y, ord=2)
print(f"||X*||_2 = {x_star_norm:.3f}")