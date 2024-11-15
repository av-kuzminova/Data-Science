class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} издает звук: {self.sound}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "мяу")
        self.color = color

    def makesound(self):
        print(f"Кошка {self.name} ({self.color}) говорит: {self.sound}")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "гав")
        self.color = color

    def makesound(self):
        print(f"Собака {self.name} ({self.color}) говорит: {self.sound}")

# Создание объектов Cat и Dog
cat = Cat("Мурка", "серый")
dog = Dog("Бобик", "коричневый")

# Вызов метода makesound для каждого объекта
cat.makesound()  # Кошка Мурка (серый) говорит: мяу
dog.makesound()  # Собака Бобик (коричневый) говорит: гав
