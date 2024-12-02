from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    print("Текущая дата и время:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_date_difference(date1, date2):

    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        difference = abs(d2 - d1)
        print(f"Разница между {date1} и {date2}: {difference.days} дней.")
    except ValueError as e:
        print(f"Ошибка преобразования даты: {e}")

def convert_string_to_datetime(date_string, format_string="%Y-%m-%d %H:%M:%S"):

    try:
        date_object = datetime.strptime(date_string, format_string)
        print(f"Строка '{date_string}' преобразована в объект: {date_object}.")
        return date_object
    except ValueError as e:
        print(f"Ошибка преобразования строки: {e}")

# Основная программа
if __name__ == "__main__":
    # Отображение текущей даты и времени
    display_current_datetime()
    
    #Вычисление разницы между двумя датами
    date1 = "2023-12-01"
    date2 = "2024-01-01"
    calculate_date_difference(date1, date2)
    
    # Преобразование строки в объект даты и времени
    date_string = "2024-12-01 15:30:00"
    convert_string_to_datetime(date_string)
