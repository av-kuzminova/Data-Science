import pandas as pd
import sweetviz as sv
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('C:/Users/Anna/Desktop/Магистратура/Эксплутационная практика/Housing.csv')

# Предварительная обработка данных
# 1. Удаление дубликатов
df.drop_duplicates(inplace=True)

# 2. Обработка пропусков:
# Заполнение пропусков медианой для числовых столбцов
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Заполнение пропусков модой для категориальных столбцов
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Шаг 1: Статистический анализ
# Рассчитаем основные статистические показатели для числовых столбцов
stat_describe = df.describe()

# Рассчитаем асимметрию и эксцесс
skewness = df.skew()
kurtosis = df.kurtosis()

# Построим гистограммы и графики плотности распределения для числовых переменных(показаны в основном отчете)

# Шаг 2: Межквартильный размах (IQR) для выявления выбросов
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))
outliers_count = outliers.sum()

# Шаг 3: Корреляционный анализ
# Рассчитаем корреляционную матрицу
corr_matrix = df.corr()

# Шаг 4: Создание автоматического отчета с использованием sweetviz
# Создаем анализ с sweetviz, который включит все визуализации и статистику
report = sv.analyze(df)

# Сохраняем отчет в файл
report.show_html('sweetviz_report.html')

# Дополнительно: Сохраняем результаты ручного анализа в текстовый файл
with open('eda_report.txt', 'w') as file:
    file.write("Статистический анализ:\n")
    file.write(str(stat_describe) + "\n")
    file.write("Асимметрия:\n")
    file.write(str(skewness) + "\n")
    file.write("Эксцесс:\n")
    file.write(str(kurtosis) + "\n")
    file.write("Количество выбросов по каждой переменной:\n")
    file.write(str(outliers_count) + "\n")
    file.write("Корреляционная матрица:\n")
    file.write(str(corr_matrix) + "\n")

