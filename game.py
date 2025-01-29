import pygame
import random
from . import player, fallingObject as fo
from setup import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Coin collector")
        self.__player = player.Player()
        self.__falling_objs = []
        
    def add_falling(self):
        rand = random.randint(1, 1000)
        if rand == 1:
            self.__falling_objs.append()
        if rand % 250 == 1:
            self.__falling_objs.append()
        if rand % 50 == 1:
            self.__falling_objs.append()