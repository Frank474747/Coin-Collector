import pygame
import sys
import random
from setup import *

pygame.init()
_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

import player, fallingObject as fo
import button

_background_img = pygame.image.load("images/background.jpg").convert()
_background_img = pygame.transform.scale(_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(pygame.font.match_font("impact"), 72)
    restart_button = button.Button(RESTART_POSI[0], RESTART_POSI[1], 
                                   RESTART_SIZE[0], RESTART_SIZE[1],
                                   GOLD, "Play Again", 25)
    start_button = button.Button(START_POSI[0], START_POSI[1],
                                 START_SIZE[0], START_SIZE[1],
                                 GOLD, "START GAME", 25)

    def __init__(self):
        self.screen = _screen
        pygame.display.set_caption("Coin collector")
        self.__background = _background_img

        self.__player = player.Player()
        self.__falling_objs: list[fo.FallingObject] = []

    def __clear_screen(self):
        self.__player.to_center()
        self.__falling_objs.clear()
        
    def __add_falling(self):
        rand = random.randint(1, 500)
        if rand == 1:
            self.__falling_objs.append(fo.LuckyBag())
        elif rand % 100 == 1:
            self.__falling_objs.append(fo.banknote())
        elif rand % 75 == 1:
            self.__falling_objs.append(fo.firecracker())
        elif rand % 20 == 1:
            self.__falling_objs.append(fo.coin())

    def __start_page(self):
        self.screen.blit(self.__background, (0, 0))
        tilte_text = Game.title_font.render("Coin Collector", True, BLACK)
        self.screen.blit(tilte_text, TITLE_POSI)
        Game.start_button.draw(self.screen)
        pygame.display.flip()

        # wait for user's command
        while True:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Game.start_button.is_hovered(event.pos):
                    return


    def __main_play(self):
        self.__clear_screen()
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
        Game.restart_button.draw(self.screen)
        pygame.display.flip()

        # wait for user's command
        while True:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Game.restart_button.is_hovered(event.pos):
                    return
                
    def run(self):
        self.__start_page()
        while(True):
            self.__main_play()