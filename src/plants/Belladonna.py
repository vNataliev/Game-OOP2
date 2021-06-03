from plants.Plant import Plant


class Belladonna(Plant):
    name = 'Belladonna'

    def __init__(self, world, position):
        super().__init__(world, 99, position)

    def collision(self, attacker):
        self.world.info_box.report_kill(self, attacker)
        self.world.remove_organism(attacker)
        self.world.remove_organism(self)

    def clone(self):
        return Belladonna(self.world, self.position)

    def get_name(self):
        return Belladonna.name
