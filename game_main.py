import pygame

pygame.init()

clock = pygame.time.Clock() # Додаємо лічильник

# Розміри вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Їстівна планета")

background_color = (255,255,255)
background_color_2 = (82,157,206)

SLIME_COLOR = (0, 255, 0)
SLIME_RADIUS = 20

# Почакова позиція слимака (центр екрану)
slime_x, slime_y = WIDTH // 2, HEIGHT // 2
SPEED = 5

running = True
# Основний ігровий цикл
while running:
    clock.tick(60) # Обмеження частоти кадрів у грі
    
    # Заповнення фону обраним коліром
    screen.fill(background_color_2)

    # Обробник подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Малює коло
    pygame.draw.circle(
        screen, SLIME_COLOR,
        (slime_x, slime_y), SLIME_RADIUS)

    # Оновлення дисплею
    pygame.display.flip()
# Вихід з вікна
pygame.quit()