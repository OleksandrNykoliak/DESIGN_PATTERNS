# Builder: Абстрактний інтерфейс для створення частин складного об'єкта.
# ConcreteBuilder: Конкретна реалізація Builder, яка конструює та збирає частини продукту, реалізуючи інтерфейс Builder.
# Director: Клас, який визначає порядок виклику будівельних кроків для створення складного продукту.
# Product: Об'єкт, який має бути створений. Зазвичай, продукти, створені різними ConcreteBuilder, не мають спільного інтерфейсу.


class Product:  # House
    # ми визначаємо загальний клас продукту
    # якщо ми будуємо наприклад різні будинки то загальний клас це будинок

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(
            f"У нас тепер є будинок з наступними елементами: {', '.join(self.parts)}")


class Builder:  # HouseBuilder з різними частинами
    # тут ми маємо визначити що ми будуємо якісь частини будинку
    # наприклад будинок з гаражем, з підвалом, з басейном або зі садом
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_result(self):
        return self.product


class ConcreteBuilder(Builder):
    # тут ми конкретизуємо які частини будинку ми будуємо і будуємо їх
    def build_part_a(self):
        self.product.add("Гараж")  # гараж

    def build_part_b(self):
        self.product.add("Підвал")  # підвал

    def build_part_c(self):
        self.product.add("Комен")  # комен


class Director:  # HouseDirector
    # в кінцевому результаті виконує будівництво будинку
    # викликом усіх частини будинку
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()


builder = ConcreteBuilder()  # ми маємо конкретно побудувати підвал та гараж

# наш клас приймає на підряд будівництво гаражу і підвалу в конкретному будинку
director = Director(builder)

director.construct()  # ми починаємо будувати гараж та підвал

product = builder.get_result()  # ми отримуємо результат будівництва

product.list_parts()  # виводимо результат будівництва
