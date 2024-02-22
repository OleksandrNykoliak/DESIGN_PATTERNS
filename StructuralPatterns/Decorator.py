""" 
Дизайн патерн, який дозволяє динамічно додавати нові функції до об'єктів, обертаючи їх 
у корисні "обгортки". Він надає гнучкий альтернативний спосіб розширення функціональності 
об'єктів порівняно з наслідуванням, мінімізуючи кількість змін в існуючому коді.

Декоратор має базовий інтерфейс, який є спільним для як декорованих об'єктів, так і для декораторів. 
Декоратори містять посилання на об'єкт інтерфейсу, який вони "обгортають", і 
виконують свої додаткові функції разом з делегуванням викликів до обгорнутого об'єкта.
"""


# Сценарії використання:
# Коли потрібно додати обов'язки до окремих об'єктів динамічно та прозоро, без впливу на інші об'єкти.
# Коли розширення за допомогою наслідування є непрактичним або неможливим через велику кількість комбінованих функцій або через обмеження в компіляційному часі.


class Component:
    # Component: Оголошує інтерфейс для об'єктів, до яких можна динамічно додавати обов'язки.
    def operation(self):
        pass


class ConcreteComponent(Component):
    # ConcreteComponent: Визначає об'єкт, до якого додаються нові обов'язки.
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    # Decorator: Тримає посилання на об'єкт Component і визначає інтерфейс, який відповідає інтерфейсу Component
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    # ConcreteDecorator: Додає обов'язки до Component.
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    # ConcreteDecorator: Додає обов'язки до Component.
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


# Використання
simple = ConcreteComponent()
print(simple.operation())

decorator1 = ConcreteDecoratorA(simple)
print(decorator1.operation())

decorator2 = ConcreteDecoratorB(decorator1)
print(decorator2.operation())


""" Ще один приклад """


class Coffee:
    # Coffee: Інтерфейс (або абстрактний клас) для напоїв, які можна придбати в кав'ярні.
    def cost(self):
        pass

    def description(self):
        pass


class SimpleCoffee(Coffee):
    # SimpleCoffee: Конкретний напій, який реалізує Coffee.
    def cost(self):
        return 10

    def description(self):
        return "Simple coffee"


class CoffeeDecorator(Coffee):
    # CoffeeDecorator: Абстрактний декоратор, який також імплементує інтерфейс Coffee і містить посилання на декорований об'єкт Coffee
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()


class MilkDecorator(CoffeeDecorator):
    # MilkDecorator: Конкретні декоратори, які додають відповідні інгредієнти та змінюють вартість напою.
    def cost(self):
        return self.coffee.cost() + 2

    def description(self):
        return self.coffee.description() + ", milk"


class SugarDecorator(CoffeeDecorator):
    # SugarDecorator Конкретний декоратори, які додають відповідні інгредієнти та змінюють вартість напою.
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", sugar"


class WhipDecorator(CoffeeDecorator):
    # WhipDecorator Конкретний декоратори, які додають відповідні інгредієнти та змінюють вартість напою.
    def cost(self):
        return self.coffee.cost() + 3

    def description(self):
        return self.coffee.description() + ", whip"


# Створення простої кави
coffee = SimpleCoffee()
print(f"Cost: {coffee.cost()}; Description: {coffee.description()}")

# Додавання молока
milk_coffee = MilkDecorator(coffee)
print(f"Cost: {milk_coffee.cost()}; Description: {milk_coffee.description()}")

# Додавання цукру до кави з молоком
sugar_milk_coffee = SugarDecorator(milk_coffee)
print(
    f"Cost: {sugar_milk_coffee.cost()}; Description: {sugar_milk_coffee.description()}")

# Додавання вершків до кави з молоком і цукром
whip_sugar_milk_coffee = WhipDecorator(sugar_milk_coffee)
print(f"Cost: {whip_sugar_milk_coffee.cost()}; Description: {whip_sugar_milk_coffee.description()}")
