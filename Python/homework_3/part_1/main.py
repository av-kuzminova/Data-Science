from math_tools import Summator

# Создаем объект класса Summator
summator = Summator()

# Передаем список чисел в метод для вычисления суммы
numbers = [1, 2, 3, 4, 5]
result = summator.calculate_sum(numbers)

# Выводим результат
print("Сумма чисел в списке:", result)
