import copy


# a = [1, 2, 3, [4, 5]]
# b = copy.deepcopy(a)

# print(a)  # [1, 2, 3, [4, 5]]
# print(b)  # [1, 2, 3, [4, 5]]

# a[3][0] = 6

# print(a)  # [1, 2, 3, [6, 5]]
# # [1, 2, 3, [4, 5]]    # b не змінився, тому що ми використали глибоке копіювання
# print(b)


""" 
 Iнтерфейс, який дозволяє об'єкту створювати копію самого себе. 
 Цей інтерфейс може бути реалізований за допомогою спеціального методу клонування. 
 Коли об'єкт потребує копії, він викликає цей метод замість створення нового об'єкта від початку.
"""


# Патерн Прототип часто використовується в програмуванні, коли:
# Створення екземпляру класу є більш ресурсоємним, ніж клонування.
# Потрібно уникнути прямої залежності між кодом, що створює об'єкти, та класами створюваних об'єктів.
# Системі потрібні динамічні зміни під час виконання.


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
print(id(original))  # 140310834097104
print(id(cloned))  # 140310834099728

print('_______________--other example--______________________')


class IntelCore:
    def __init__(self, value):
        self.value = value
        self.advanced_feautures_list = []

    def clone(self):
        return copy.deepcopy(self)

    def add_functionality(self, feature):
        self.advanced_feautures_list.append(feature)
        self.value = f'{self.value} + {feature}'


intel_core_i7 = IntelCore('Basic functions для i7')

intel_core_i9 = intel_core_i7.clone()

intel_core_i9.add_functionality(
    'Advanced functions, які відсутні в i7 і притаманні тільки i9')

print(intel_core_i7.value)
print(intel_core_i9.value)
