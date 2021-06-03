from abc import abstractmethod
from src.Organism import Organism
import random


class Plant(Organism):

    def __init__(self, world, strength, position):
        super().__init__(world, strength, 0, position)

    def action(self):
        r = random.randint(0, 100)
        try:
            if r < 3:
                new_position = self.get_free_position_around()
                new_o = self.clone()
                new_o.set_position(new_position)
                self.world.info_box.report_spawn(new_o)
                self.world.add_organism(new_o)
        except IndexError:
            pass

    def collision(self, attacker):
        super().collision(attacker)

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
