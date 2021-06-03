from abc import abstractmethod
import random
from math import sqrt, pow

from utils import Position
from copy import copy


class Organism:

    def __init__(self, world, strength, initiative, position: Position):
        self.world = world
        self.strength = strength
        self.initiative = initiative
        self.position = copy(position)
        self.prev_position = copy(position)
        self.age = 0

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def collision(self, attacker):
        if attacker.strength >= self.strength:
            self.world.info_box.report_kill(attacker, self)
            self.world.remove_organism(self)
        else:
            self.world.info_box.report_kill(self, attacker)
            self.world.remove_organism(attacker)

    def get_position_around(self, r):
        offsets = [[r, r], [r, 0], [0, r], [-r, 0], [0, -r], [-r, -r], [-r, r], [r, -r]]
        while True:
            pos = copy(self.position)
            x = random.randint(0, 7)
            pos.add(*offsets[x])
            if self.world.test_position(pos):
                return pos

    def get_free_position_around(self):
        new_pos_counter = 0
        while True:
            new_position = self.get_position_around(1)
            new_pos_counter += 1
            if self.world.is_position_free(new_position):
                return new_position
            if new_pos_counter == 100:
                raise IndexError("No free positions.")

    def increase_strength(self, strength_to_add):
        self.strength += strength_to_add

    def set_position(self, new_position):
        self.prev_position = self.position
        self.position = new_position

    def distance_to(self, o):
        return sqrt(pow(self.position.x - o.position.x, 2) + pow(self.position.y - o.position.y, 2))

    @staticmethod
    def compare(o1, o2):
        if o1.initiative == o2.initiative:
            return 1 if o1.age > o2.age else -1
        return 1 if o1.initiative > o2.initiative else -1
