from Organism import Organism
from animals import *
from plants import *
from utils import *
from copy import copy
import functools


class World:

    def __init__(self, dim: Dimension):
        self.turn_counter = 0
        self.dims = dim
        self.organisms = []
        self.info_box = InfoBox()
        self.human = None

    def fill_world(self):
        self.human = Human(self, Position(10, 10))
        self.add_organism(self.human)
        self.add_organism(Fox(self, Position(7, 3)))
        self.add_organism(Fox(self, Position(12, 15)))
        self.add_organism(Wolf(self, Position(4, 9)))
        self.add_organism(Wolf(self, Position(16, 18)))
        self.add_organism(Guarana(self, Position(10, 12)))
        self.add_organism(Guarana(self, Position(14, 5)))
        self.add_organism(Antelope(self, Position(2, 1)))
        self.add_organism(Antelope(self, Position(12, 9)))
        self.add_organism(Sheep(self, Position(14, 0)))
        self.add_organism(Sheep(self, Position(9, 10)))
        self.add_organism(Sheep(self, Position(6, 14)))
        self.add_organism(CyberSheep(self, Position(3, 13)))
        self.add_organism(Turtle(self, Position(11, 6)))
        self.add_organism(Turtle(self, Position(1, 6)))
        self.add_organism(Grass(self, Position(18, 2)))
        self.add_organism(Grass(self, Position(1, 17)))
        self.add_organism(Grass(self, Position(19, 16)))
        self.add_organism(Belladonna(self, Position(6, 6)))
        self.add_organism(Belladonna(self, Position(0, 12)))
        self.add_organism(Belladonna(self, Position(9, 18)))
        self.add_organism(Sosnowsky(self, Position(11, 1)))
        self.add_organism(Sosnowsky(self, Position(3, 18)))
        self.add_organism(SowThistle(self, Position(17, 13)))
        self.add_organism(SowThistle(self, Position(17, 7)))
        self.add_organism(SowThistle(self, Position(7, 18)))

    def get_initiative(self, i):
        return self.organisms[i].initiative

    def get_max_count(self):
        return self.dims.x * self.dims.y

    def add_organism(self, organism):
        if len(self.organisms) == self.get_max_count():
            raise IndexError("Too many organisms.")
        self.organisms.append(organism)

    def remove_organism(self, organism):
        i = 0
        while i < len(self.organisms):
            if organism is self.organisms[i]:
                if organism is self.human:
                    self.human = None
                self.organisms.remove(organism)
            i += 1

    def is_position_free(self, position):
        for org in self.organisms:
            if org.position == position:
                return False
        return True

    def get_organism(self, position):
        for i in range(len(self.organisms)):
            if self.organisms[i].position == position:
                return self.organisms[i]
        return None

    def get_defender(self, organism):
        p = organism.position
        for i in range(len(self.organisms)):
            if self.organisms[i] is not organism and self.organisms[i].position == p:
                return self.organisms[i]
        return None

    def get_sosnowskys(self) -> []:
        sosnowskys = []
        for o in self.organisms:
            if isinstance(o, Sosnowsky):
                sosnowskys.append(o)
        return sosnowskys

    def index_of(self, organism):
        for i in range(len(self.organisms)):
            if self.organisms[i] is organism:
                return i
        return -1

    def test_position(self, p):
        if 0 <= p.x < self.dims.x and 0 <= p.y < self.dims.y:
            return True
        else:
            return False

    def make_turn(self, event):
        self.turn_counter += 1

        self.organisms.sort(key=functools.cmp_to_key(Organism.compare), reverse=True)
        for org in self.organisms:
            org.age += 1
        i = 0
        while i < len(self.organisms):
            o = self.organisms[i]
            if o.age > 0:
                if o is self.human:
                    self.human.specific_action(event)
                else:
                    o.action()
                def_o = self.get_defender(o)
                if def_o is not None:
                    def_o.collision(o)
            i += 1
