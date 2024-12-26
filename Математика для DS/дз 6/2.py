import numpy as np

x = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
y = np.array([0.4, 0.3, 1, 1.7, 2.1, 3.4, 4.1, 5.8, 7.7, 9.4, 11.4, 13.6, 15.6, 18.6, 21.2, 24.1])

# Расчет необходимых сумм для формул
n = len(x)  # Количество элементов
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum(xi**2 for xi in x)
sum_x3 = sum(xi**3 for xi in x)
sum_x4 = sum(xi**4 for xi in x)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2y = sum(xi**2 * yi for xi, yi in zip(x, y))

# Формируем элементы матрицы
A = [
    [n, sum_x, sum_x2],
    [sum_x, sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
]

B = [sum_y, sum_xy, sum_x2y]

# Решаем систему уравнений методом Крамера
# Определитель матрицы A
def determinant_3x3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

det_A = determinant_3x3(A)

# Матрицы для расчета β0, β1 и β2
A0 = [B, A[1], A[2]]  # Подставляем B в первый столбец
A1 = [[A[0][0], B[0], A[0][2]], [A[1][0], B[1], A[1][2]], [A[2][0], B[2], A[2][2]]]  # Во второй столбец
A2 = [[A[0][0], A[0][1], B[0]], [A[1][0], A[1][1], B[1]], [A[2][0], A[2][1], B[2]]]  # В третий столбец

# Вычисление коэффициентов
beta_0 = determinant_3x3(A0) / det_A
beta_1 = determinant_3x3(A1) / det_A
beta_2 = determinant_3x3(A2) / det_A

# Вывод результатов
print(f"Оценки параметров:")
print(f"β0 = {beta_0:.4f}")
print(f"β1 = {beta_1:.4f}")
print(f"β2 = {beta_2:.4f}")
print(f"Сумма параметров:")
print(abs(beta_0)+abs(beta_1)+abs(beta_2))
