import pygame
from settings import slime_size, SPEED, ANIMATION_SPEED
from settings import SLIME_IMAGE_PATH, WIDTH, HEIGHT
from entities.entity import Entity
import math

class Slime(Entity):
    def __init__(self, x, y):
        super.__init__(SLIME_IMAGE_PATH, slime_size)
        self.rect.center = (x, y) # Визначаємо центр зображення
        self.direction = 0 # Кут в градусах
        self.moving = False # Перевіряє стан руху. Чи рухається персонаж
        # Поточний відносний розмір зображення
        self.current_scale_x = 1.0
        self.current_scale_y = 1.0
        # Кортеж з координатами x,y який уособлює поточне прискорення об'єкту
        self.velocity = pygame.math.Vector2(0, 0)
    
    # Обробка руху
    def move(self, keys):
        self.velocity.update(0,0) # Скидання вектору швидкості
        self.moving = False # Початково вважається, що руху немає

        # Вектор руху. Перевіряє натискання клавіш
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.y = -1 # Рух вгору
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity.y = 1 # Рух вниз
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.y = -1 # Рух ліворуч
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity.y = 1 # Рух праворуч
        # Якщо вектор швидкості не нульовий
        if self.velocity.length_squared() > 0:
            # Нормалізація та застосування швидкості
            self.velocity = self.velocity.normalize() * SPEED
            self.moving = True 
            # Визначення напрямку для обертання
            self.direction = math.degrees(math.atan2(
            -self.velocity.y, self.velocity.x)) % 360
        
        # Оновлення позиції
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Обмеження руху в межах екрану
        self.rect.clamp_ip(pygame.Rect(0,0, WIDTH, HEIGHT))
    
    def lerp(self, a, b, t):
        """ Лінійна інтерполяція між "a" та "b" з коефіцієнтом "t". """
        return a + (b - a) * t
    
    # Функція для анімації
    def animate(self):
        # Цільовий масштаб залежно від стану руху
        target_scale_x = 1.3 if self.moving else 1.0
        target_scale_y = 0.8 if self.moving else 1.0

        # Плавна зміна масштабу за допомогою інтерполяції
        self.current_scale_x = self.lerp(
            self.current_scale_x, target_scale_x, ANIMATION_SPEED)
        self.current_scale_y = self.lerp(
            self.current_scale_y, target_scale_y, ANIMATION_SPEED)
        
        # Масштабування зображення
        scaled_image = pygame.transform.scale(
            self.original_image,
            (int(slime_size * self.current_scale_x),
             int(slime_size * self.current_scale_y)))
        
        # Обертання зображення відповідно до напряму руху
        rotated_image = pygame.transform.rotate(scaled_image, self.direction)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        # Оновлення зображення та його прямокутника
        self.image = rotated_image
        self.rect = rotated_rect

    # Оновлена функція оновлення (рух і анімація)
    def update(self, keys):
        self.move(keys) # Виклик функціх обробки натискання клавіш руху
        self.animate() # Виклик функції-аніматора





