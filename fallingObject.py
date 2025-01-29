import pygame
import random
from setup import *

class FallingObject:
    def __init__(self, image: pygame.Surface, speed_range: tuple[int]):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(speed_range[0], speed_range[1])

    def fall(self):
        self.rect.y += self.speed

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        