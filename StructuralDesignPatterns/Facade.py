""" 
Патерн "Фасад" (Facade) є структурним дизайн патерном, який надає простий інтерфейс до складної системи. 
Цей патерн приховує складність системи, надаючи простий доступ до її функціональності. 
Він дозволяє високорівневій абстракції спілкуватися з підсистемами без необхідності розбиратися в деталях їх реалізації.
"""


class PhotoConventerFacade:
    """ 
    У цьому прикладі PhotoConverterFacade виступає як фасад для системи обробки зображень, 
    яка включає конвертацію, стиснення та застосування фільтрів до фотографій. 
    Використання фасаду спрощує роботу з системою, надаючи єдиний метод convert_image,
    що об'єднує всі етапи обробки зображення:
    """

    def __init__(self):
        # конвертує зображення в інший формат.
        self.converter = ImageConverter()
        self.compressor = ImageCompressor()  # стискає зображення
        self.filter = ImageFilter()  # застосовує фільтр до зображення

    def convert_image(self, filename, format):
        photo = self.converter.convert(filename)
        photo = self.compressor.compress(photo)
        photo = self.filter.apply_filter(photo)
        print("Converted and saved successfully")
        return photo


converter = PhotoConventerFacade()
photo = converter.convert_image("example.jpg", "png")

# Second Example


class Facade:
    """
    Цей приклад ілюструє використання фасада для спрощення взаємодії з кількома підсистемами. 
    Клас Facade надає метод operation, який агрегує виклики методів трьох підсистем:
    """

    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()
        self.subsystem3 = Subsystem3()

    def operation(self):
        self.subsystem1.operation1()  # виконує операцію першої підсистеми.
        self.subsystem2.operation1()  # виконує операцію другої підсистеми.
        self.subsystem3.operation1()  # виконує операцію третьої підсистеми.


class Subsystem1:
    def operation1(self):
        print("Subsystem1 operation1")

    def operation2(self):
        print("Subsystem1 operation2")


class Subsystem2:
    def operation1(self):
        print("Subsystem2 operation1")

    def operation2(self):
        print("Subsystem2 operation2")


class Subsystem3:
    def operation1(self):
        print("Subsystem3 operation1")

    def operation2(self):
        print("Subsystem3 operation2")


facade = Facade()
facade.operation()


"""
Спрощення інтерфейсу: Фасад надає простий інтерфейс до складної системи, що спрощує її використання.
Зменшення залежностей: Клієнтський код взаємодіє лише з фасадом, зменшуючи залежності від підсистем.
Гнучкість та легкість модифікації: Модифікувати внутрішню реалізацію системи легше, не впливаючи на клієнтський код, 
оскільки всі зміни залишаються за фасадом.
"""

