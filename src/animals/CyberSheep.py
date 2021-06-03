from animals.Animal import Animal
from copy import copy


class CyberSheep(Animal):
    name = 'Cyber Sheep'

    def __init__(self, world, position):

        super().__init__(world, 11, 4, position)

    def action(self):
        sosonowskys = self.world.get_sosnowskys()
        if len(sosonowskys) == 0:
            super().action()
        else:
            sosonowskys.sort(key=lambda sss: self.distance_to(sss))
            sosnowsky = sosonowskys[0]
            pos = copy(sosnowsky.position)
            pos.sub_pos(self.position)
            pos.cut()
            self.prev_position = copy(self.position)
            self.position.add_pos(pos)

    def clone(self):
        return CyberSheep(self.world, self.position)

    def get_name(self):
        return CyberSheep.name
