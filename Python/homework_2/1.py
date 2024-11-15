def read_numbers_from_file(filename='data.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()  # Убираем лишние пробелы и переносы строк
            if line:  # Проверяем, что строка не пустая
                try:
                    # преобразую строку в число
                    number = float(line)  # float охватывает и целые, и вещественные числа
                    print(line)  # Если преобразование успешно, выводим строку
                except ValueError:
                    raise TypeError(f"Строка '{line}' содержит не числовое значение.")
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except TypeError as e:
        print(e)

# вызов функции
read_numbers_from_file()
