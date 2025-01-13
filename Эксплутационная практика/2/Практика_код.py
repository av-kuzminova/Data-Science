import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as sv

# Загрузка датасета
file_path = 'C:/Users/Anna/Desktop/Магистратура/Эксплутационная практика/2/Housing (2).csv'  # Укажите путь к вашему файлу
data = pd.read_csv(file_path)

# Этап 1: Предварительное изучение данных
print("Первые 5 строк датасета:")
print(data.head())

print("\nИнформация о датасете:")
print(data.info())

print("\nРазмеры датасета:")
print(f"Строк: {data.shape[0]}, Столбцов: {data.shape[1]}")

print("\nТипы данных:")
print(data.dtypes)

print("\nКоличество пропусков в каждом столбце:")
print(data.isnull().sum())

print("\nКоличество дубликатов:")
print(data.duplicated().sum())

# Удаление дубликатов
data = data.drop_duplicates()
print("\nДубликаты удалены.")

# Обработка пропусков (пример замены на медиану для числовых данных)
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    if data[column].isnull().sum() > 0:
        data[column] = data[column].fillna(data[column].median())
        print(f"Пропуски в столбце {column} заполнены медианой.")

# Этап 2: Изучение статистических характеристик
print("\nОсновные статистические показатели:")
print(data.describe())

# Анализ распределений
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    plt.hist(data[column], bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f"Гистограмма для {column}")
    plt.xlabel(column)
    plt.ylabel("Частота")
    plt.show()
    
    sns.kdeplot(data[column], color='red')
    plt.title(f"Плотность распределения для {column}")
    plt.xlabel(column)
    plt.ylabel("Плотность")
    plt.show()

# Выявление выбросов
print("\nВыявление выбросов:")
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"Столбец {column}: количество выбросов = {len(outliers)}")
    
    # Удаление выбросов (опционально)
    # data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Анализ асимметрии и эксцесса
print("\nАнализ асимметрии и эксцесса:")
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    print(f"{column}: Асимметрия = {data[column].skew()}, Эксцесс = {data[column].kurtosis()}")

# Этап 3: Изучение взаимосвязей между переменными

# 1. Построение корреляционной матрицы и визуализация её с помощью тепловой карты
print("\nКорреляционная матрица:")
corr_matrix = data.corr()

# Визуализация корреляционной матрицы
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
plt.title('Корреляционная матрица')
plt.show()

# Определение переменных с наибольшей корреляцией с целевой переменной 'price'
target_column = 'price'
correlated_with_target = corr_matrix[target_column].sort_values(ascending=False)
print(f"\nПеременные с наибольшей корреляцией с {target_column}:")
print(correlated_with_target)

# 2. Анализ зависимости между стоимостью жилья и ключевыми характеристиками
key_columns = ['area', 'bedrooms', 'bathrooms']  # Площадь, количество комнат, количество ванных

for column in key_columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[column], y=data[target_column])
    plt.title(f"Зависимость {target_column} от {column}")
    plt.xlabel(column)
    plt.ylabel(target_column)
    plt.show()

# 3. Анализ категориальных переменных с использованием boxplot
categorical_columns = ['stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                       'airconditioning', 'parking', 'prefarea', 'furnishingstatus']

for column in categorical_columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[column], y=data[target_column])
    plt.title(f"Влияние {column} на {target_column}")
    plt.xlabel(column)
    plt.ylabel(target_column)
    plt.show()

# 4. Построение парных графиков (pairplot) для исследования зависимостей между несколькими переменными
# Для парных графиков выбираем несколько переменных, включая числовые и категориальные
selected_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories']  # Пример переменных
sns.pairplot(data[selected_columns], hue='stories', plot_kws={'alpha': 0.5})
plt.suptitle("Парные графики для выбранных переменных", y=1.02)
plt.show()

# Этап 4.1: Создание отчёта Sweetviz
report = sv.analyze(data)  # Автоматический анализ данных

# Сохранение отчёта в HTML файл
report.show_html("sweetviz_report.html")  # Сохраняем отчет в HTML формате

# В Jupyter Notebook можно сразу визуализировать отчёт
report.show_notebook()