class Summator:
    def __init__(self):
        pass

    def calculate_sum(self, numbers):
        if not all(isinstance(i, (int, float)) for i in numbers):
            raise ValueError("Все элементы списка должны быть числами")
        return sum(numbers)
