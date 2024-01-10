import pygame as pg


class Core:
    def __init__(self):
        pass

    def main_loop(self):
        pg.init()

        sc = pg.display.set_mode((500, 500))
        pg.display.set_caption('LsSnake')

        run = True
        while run:
            sc.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    break
            pg.display.update()
        pg.quit()
