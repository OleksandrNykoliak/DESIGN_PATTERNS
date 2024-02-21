class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}")

class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        return self.product

class ConcreteBuilder(Builder):
    def build_part_a(self):
        self.product.add("PartA")

    def build_part_b(self):
        self.product.add("PartB")

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_result()
product.list_parts()




# Компоненти патерна Builder
# Builder: Абстрактний інтерфейс для створення частин складного об'єкта.
# ConcreteBuilder: Конкретна реалізація Builder, яка конструює та збирає частини продукту, реалізуючи інтерфейс Builder. Він надає інтерфейс для отримання кінцевого продукту.
# Director: Клас, який визначає порядок виклику будівельних кроків для створення складного продукту.
# Product: Об'єкт, який має бути створений. Зазвичай, продукти, створені різними ConcreteBuilder, не мають спільного інтерфейсу.
