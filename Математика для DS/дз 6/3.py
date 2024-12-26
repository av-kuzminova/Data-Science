import math

# Данные
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [2.11, 2.45, 2.61, 2.73, 2.75, 2.81, 2.87, 2.91, 2.96, 3.03, 3.05, 3.12]

# Вычисление ln(x)
z = [math.log(xi) for xi in x]

# Количество наблюдений
n = len(x)

# Вычисление сумм
sum_z = sum(z)
sum_y = sum(y)
sum_zy = sum(zi * yi for zi, yi in zip(z, y))
sum_z2 = sum(zi**2 for zi in z)

# Формула для β1
beta_1 = (n * sum_zy - sum_z * sum_y) / (n * sum_z2 - sum_z**2)

# Формула для β0
beta_0 = (sum_y - beta_1 * sum_z) / n

# Сумма модулей
S = abs(beta_0) + abs(beta_1)

# Вывод результатов
print(f"Оценки параметров: β0 = {beta_0:.4f}, β1 = {beta_1:.4f}")
print(f"Сумма модулей параметров: S = {S:.4f}")