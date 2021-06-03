from animals.Animal import Animal


class Wolf(Animal):
    name = 'Wolf'

    def __init__(self, world, position):
        super().__init__(world, 9, 5, position)

    def collision(self, attacker):
        super().collision(attacker)

    def action(self):
        super().action()

    def clone(self):
        return Wolf(self.world, self.position)

    def get_name(self):
        return Wolf.name
