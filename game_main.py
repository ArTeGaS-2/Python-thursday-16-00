import pygame
import sys
import random
from pygame.locals import *

pygame.init() # Ініціалізація бібліотеки

clock = pygame.time.Clock() # Додавання лічильника
start_ticks = pygame.time.get_ticks()

# Розміри вікна
WIDTH, HEIGHT = 800, 600 # Ширина та висота

# Налаштування дисплею
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

# Заголовок вікна
pygame.display.set_caption("Їстівна планета")

# Колір фону
background_color = (255, 255, 255) # Білий колір у RGB
background_color_2 = (72, 209, 86)

# Колір і розмір слимака
SLIME_COLOR = (0,255,0)
SLIME_COLOR_2 = (0,255,0)

SLIME_RADIUS = 20

# Початкова позиція слимака (центр екрану)
slime_x, slime_y = WIDTH // 2, HEIGHT // 2

# Завантаження спрайту слайма
slime_image = pygame.image.load('slime.png').convert_alpha()

# Масштабування спрайта до бажаного розміру
slime_size = 120
slime_image = pygame.transform.scale(slime_image,(slime_size, slime_size))

# Початковий напрямок
direction = 0 # Кут в градусах

SPEED = 5 # швидкість слимака

# Множник швидкості з ДЗ
speedMultiplier = 3

# Основний ігровий цикл
running = True
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

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]: # Вгору-вліво
        slime_x -= SPEED // 1.414 + speedMultiplier
        slime_y -= SPEED // 1.414 + speedMultiplier

    elif keys[pygame.K_w] and keys[pygame.K_d]: # Вгору-вправо
        slime_x += SPEED // 1.414 + speedMultiplier
        slime_y -= SPEED // 1.414 + speedMultiplier
    elif keys[pygame.K_s] and keys[pygame.K_a]: # Вниз-вліво
        slime_x -= SPEED // 1.414 + speedMultiplier
        slime_y += SPEED // 1.414  + speedMultiplier
    elif keys[pygame.K_s] and keys[pygame.K_d]: # Вниз-вправо
        slime_x += SPEED // 1.414 + speedMultiplier
        slime_y += SPEED // 1.414 + speedMultiplier

    elif keys[pygame.K_w]:
        slime_y -= SPEED + speedMultiplier
    elif keys[pygame.K_s]:
        slime_y += SPEED + speedMultiplier
    elif keys[pygame.K_a]:
        slime_x -= SPEED + speedMultiplier
    elif keys[pygame.K_d]:
        slime_x += SPEED + speedMultiplier

    # Отримуємо прямокутник спрайта
    slime_rect = slime_image.get_rect(center=(slime_x, slime_y))

    # Малювання спрайта на екрані
    screen.blit(slime_image, slime_rect)

    pygame.display.flip() # Оновлення дисплею

pygame.quit # Закриває вікно, коли/якщо завершується основний ігровий цикл