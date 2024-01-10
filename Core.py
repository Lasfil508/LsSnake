import pygame as pg
from settings import *
from GameField import GameField
from MenuManager import MenuManager


class Core:
    def __init__(self):
        self.game_field = GameField()
        self.oMM = MenuManager()

        self.sc = pg.display.set_mode(win_size)
        self.clock = pg.time.Clock()

        self.run = True

        pg.display.set_caption('LsSnake')

    def input(self):
        if self.get_mm().game_state == 'Game':
            self.player_input()

    def player_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
            elif event.type == pg.KEYDOWN:
                pass

    def main_loop(self):
        pg.init()

        while self.run:
            self.sc.fill((0, 0, 0))
            self.input()
            self.get_mm().update(self)
            self.get_mm().render(self)

            pg.display.flip()
            self.clock.tick(fps)

        pg.quit()

    def get_mm(self):
        return self.oMM

    def get_gf(self):
        return self.game_field
