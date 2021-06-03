from copy import copy

from Organism import Organism
from abc import abstractmethod


class Animal(Organism):

    def __init__(self, world, strength, initiative, position):

        super().__init__(world, strength, initiative, position)

    def action(self):
        self.move(1)

    def collision(self, attacker):
        if type(self) == type(attacker):
            attacker.go_back()
            try:
                new_position = self.get_free_position_around()
                new_animal = self.clone()
                new_animal.set_position(new_position)
                self.world.info_box.report_spawn(new_animal)
                self.world.add_organism(new_animal)
            except IndexError:
                pass
        else:
            super().collision(attacker)

    def move(self, r):
        self.prev_position = self.position
        self.position = self.get_position_around(r)

    def go_back(self):
        self.position = self.prev_position

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
