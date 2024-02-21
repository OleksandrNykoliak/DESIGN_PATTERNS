class Singleton:
    """ 
    Цей клас імплементує базову ідею патерна Singleton. Метод __new__ перевизначає стандартну поведінку створення об'єкта. 
    Коли ви намагаєтесь створити екземпляр Singleton, Python спочатку викликає метод __new__
    Якщо _instance є None, це означає, що екземпляр класу ще не створено. 
    Тоді він створює новий екземпляр за допомогою super(Singleton, cls).__new__(cls) і зберігає його в _instance.
    При подальших спробах створення екземпляра класу, метод __new__ просто повертає існуючий екземпляр, збережений у _instance.
    Це забезпечує, що example і example2 посилаються на один і той же об'єкт у пам'яті, 
    тому виведення їх ідентифікаторів у консоль покаже, що це один і той самий об'єкт.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


example = Singleton()
example2 = Singleton()

print(example)
print(example2)


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.name = "Example"

    def __str__(self):
        return self.name


db1 = Database()
db2 = Database()

print(db1)
print(db2)
