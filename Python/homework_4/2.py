import itertools
import operator

def infinite_number_generator(start=0, step=1):
    print("Бесконечный генератор чисел:")
    try:
        for number in itertools.count(start, step):
            print(number, end=" ")
            if number >= start + 10:  # Ограничение для примера
                print("\n(Остановлено вручную.)")
                break
    except Exception as e:
        print(f"\nОшибка: {e}")

def apply_function_to_iterator(iterable, func):
    print("\nПрименение функции к элементам:")
    try:
        result = itertools.starmap(func, zip(iterable, iterable))
        print("Результаты:", list(result))
    except Exception as e:
        print(f"Ошибка: {e}")

def combine_iterators(*iterators):
    print("\nОбъединение нескольких итераторов:")
    try:
        combined = itertools.chain(*iterators)
        print("Объединённый результат:", list(combined))
    except Exception as e:
        print(f"Ошибка: {e}")

# Основная программа
if __name__ == "__main__":
    # Создание бесконечного генератора чисел
    infinite_number_generator(start=5, step=2)
    
    # Применение функции к каждому элементу в итераторе
    numbers = [1, 2, 3, 4]
    apply_function_to_iterator(numbers, operator.add)
    
    # Объединение нескольких итераторов в один
    iterator1 = [1, 2, 3]
    iterator2 = ['a', 'b', 'c']
    iterator3 = [True, False]
    combine_iterators(iterator1, iterator2, iterator3)
