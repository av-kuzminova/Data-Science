import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных
data = pd.read_excel('C:/Users/Anna/Desktop/Магистратура/Теория вероятности/ЛР_3/Бедность и безработица 2023 г.xlsx', sheet_name='all')
x = data['бедность']
y = data['безработица']

# Расчет коэффициента корреляции
correlation = np.corrcoef(x, y)[0, 1]
print(f"Коэффициент корреляции: {correlation:.2f}")

# Оценка меры связи
if abs(correlation) > 0.7:
    strength = "сильная"
elif abs(correlation) > 0.3:
    strength = "умеренная"
else:
    strength = "слабая"
print(f"Мера связи: {strength}")

# Линейная аппроксимация: нахождение коэффициентов наклона и смещения
slope, intercept = np.polyfit(x, y, 1)
y_pred = slope * x + intercept

# Расчет коэффициента достоверности R^2
ss_res = np.sum((y - y_pred) ** 2)         # Сумма квадратов остатков
ss_tot = np.sum((y - np.mean(y)) ** 2)      # Общая сумма квадратов
r2 = 1 - (ss_res / ss_tot)                  # Коэффициент R^2
print(f"Коэффициент достоверности R^2: {r2:.2f}")

# Построение графика
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label=f'Linear Fit (R^2={r2:.2f})')
plt.xlabel('бедность')
plt.ylabel('безработица')
plt.legend()
plt.title(f'Correlation: {correlation:.2f} (Мера связи: {strength})')
plt.show()
