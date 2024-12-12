import pygame
from settings import slime_size, SPEED, ANIMATION_SPEED
from settings import SLIME_IMAGE_PATH, WIDTH, HEIGHT
from entities.entity import Entity
import math

class Slime(Entity):
    def __init__(self, x, y):
        super.__init__(SLIME_IMAGE_PATH, slime_size)
        self.rect.center = (x, y)
        self.direction = 0 # Кут в градусах
        self.moving = False
        self.current_scale_x = 1.0
        self.current_scale_y = 1.0

