import pygame
from settings import (
    WIDTH, HEIGHT, background_color,
    spawn_interval, FPS, BACKGROUND_IMAGE)
from entities.slime import Slime
from entities.game_object import GameObject

# Імпортуємо класи ворогів
from entities.vertical_enemy import VerticalEnemy
from entities.patrol_enemy import PatrolEnemy
from entities.crow_enemy import CrowEnemy

# Скрімер
from entities.screamer import Screamer

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from entities.buttons import PauseButton, ExitButton

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Їстівна планета")
        self.clock = pygame.time.Clock()
        self.background_color = pygame.Color(background_color)
        self.font = pygame.font.SysFont(None, 36)

        # Створення спрайт-груп
        self.all_sprites = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()

        # Створюємо скрімер
        self.screamer = Screamer()
        self.screamer.resize(WIDTH, HEIGHT)

        # Група ворогів
        self.enemies = pygame.sprite.Group()

        # Створення слайма
        self.slime = Slime(WIDTH // 2, HEIGHT // 2)
        self.all_sprites.add(self.slime)

        # Створюємо ворогів і додаємо їх у групи
        vertical_enemy = VerticalEnemy() # Екземпляр 
        self.all_sprites.add(vertical_enemy) 
        self.enemies.add(vertical_enemy)

        patrol_points = [
            (100, 100),
            (WIDTH - 100, 100),
            (WIDTH - 100, HEIGHT - 100),
            (100, HEIGHT - 100)]
        patrol_enemy = PatrolEnemy(patrol_points)
        self.all_sprites.add(patrol_enemy)
        self.enemies.add(patrol_enemy)

        crow_enemy = CrowEnemy(self.slime)
        self.all_sprites.add(crow_enemy)
        self.enemies.add(crow_enemy)

        self.last_spawn_time = pygame.time.get_ticks() # Час від останнього спавну
        self.collected_objects = 0 # Кількість зібраних об'єктів

        self.background_image = pygame.image.load(BACKGROUND_IMAGE)
        self.background_image = pygame.transform.scale(
            self.background_image, (1550, 780))
        
        # Стан паузи
        self.pause = False

        # Створюємо кнопки - задаємо шляхи до зображень та позицію
        self.pause_button = PauseButton(
            "OOP/assets/ingame_pause_button.png",
            (WIDTH - 120, 10), self.pause)
        self.exit_button = ExitButton(
            "OOP/assets/ingame_exit_button.png",
            (WIDTH - 60, 10))

    # Метод запуску основного ігрового циклу
    def run(self):
        running = True
        while running:
            # Малювання фону
            self.screen.blit(self.background_image, (0,0))

            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
        pygame.quit()

    # Основний обробник подій
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys)

        # Спавн об'єктів з інтервалом
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_spawn_time) >= spawn_interval * 1000:
            obj = GameObject()
            self.all_sprites.add(obj)
            self.collectibles.add(obj)
            self.last_spawn_time = current_time

        # Перевірка на зіткнення
        collided = pygame.sprite.spritecollide(
            self.slime, self.collectibles, True)
        self.collected_objects += len(collided)

        # Перевірка зіткнень з ворогами
        collided_found = False
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.slime, enemy):
                enemy.handle_collision_with_player(self.slime)
                collided_found = True

        if collided_found:
            self.screamer.activate()
        else:
            self.screamer.deactivate()


    def draw(self):
        #self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        self.display_score()
        self.screamer.draw(self.screen)

    def display_score(self):
        text = self.font.render(f'Зібрано: {self.collected_objects}',
                                True, (0,0,0))
        self.screen.blit(text, (10,10))