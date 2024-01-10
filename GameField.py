import pygame as pg
from settings import *


class GameField:
    def __init__(self):
        self.field = [[0 for x in range(field_size[0])] for y in range(field_size[1])]

    def update(self):
        pass

    def render(self):
        pass
