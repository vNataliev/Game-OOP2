from animals.Animal import Animal


class Sheep(Animal):
    name = 'Sheep'

    def __init__(self, world, position):
        super().__init__(world, 4, 4, position)

    def collision(self, attacker):
        super().collision(attacker)

    def action(self):
        super().action()

    def clone(self):
        return Sheep(self.world, self.position)

    def get_name(self):
        return Sheep.name

