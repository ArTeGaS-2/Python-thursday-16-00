import pygame
from settings import (
    WIDTH, HEIGHT, background_color,
    spawn_interval, FPS)
from entities.slime import Slime
from entities.game_object import GameObject

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

        # Створення слайма
        self.slime = Slime(WIDTH // 2, HEIGHT // 2)
        self.all_sprites.add(self.slime)