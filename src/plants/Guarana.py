from plants.Plant import Plant


class Guarana(Plant):
    name = 'Guarana'

    def __init__(self, world, position):
        super().__init__(world, 0, position)

    def collision(self, attacker):
        attacker.increase_strength(3)
        self.world.info_box.report_guarana(attacker)
        self.world.remove_organism(self)

    def clone(self):
        return Guarana(self.world, self.position)

    def get_name(self):
        return Guarana.name
