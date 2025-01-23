import pygame
from entities.entity import Entity

class Enemy(Entity):
    """
    Базовий класс (абстрактний) для всіх ворогів і загроз.
    Наслідує від Entity, щоб мати доступ до зображень,
    rect тощо.
    """
    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def update(self, *args):
        """
        Метод оновлення ворогів. У базовому класі - порожній.
        У нащадків - своя логіка.
        """
        pass
    def handle_collision_with_player(self, player):
        """
        Обробка зіткнення з гравцем. У базовому классі - порожня.
        У нащадків можна перевизначити.
        """
        pass
    