# 1.Створіть клас Character, який матиме такі атрибути
# - name(текстовий тип)
# - level(цілий тип)
# - health(дробовий тип)

# 2. Створіть конструктор __init__, що прийматиме значення цих
# атрибутів

# 3. Створіть 3-5 об'єктів класу Character з різними початковими
# даними та додайте їх до списку characters.

# 4.Виведіть інформацію про кожного персонажа в консоль
# Інструменти: списки, цикл for, базові типи даних

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

knight = Character("Вася", 3, 50) # Лицар
bowman = Character("Орландо Блум", 2, 25) # Лучник
mage = Character("Андрій", 4, 20) # Маг

charactersList = [knight, bowman, mage] # Список персонажів

for char in charactersList:
    print(f"Name: {char.name}, Level: {char.level}, Health: {char.health}")