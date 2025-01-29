import pygame
import sys
import random
from setup import *

pygame.init()
_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

import player, fallingObject as fo

_background_img = pygame.image.load("images/background.jpg").convert()
_background_img = pygame.transform.scale(_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    def __init__(self):
        self.screen = _screen
        pygame.display.set_caption("Coin collector")
        self.__background = _background_img

        self.__player = player.Player()
        self.__falling_objs: list[fo.FallingObject] = []
        
    def __add_falling(self):
        rand = random.randint(1, 500)
        if rand == 1:
            self.__falling_objs.append(fo.LuckyBag())
        elif rand % 100 == 1:
            self.__falling_objs.append(fo.banknote())
        elif rand % 75 == 1:
            self.__falling_objs.append(fo.firecracker())
        elif rand % 25 == 1:
            self.__falling_objs.append(fo.coin())

    def main_play(self):
        money = 0
        start_ticks = pygame.time.get_ticks()

        while True:
            # draw background
            self.screen.blit(self.__background, (0, 0))
            keys = pygame.key.get_pressed()

            # handle events
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # move and draw player
            self.__player.move(keys)
            self.__player.draw(self.screen)

            # add new falling objects
            self.__add_falling()

            # update and draw falling objects
            for obj in self.__falling_objs:
                obj.fall()
                obj.draw(self.screen)

                # collect caught objects
                if self.__player.catch_object(obj):
                    if isinstance(obj, fo.LuckyBag):
                        fo.LuckyBag.bring_money(self.__falling_objs)
                    money += obj.bounty
                    self.__falling_objs.remove(obj)

                # remove objects which fall off the screen
                elif obj.fall_off():
                    self.__falling_objs.remove(obj)

            # display money and timer
            money_text = Game.font.render(f"money: {money}", True, BLACK)
            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            time_text = Game.font.render(f"time left: {GAME_DURATION - elapsed_seconds}", True, BLACK)
            self.screen.blit(money_text, MONEY_POSI)
            self.screen.blit(time_text, TIME_POSI)

            # check if time is up
            if elapsed_seconds > GAME_DURATION:
                break

            # update display
            pygame.display.flip()

            # cap the frame rate
            Game.clock.tick(FPS)

        # show final results
        self.screen.blit(_background_img, (0, 0))
        result_text = Game.font.render(f"Time's up! You earn {money} dollars!", True, BLACK)

        self.screen.blit(result_text, RESULT_POSI)
        pygame.display.flip()

        # wait for user's command
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()