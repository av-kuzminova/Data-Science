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

# Начальное приближение и параметры алгоритма
y = np.zeros(6)  # Начальное приближение y_0 = 0
tolerance = 1e-6  # Порог сходимости
max_iterations = 1000  # Максимальное количество итераций

# Метод наискорейшего спуска
for _ in range(max_iterations):
    gradient = 2 * A @ y - 2 * b  # Вычисляем градиент ∇f(y)
    if np.linalg.norm(gradient) < tolerance:  # Проверка на сходимость
        break
    alpha = (gradient @ gradient) / (gradient @ A @ gradient)  # Оптимальный шаг
    y = y - alpha * gradient  # Обновляем y

# Вычисляем L2-норму найденного решения
x_star_norm = np.linalg.norm(y, ord=2)
print(f"||X*||_2 = {x_star_norm:.3f}")