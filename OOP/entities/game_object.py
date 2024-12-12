# Імпортуємо змінні з налаштуваннями з файлу settings.py
from settings import OBJECT_IMAGE_PATH, OBJECT_SIZE, WIDTH, HEIGHT
# Імпортуємо з папки entities файл entity, а далі класс Entity
from entities.entity import Entity
# Бібліотека для випадкових чисел
import random

# Класс об'єкту який ми підбираємо
class GameObject(Entity):
    # Конструктор класу
    def __init__(self):
        # Наслідуємо класс Entity, передаємо йому данні налаштувань
        super().__init__(OBJECT_IMAGE_PATH, OBJECT_SIZE)

    # Визначає координати
    def spawn(self):
        x = random.randint(0, WIDTH - self.rect.width)
        y = random.randint(0, HEIGHT - self.rect.height)
        return(x, y)

