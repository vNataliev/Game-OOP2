from copy import copy

from animals import CyberSheep, Animal
from plants.Plant import Plant


class Sosnowsky(Plant):
    name = "Sosnowsky's hogweed"

    def __init__(self, world, position):
        super().__init__(world, 10, position)

    def collision(self, attacker):
        self.world.remove_organism(self)
        if not isinstance(attacker, CyberSheep):
            self.world.info_box.report_sosnowsky(attacker)
            self.world.remove_organism(attacker)
        if isinstance(attacker, CyberSheep):
            self.world.info_box.report_cyber(attacker)

    def action(self):
        self.kill_all_neighbour(self.position)

    def clone(self):
        return Sosnowsky(self.world, self.position)

    def get_name(self):
        return Sosnowsky.name

    def kill_all_neighbour(self, position):
        offsets = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        for i in range(8):
            new_position = copy(position)
            new_position.add(*offsets[i])
            o = self.world.get_organism(new_position)
            if o is not None and isinstance(o, Animal):
                if not isinstance(o, CyberSheep):
                    self.world.info_box.report_sosnowsky_neighbour(o)
                    self.world.remove_organism(o)
