class DataBuffer:
    def __init__(self):
        self.buffer = []  # Инициализация пустого буфера
    
    def add_data(self, data):
        """Добавляет данные в буфер. При переполнении очищает буфер и выводит сообщение."""
        self.buffer.append(data)  # Добавляем новые данные в буфер
        if len(self.buffer) >= 5:  # Проверка на переполнение (больше или равно 5 элементов)
            print("Буфер переполнен. Очистка буфера:", self.buffer)
            self.buffer.clear()  # Очистка буфера
    
    def get_data(self):
        """Возвращает данные из буфера. Выводит сообщение, если буфер пуст."""
        if not self.buffer:  # Проверка, пуст ли буфер
            print("Буфер пуст, данных нет.")
            return None
        data = self.buffer.copy()  # Создаем копию данных из буфера
        self.buffer.clear()  # Очищаем буфер после передачи данных
        return data

# Пример использования класса
buffer = DataBuffer()

# Добавляем данные
buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)  # Здесь буфер должен переполниться и очиститься

# Пробуем получить данные из пустого буфера
print(buffer.get_data())  # Ожидаем сообщение об отсутствии данных

# Добавляем данные снова
buffer.add_data(6)
buffer.add_data(7)

# Получаем данные из буфера
print(buffer.get_data())  # Должны получить [6, 7]
