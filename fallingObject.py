import pygame
import random
from setup import *

__coin_img = pygame.image.load("images/coin.jpg").convert()
__coin_img.set_colorkey(WHITE)
__coin_img = pygame.transform.scale(__coin_img, COIN_SIZE)

__banknote_img = pygame.image.load("images/banknote.png").convert()
__banknote_img.set_colorkey(WHITE)
__banknote_img = pygame.transform.scale(__banknote_img, BANKNOTE_SIZE)

_lucky_bag_img = pygame.image.load("images/lucky-bag.png").convert()
_lucky_bag_img.set_colorkey(BLACK)
_lucky_bag_img = pygame.transform.scale(_lucky_bag_img, BANKNOTE_SIZE)

__firecracker_img = pygame.image.load("images/firecracker.png").convert()
__firecracker_img.set_colorkey(WHITE)
__firecracker_img = pygame.transform.scale(__firecracker_img, FIRECRACKER_SIZE)


class FallingObject:
    def __init__(self, image: pygame.Surface, speed_range: tuple[int], bounty: int):
        self._image = image
        self._rect = self._image.get_rect()
        self._rect.x = random.randint(0, SCREEN_WIDTH - self._rect.width)
        self._rect.y = -self._rect.height
        self._speed = random.randint(speed_range[0], speed_range[1])
        self._bounty = bounty

    @property
    def bounty(self):
        return self._bounty

    def fall(self):
        self._rect.y += self._speed
    
    def fall_off(self) -> bool:
        return self._rect.y > SCREEN_HEIGHT

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._rect)
    

def coin():
    return FallingObject(__coin_img, COIN_SPEED, COIN_BOUNTY)

def banknote():
    return FallingObject(__banknote_img, BANKNOTE_SPEED, BANKNOTE_BOUNTY)

def firecracker():
    return FallingObject(__firecracker_img, FIRECRACKER_SPEED, FIRECRACKER_BOUNTY)


class LuckyBag(FallingObject):
    def __init__(self):
        super().__init__(_lucky_bag_img, LUCKY_BAG_SPEED, LUCKY_BAG_BOUNTY)

    @staticmethod
    def bring_money(falling: list[FallingObject]):
        for i in range(30):
            falling.append(coin())
        for i in range(20):
            falling.append(banknote())
        for i in range(10):
            falling.append(firecracker())