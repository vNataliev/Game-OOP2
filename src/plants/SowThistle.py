from plants.Plant import Plant


class SowThistle(Plant):
    name = 'Sow thistle'

    def __init__(self, world, position):
        super().__init__(world, 0, position)

    def collision(self, attacker):
        super().collision(attacker)

    def action(self):
        for i in range(3):
            super().action()

    def clone(self):
        return SowThistle(self.world, self.position)

    def get_name(self):
        return SowThistle.name
