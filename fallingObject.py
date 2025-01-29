import pygame
import random
from abc import ABC, abstractmethod
from setup import *

__coin_img = pygame.image.load("images/coin.jpg").convert().set_colorkey(WHITE)
__coin_img = pygame.transform.scale(__coin_img, COIN_SIZE)

__banknote_img = pygame.image.load("images/banknote.png").convert().set_colorkey(WHITE)

class FallingObject(ABC):
    def __init__(self, image: pygame.Surface, speed_range: tuple[int]):
        self._image = image
        self._rect = self._image.get_rect()
        self._rect.x = random.randint(0, SCREEN_WIDTH - self._rect.width)
        self._rect.y = -self._rect.height
        self._speed = random.randint(speed_range[0], speed_range[1])

    def fall(self):
        self._rect.y += self._speed

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._rect)
    
    @abstractmethod
    def take_effect(self, fallings: list):
        pass

