import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis


df = pd.read_excel('C:/Users/Anna/Desktop/Магистратура/Теория вероятности/ЛР_2/tab4_zpl_2023.xlsx', sheet_name='курящие люди по возрастам. норм')


print(df.head())  
print(df.columns) 


salary_data = df['Да']
salary_data = salary_data.dropna()


mean_salary = salary_data.mean()                   # Математическое ожидание
variance_salary = salary_data.var()                # Дисперсия
skewness_salary = skew(salary_data)                # Асимметрия
kurtosis_salary = kurtosis(salary_data)            # Эксцесс


quantile_05 = salary_data.quantile(0.05)
quantile_95 = salary_data.quantile(0.95)
quantile_025 = salary_data.quantile(0.025)


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


