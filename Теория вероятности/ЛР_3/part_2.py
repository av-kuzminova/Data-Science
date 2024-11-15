import pandas as pd
import numpy as np
import scipy.stats as st

file_path = 'C:/Users/Anna/Desktop/Магистратура/Теория вероятности/ЛР_3/iris.data.txt'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(file_path, header=None, names=column_names, sep=",")
df['species'] = df['species'].astype(str)

# Случайная выборка 1/3 наблюдений
random_sample = df.sample(frac=1/3, random_state=42)

# Стратифицированная выборка (по столбцу 'species')
groups = df.groupby('species')

# Стратифицированная выборка: берем 1/3 из каждой группы, исключаем столбец 'species'
stratified_sample = groups.apply(lambda x: x.drop(columns='species').sample(frac=1/3, random_state=42))

# Среднее значение для случайной выборки (исключаем столбец 'species')
random_sample_mean = random_sample.drop(columns='species').mean()
random_sample_mean = random_sample_mean.round(4)  

# Среднее значение для стратифицированной выборки (исключаем столбец 'species')
stratified_sample_mean = stratified_sample.mean()
stratified_sample_mean = stratified_sample_mean.round(4)  

#  Функция для расчета доверительного интервала
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # Стандартное отклонение для выборки
    n = len(data)
    
    # t-критическое значение для заданного уровня доверия
    alpha = 1 - confidence
    t_critical = st.t.ppf(1 - alpha/2, df=n-1)
    
    # Доверительный интервал
    margin_of_error = t_critical * (std_dev / np.sqrt(n))
    return (float(mean - margin_of_error), float(mean + margin_of_error))

# доверительный интервал для случайной выборки (по колонке 'sepal_length')
random_sample_sepal_length = random_sample['sepal_length']
ci_random_sample = confidence_interval(random_sample_sepal_length, confidence=0.95)

# доверительный интервал для стратифицированной выборки (по колонке 'sepal_length')
stratified_sample_sepal_length = stratified_sample['sepal_length']
ci_stratified_sample = confidence_interval(stratified_sample_sepal_length, confidence=0.95)

# Среднее значение для генеральной выборки (по всем данным, исключая 'species')
df_mean = df.drop(columns='species').mean()
df_mean = df_mean.round(4)  # Округляем до 4 знаков

# средние значения и доверительные интервалы
print(f"\nСреднее значение для случайной выборки: {random_sample_mean['sepal_length']}")
print(f"Среднее значение для стратифицированной выборки: {stratified_sample_mean['sepal_length']}")

print(f"Доверительный интервал для случайной выборки (95%): {ci_random_sample}")
print(f"Доверительный интервал для стратифицированной выборки (95%): {ci_stratified_sample}")

# Вывод средних значений для всей выборки (генеральной)
print(f"\nСреднее значение для генеральной выборки: {df_mean['sepal_length']}")
