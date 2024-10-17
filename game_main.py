import pygame
import sys
import random
from pygame.locals import *

# Метод для обрахунку анімації
def Slime_Animation():
    if moving:
        animation_phase += animation_speed
        if animation_phase >= 360:
            animation_phase = 0
    
        # Розрахунок масштабу за допомогою синусоїди
        scale_x = 0.8 + 0.5 * pygame.math.sin(
            pygame.math.radians(animation_phase))
        scale_y = 1.3 - 0.5 * pygame.math.sin(
            pygame.math.radians(animation_phase))
        
        # Застосування масштабування у напрямку руху
        # Визначаємо, чи рухаємось горизонтально, чи вертикально для масштабування
        if direction == 0 or direction == 180:
            return

pygame.init() # Ініціалізація бібліотеки

animation_phase = 0 # Фаза анімації
animation_speed = 5 # Швидкість анімації

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

    # Обертання спрайта у напряму руху
    if moving:
        rotated_slime = pygame.transform.rotate(
            slime_image,
            -direction)
    # Без обертання, якщо не рухається
    else:
        rotated_slime = slime_image

    # Отримуємо прямокутник спрайта
    slime_rect = rotated_slime.get_rect(
        center=(slime_x, slime_y))

    # Малювання спрайта на екрані
    screen.blit(rotated_slime, slime_rect)

    pygame.display.flip() # Оновлення дисплею

pygame.quit # Закриває вікно, коли/якщо завершується основний ігровий цикл