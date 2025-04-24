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
            
class Enemy:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self, target):
        """Завдає шкоди об'єкту Character (target)."""
        damage = self.level * 1.5
        print(f"{self.name} атакує {target.name} і завдає {damage} шкоди!")
        target.take_damage(damage)

# Створюємо персонажа і ворога
hero = Character("Hero", 3, 50)
enemy_1 = Enemy("Grblin", 2, 30)

# Імітація "раундів" бою в циклі while
round_counter = 0
while hero.health > 0 and enemy_1.health > 0:
    round_counter += 1
    print(f"\n--- Раунд {round_counter} ---")
    enemy_1.attack(hero)
    if hero.health <=0:
        break
    print(f"{hero.name} завдає удару у відповідь!")
    enemy_1.health -= 10
    print(f"{enemy_1.name} втрачає 10 здоров'я, тепер: {enemy_1.health}")
print("\nБій завершено.")