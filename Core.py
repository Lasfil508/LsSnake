import pygame as pg
from settings import *


class Core:
    def __init__(self):
        self.sc = pg.display.set_mode(win_size)
        pg.display.set_caption('LsSnake')

    def update(self):
        pass

    def main_loop(self):
        pg.init()

        run = True
        while run:
            self.sc.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            pg.display.update()
        pg.quit()
