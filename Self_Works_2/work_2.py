# 1.Додайте до класу Character метод take_damage(amount),
# який зменшує health персонажа на amount.
# 
# 2.Якщо здоров'я падає нижче або дорівнює нулю, виводь
# повідомлення в консоль, що персонаж "непритомніє" чи "вибуває"
#
# 3.Створи кілька викликів методу take_damage для різних персонажів
#  щоб побачити, як змінюється їхній стан.
#
#
#
#

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def take_damage(self, amount):
        """ Зменшує здоров'я персонажа на amount"""
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} вибув з гри. Здоров'я < 0")
        else:
            print(f"{self.name} отримав {amount} ушкоджень."
                  + f"здоров'я тепер: {self.health}")

knight = Character("Алех", 3, 40)

damage = 30

if damage > 0:
    knight.take_damage(damage)
else:
    print("Не завдано шкоди")

if knight.health <= 0:
    print(f"{knight.name} вибув")
else:
    knight.take_damage(damage)


