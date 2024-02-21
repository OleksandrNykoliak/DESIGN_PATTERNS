
from abc import ABC, abstractmethod

""" 
ABC є механізмом для оголошення класів у Python, які не можуть бути екземпляризовані безпосередньо. 
Це означає, що ви не можете створити об'єкт класу, який наслідується від ABC, якщо не реалізуєте всі його абстрактні методи 
у дочірньому класі.Таким чином, ABC виступає як шаблон (або контракт), який повинен бути виконаний дочірніми класами.

Декоратор abstractmethod використовується для вказівки методів у абстрактному класі, 
які мають бути обов'язково реалізовані у всіх дочірніх класах, що наслідуються від цього абстрактного класу. 
Абстрактний метод визначає лише сигнатуру методу без реалізації. Це змушує дочірні класи надавати конкретну реалізацію цих методів, 
гарантуючи, що дочірній клас відповідає інтерфейсу та логіці, заданій у базовому класі.
"""


class Transport(ABC):  # AbstractFactory
    """ 
    Клас Transport: Він визначений як абстрактний базовий клас з абстрактним методом deliver. Це означає, що будь-який клас, 
    який наслідується від Transport, мусить надати свою реалізацію методу deliver. Це забезпечує уніфікований інтерфейс для 
    всіх видів транспорту.
    """
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box."


class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a container."


class Logistics(ABC):
    """
    Клас Logistics: Також є абстрактним базовим класом із визначеним абстрактним методом create_transport. 
    Цей метод служить фабричним методом, який змушує дочірні класи (RoadLogistics і SeaLogistics) реалізувати логіку 
    створення конкретних об'єктів транспорту (Truck або Ship).
    """
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        # викликаємо фабричний метод для отримання об'єкта-продукту
        transport = self.create_transport()
        return f"Logistics: {transport.deliver()}"


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


def client_code(logistics: Logistics) -> None:
    print(logistics.plan_delivery())


if __name__ == "__main__":
    print("App: Launched with the RoadLogistics.")
    client_code(RoadLogistics())

    print("\n")

    print("App: Launched with the SeaLogistics.")
    client_code(SeaLogistics())

"""
Ці механізми забезпечують строгу структуру та контракт між базовими та дочірніми класами, спрощуючи розуміння, 
розширення та підтримку коду. Вони змушують розробників більш уважно ставитися до архітектури програми, 
дотримуючись принципів об'єктно-орієнтованого програмування.
"""
