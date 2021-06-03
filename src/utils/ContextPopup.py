from utils import Icons
import pygame as pg
from animals import *
from plants import *


class ContextPopup:

    def __init__(self, icons: Icons, pos):
        self.icons = [
            (icons[Antelope.name], Antelope),
            (icons[CyberSheep.name], CyberSheep),
            (icons[Fox.name], Fox),
            (icons[Sheep.name], Sheep),
            (icons[Turtle.name], Turtle),
            (icons[Wolf.name], Wolf),
            (icons[Belladonna.name], Belladonna),
            (icons[Grass.name], Grass),
            (icons[Guarana.name], Guarana),
            (icons[Sosnowsky.name], Sosnowsky),
            (icons[SowThistle.name], SowThistle)
        ]
        from game import Game
        height = Game.icon_size
        width = 11 * Game.icon_size
        self.bounds = (pos[0], pos[1], width, height)
        self.field_size = Game.icon_size

        self.is_active = False
        self.pos = pos

        self.on_click_listener = None

    def activate(self):
        self.is_active = True

    def blit(self, screen):
        for i, (icon, constructor) in enumerate(self.icons):
            screen.blit(icon, (self.bounds[0] + i * self.field_size, self.bounds[1]))

    def handle_event(self) -> bool:
        pos = list(pg.mouse.get_pos())
        if self.bounds[0] < pos[0] < self.bounds[0] + self.bounds[2] and self.bounds[1] < pos[1] < self.bounds[1] + self.bounds[3]:
            index = (pos[0] - self.bounds[0]) // self.field_size
            _, constructor = self.icons[index]
            self.on_click_listener(constructor)
            self.is_active = False

