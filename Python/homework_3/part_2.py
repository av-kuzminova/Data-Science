import re
from collections import Counter

def count_unique_words(text):
    """
    Подсчитывает количество уникальных слов в строке, игнорируя знаки препинания и пробелы.
    
    :param text: str - Входная строка.
    :return: int - Количество уникальных слов.
    """
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Разбиваем строку на слова
    words = cleaned_text.split()
    
    # Используем Counter для подсчёта уникальных слов
    word_counts = Counter(words)
    
    # Возвращаем количество уникальных слов
    return len(word_counts)

# Пример использования
example_text = "Привет, мир! Привет всем, кто любит кодить."
unique_count = count_unique_words(example_text)

print(f"Количество уникальных слов: {unique_count}")
