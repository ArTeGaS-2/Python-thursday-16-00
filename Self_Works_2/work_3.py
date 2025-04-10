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