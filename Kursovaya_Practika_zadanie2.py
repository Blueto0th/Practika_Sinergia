# Кейс 2
# базовый и производный классы (Собака и Кошка)

# родительский класс
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "издает какой-то звук"

    def move(self):
        return "двигается"

    def info(self):
        return "Имя: " + self.name + ", Возраст: " + str(self.age) + " лет"


# дочерний класс Собака
class Dog(Animal):
    def __init__(self, name, age, poroda):
        Animal.__init__(self, name, age)
        self.poroda = poroda

    def sound(self):
        return "Гав-гав!"

    def move(self):
        return "бегает на четырех лапах"

    def fetch(self):
        return self.name + " приносит палку!"

    def gav(self):
        return self.name + " громко лает!"


# дочерний класс Кошка
class Cat(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, age)
        self.color = color  # окрас шерсти

    def sound(self):
        return "Мяу-мяу!"

    def move(self):
        return "крадется бесшумно"

    def purr(self):
        return self.name + " мурлычет: мрррр..."

    def hunt(self):
        return self.name + " ловит мышь!"


# проверка работы
print("=== ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ ===")

print("\n--- Базовый класс Animal ---")
a = Animal("Зверь", 5)
print(a.info())
print("Звук:", a.sound())
print("Движение:", a.move())

print("\n--- Производный класс Dog ---")
dog = Dog("Барбос", 3, "Овчарка")
print(dog.info())
print("Порода:", dog.poroda)
print("Звук:", dog.sound())
print("Движение:", dog.move())
print(dog.fetch())
print(dog.gav())

print("\n--- Производный класс Cat ---")
cat = Cat("Мурка", 2, "серая")
print(cat.info())
print("Окрас:", cat.color)
print("Звук:", cat.sound())
print("Движение:", cat.move())
print(cat.purr())
print(cat.hunt())

print("\n=== ПОЛИМОРФИЗМ ===")
print("Все животные по-разному реагируют на одни и те же команды:")
print("------------------------------")

zoo = [dog, cat]  # список объектов
for x in zoo:
    print(x.info())
    print("  Звук:", x.sound())
    print("  Движение:", x.move())
    print("------------------------------")

print("Программа завершена!")