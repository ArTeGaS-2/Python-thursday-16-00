import pygame

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

SPEED = 5 # швидкість слимака

# Основний ігровий цикл
running = True
while running:
    screen.fill(background_color_2) # Заповньюємо екран обраним кольором

    # Обчислення секунд
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    # Виведення часу на екран
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f'Time: {seconds}', True, (0,0,0))
    screen.blit(timer_text,( 10, 10))

    clock.tick(60) # Обмежуємо кількість кадрів на секунду у вікні
    
    # Основний обробник подій у грі
    for event in pygame.event.get(): # Перебираємо події у грі
        if event.type == pygame.QUIT: # Якщо подій - вихід / закриття вікна
            running = False # Завершення ігрового циклу (while running)

    # Отримання стану клавіш
    keys = pygame.key.get_pressed()

    # Рух на WASD у восьми напрямках
    if keys[pygame.K_w] and keys[pygame.K_a]: # Вгору-вліво
        slime_x -= SPEED // 1.414
        slime_y -= SPEED // 1.414

    elif keys[pygame.K_w] and keys[pygame.K_d]: # Вгору-вправо
        slime_x += SPEED // 1.414
        slime_y -= SPEED // 1.414 
    elif keys[pygame.K_s] and keys[pygame.K_a]: # Вниз-вліво
        slime_x -= SPEED // 1.414
        slime_y += SPEED // 1.414 
    elif keys[pygame.K_s] and keys[pygame.K_d]: # Вниз-вправо
        slime_x += SPEED // 1.414
        slime_y += SPEED // 1.414

    elif keys[pygame.K_w]:
        slime_y -= SPEED
    elif keys[pygame.K_s]:
        slime_y += SPEED
    elif keys[pygame.K_a]:
        slime_x -= SPEED
    elif keys[pygame.K_d]:
        slime_x += SPEED

    pygame.draw.circle(screen, SLIME_COLOR,(slime_x, slime_y), SLIME_RADIUS)

    pygame.display.flip() # Оновлення дисплею

pygame.quit # Закриває вікно, коли/якщо завершується основний ігровий цикл