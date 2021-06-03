from plants.Plant import Plant


class Grass(Plant):
    name = 'Grass'

    def __init__(self, world, position):
        super().__init__(world, 0, position)

    def clone(self):
        return Grass(self.world, self.position)

    def get_name(self):
        return Grass.name
