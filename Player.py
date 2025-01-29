import pygame
from fallingObject import FallingObject
from setup import *

__piggy_img = pygame.image.load("images/piggy.png").convert()
__piggy_img.set_colorkey(WHITE)
__piggy_img = pygame.transform.scale(__piggy_img, PIGGY_SIZE)


class Player:
    def __init__(self, image: pygame.Surface=__piggy_img, speed: int=10):
        self.__image = image
        self.__rect = self.__image.get_rect()
        self.__rect.x = SCREEN_WIDTH // 2 - self.__rect.width // 2  # at middle
        self.__rect.y = SCREEN_HEIGHT - self.__rect.height - 5  # at bottom
        self.__speed = speed

    def move(self, keys: pygame.key.ScancodeWrapper):
        if keys[pygame.K_LEFT] and self.__rect.x > 0:
            self.__rect.x -= self.__speed
        elif keys[pygame.K_RIGHT] and self.__rect.x < SCREEN_WIDTH - self.__rect.width:
            self.__rect.x += self.__speed

    def draw(self, screen: pygame.Surface):
        screen.blit(self.__image, self.__rect)

    def catch_object(self, obj: FallingObject) -> bool:
        return self.__rect.colliderect(obj._rect)

