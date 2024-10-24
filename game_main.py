import pygame
import sys
import random
from pygame.locals import *


# Налаштування
WIDTH, HEIGHT = 800, 600 # Ширина та висота
background_color = (255, 255, 255) # Білий колір у RGB
background_color_2 = (72, 209, 86)
slime_size = 120 # Масштабування спрайта до бажаного розміру
SPEED = 5 # швидкість слимака
ANIMATION_SPEED = 0.1

def init_game():
    pygame.init() # Ініціалізація бібліотеки
    # Налаштування дисплею
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    # Заголовок вікна
    pygame.display.set_caption("Їстівна планета")
    return screen

def load_slime_image():
    # Завантаження спрайту слайма
    slime_image = pygame.image.load('slime.png').convert_alpha()
    return pygame.transform.scale(slime_image,(slime_size, slime_size))

def slime_movement(keys, slime_x, slime_y, SPEED, current_direction):
    # Визначення на прямку руху
    moving = False
    dx, dy = 0, 0

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 225 # Вгору-вліво
        moving = True
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = -SPEED // 1.414
        direction = 315 # Вгору-вправо
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        dx = -SPEED // 1.414
        dy = SPEED // 1.414
        direction = 135 # Вниз-вліво
        moving = True
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        dx = SPEED // 1.414
        dy = SPEED // 1.414
        direction = 45 # Вниз-вправо
        moving = True

    elif keys[pygame.K_w]:
        dy = -SPEED
        direction = 270 # Вгору
        moving = True
    elif keys[pygame.K_s]:
        dy = SPEED
        direction = 90 # Вниз
        moving = True
    elif keys[pygame.K_a]:
        dx = -SPEED
        direction = 180 # Вліво
        moving = True
    elif keys[pygame.K_d]:
        dx = SPEED
        direction = 0 # Вправо
        moving = True

    # Оновлення позиції слайма
    slime_x += dx
    slime_y += dy
    return slime_x, slime_y, direction, moving

def lerp(a, b, t):
    """Лінійна інтерполяція між a та b з коефіціентом t."""
    return a + (b - a) * t

def animate_slime(moving, direction, slime_image, slime_x,slime_y,
                  current_scale_x, current_scale_y):
    
# Ініціалізація гри
screen = init_game()
slime_image = load_slime_image()
clock = pygame.time.Clock() # Додавання лічильника
start_ticks = pygame.time.get_ticks()
# Початкова позиція слимака (центр екрану)
slime_x, slime_y = WIDTH // 2, HEIGHT // 2
running = True

# Ініціалізація поочних масштабів та напрямку
current_scale_x = 1.0
current_scale_y = 1.0
direction = 0 # Кут в градусах

# Основний ігровий цикл
while running:
    screen.fill(background_color_2) # Заповньюємо екран обраним кольором
    clock.tick(60) # Обмежуємо кількість кадрів на секунду у вікні

    # Обчислення секунд
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    # Виведення часу на екран
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f'Time: {seconds}', True, (0,0,0))
    screen.blit(timer_text,( 10, 10))

    # Основний обробник подій у грі
    for event in pygame.event.get(): # Перебираємо події у грі
        if event.type == pygame.QUIT: # Якщо подій - вихід / закриття вікна
            running = False # Завершення ігрового циклу (while running)

    # Отримання стану клавіш
    keys = pygame.key.get_pressed()
    slime_x, slime_y, direction, moving = slime_movement(
        keys, slime_x, slime_y, SPEED, direction)

    # Малювання спрайта на екрані
    screen.blit(rotated_slime, slime_rect)

    pygame.display.flip() # Оновлення дисплею

pygame.quit # Закриває вікно, коли/якщо завершується основний ігровий цикл