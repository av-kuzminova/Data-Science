import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm, skew, kurtosis

# Загрузка данных
df = pd.read_excel('C:/Users/Anna/Desktop/Магистратура/Теория вероятности/ЛР_2/tab4_zpl_2023.xlsx', sheet_name='Средняя ЗП по РФ (непрерыв)')

# Предварительный просмотр данных
print(df.head())
print(df.columns)

# Извлечение данных по зарплатам и обработка пропусков
salary_data = df['20231)']
salary_data = salary_data.dropna()

# Вычисление статистических характеристик
mean_salary = salary_data.mean()
variance_salary = salary_data.var()
std_dev_salary = np.sqrt(variance_salary)          # Стандартное отклонение
skewness_salary = skew(salary_data)
kurtosis_salary = kurtosis(salary_data)

quantile_05 = salary_data.quantile(0.05)
quantile_95 = salary_data.quantile(0.95)
quantile_025 = salary_data.quantile(0.025)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(salary_data, bins=20, color='skyblue', edgecolor='black', density=True)

# Добавление линии нормального распределения
x = np.linspace(salary_data.min(), salary_data.max(), 100)
normal_pdf = norm.pdf(x, mean_salary, std_dev_salary)
plt.plot(x, normal_pdf, color='red', linestyle='-', linewidth=2, label='Нормальное распределение')

# Настройки диаграммы
plt.title('Распределение средних зарплат по субъектам РФ')
plt.xlabel('Средняя зарплата (руб.)')
plt.ylabel('Плотность вероятности')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Сохранение и отображение диаграммы
histogram_path = 'C:/Users/Anna/Desktop/Магистратура/Теория вероятности/ЛР_2/histogram_with_normal_curve.png'
plt.savefig(histogram_path)
plt.show()

# Формирование таблицы результатов
results = {
    'Показатель': [
        'Математическое ожидание',
        'Дисперсия',
        'Асимметрия',
        'Эксцесс',
        'Квантиль 0.05',
        'Квантиль 0.95',
        '2.5%-я точка'
    ],
    'Значение': [
        f"{mean_salary:.4f}",
        f"{variance_salary:.4f}",
        f"{skewness_salary:.4f}",
        f"{kurtosis_salary:.4f}",
        f"{quantile_05:.4f}",
        f"{quantile_95:.4f}",
        f"{quantile_025:.4f}"
    ]
}

results_df = pd.DataFrame(results)
print(results_df)
