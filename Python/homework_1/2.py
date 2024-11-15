import datetime

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError("Недостаточно товара на складе!")
        self.quantity -= amount

    def calculate_cost(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name} (кол-во: {self.quantity}, цена: {self.price})"


class Warehouse:
    def __init__(self):
        self.products = []
        self.log = []

    def add_product(self, product):
        self.products.append(product)
        self.log.append(f"{datetime.datetime.now()} - Добавлен товар: {product}")

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]
        self.log.append(f"{datetime.datetime.now()} - Удалён товар: {product_name}")

    def calculate_total_value(self):
        return sum(product.calculate_cost() for product in self.products)

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        raise ValueError("Товар не найден на складе.")

    def display_log(self):
        print("История операций на складе:")
        for entry in self.log:
            print(entry)


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []
        self.total_revenue = 0

    def sell_product(self, warehouse, product_name, quantity):
        try:
            product = warehouse.find_product(product_name)
            product.decrease_quantity(quantity)
            sale_amount = quantity * product.price
            self.sales_report.append({
                "product": product_name,
                "quantity": quantity,
                "revenue": sale_amount
            })
            self.total_revenue += sale_amount
            warehouse.log.append(f"{datetime.datetime.now()} - Продавец {self.name} продал {quantity} ед. товара {product_name} на сумму {sale_amount}.")
        except ValueError as e:
            print(f"Ошибка при продаже: {e}")

    def display_sales_report(self):
        print(f"Отчёт о продажах продавца {self.name}:")
        for sale in self.sales_report:
            print(f"Товар: {sale['product']}, Количество: {sale['quantity']}, Выручка: {sale['revenue']}")
        print(f"Общая выручка: {self.total_revenue}")


# Пример использования
warehouse = Warehouse()

# Добавляем товары на склад
product1 = Product("Ноутбук", 10, 50000)
product2 = Product("Телефон", 20, 20000)
warehouse.add_product(product1)
warehouse.add_product(product2)

# Создаем продавца
seller = Seller("Иван")

# Продаем товары
seller.sell_product(warehouse, "Ноутбук", 2)
seller.sell_product(warehouse, "Телефон", 5)

# Удаляем товар со склада
warehouse.remove_product("Телефон")

# Отображаем отчёты
seller.display_sales_report()
warehouse.display_log()

# Общая стоимость товаров на складе
print("Общая стоимость товаров на складе:", warehouse.calculate_total_value())
