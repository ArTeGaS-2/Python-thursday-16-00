import pygame

class Entity(pygame.sprite.Sprite):
    """Клас Entity представляє основну сутність у грі"""
    def __init__(self, image_path, size):
        """Ініціалізує об'єкт Entity"""
        super().__init__() # Викликаємо конструктор батьківського класу
        # Завантаження зображення
        self.original_image = pygame.image.load(image_path).convert_alpha()
        # Зміна розміру
        self.image = pygame.transform.scale(self.original_image, size)
        # Отримуємо прямокутник зображення
        self.rect = self.image.get_rect()