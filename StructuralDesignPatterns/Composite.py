# "Композит" (Composite) — це структурний дизайн патерн, який дозволяє складати об'єкти в
# деревоподібні структури для представлення ієрархій "частково-ціле". Використовуючи патерн Композит,
# клієнти можуть однаково обробляти як окремі об'єкти, так і складові групи об'єктів.

# Основна ідея:
# Основна ідея полягає в тому, що як "Лист" (Leaf), так і "Композит" (Composite)
# класи реалізують один і той самий інтерфейс. Це дозволяє обробляти окремі об'єкти та їх комбінації єдиним чином.
# "Лист" є простим об'єктом, що не має підоб'єктів, тоді як "Композит" може містити інші об'єкти "Лист"
# або "Композит" всередині себе, формуючи деревоподібну структуру.


class FileSystemComponent:
    # FileSystemComponent відповідає за Component роль, визначаючи загальний інтерфейс.
    def display(self):
        pass


class File(FileSystemComponent):
    # File є Leaf, представляючи листові елементи без дочірніх.
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")


class Directory(FileSystemComponent):
    # Directory виконує роль Composite, управляючи колекцією дочірніх елементів (як листові, так і інші композитні об'єкти).
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Створення файлів
file1 = File("File1")
file2 = File("File2")

# Створення директорії
directory = Directory("Directory")

# Додавання файлів до директорії
directory.add(file1)
directory.add(file2)

# Відображення структури
directory.display()
