import copy

""" 
 Iнтерфейс, який дозволяє об'єкту створювати копію самого себе. 
 Цей інтерфейс може бути реалізований за допомогою спеціального методу клонування. 
 Коли об'єкт потребує копії, він викликає цей метод замість створення нового об'єкта від початку.
"""


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


original = Prototype(42)

cloned = original.clone()

print(original.value)
print(cloned.value)
print(original is cloned)

# Патерн Прототип часто використовується в програмуванні, коли:

# Створення екземпляру класу є більш ресурсоємним, ніж клонування.
# Потрібно уникнути прямої залежності між кодом, що створює об'єкти, та класами створюваних об'єктів.
# Системі потрібні динамічні зміни під час виконання.


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.model} {self.color}"


car1 = Car("Ford", "red")
car2 = car1.clone()

print(car1)
print(car2)
