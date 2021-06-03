from copy import copy
from animals.Animal import Animal
import pygame as pg


class Human(Animal):
    name = 'Human'

    def __init__(self, world, position):
        super().__init__(world, 5, 4, position)
        self.turns_to_activation = 0
        self.activated = False
        self.ability_activation = True

    def magical_potion(self):
        self.strength = 10

    def check_ability(self):
        if self.activated:
            self.strength -= 1
            self.turns_to_activation -= 1
            if self.strength == 5:
                self.activated = False
            return
        elif not self.ability_activation and self.turns_to_activation > 0:
            self.turns_to_activation -= 1
        elif not self.ability_activation and self.turns_to_activation == 0:
            self.ability_activation = True

    def activate_special_ability(self):
        if self.ability_activation and not self.activated:
            self.magical_potion()
            self.turns_to_activation = 10
            self.ability_activation = False
            self.activated = True

    def action(self):
        raise RuntimeError('Call not supported by Human class.')

    def specific_action(self, event):
        pos = copy(self.position)
        if event.key == pg.K_UP:
            pos.add(0, -1)
        elif event.key == pg.K_LEFT:
            pos.add(-1, 0)
        elif event.key == pg.K_DOWN:
            pos.add(0, 1)
        elif event.key == pg.K_RIGHT:
            pos.add(1, 0)
        if self.world.test_position(pos):
            self.position = pos
        self.check_ability()

    def clone(self):
        return self

    def get_name(self):
        return Human.name
