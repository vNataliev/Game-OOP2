from animals.Animal import Animal
import random


class Antelope(Animal):
    name = 'Antelope'

    def __init__(self, world, position):

        super().__init__(world, 4, 4, position)

    def collision(self, attacker):
        r = random.randint(0, 1)
        if r:
            try:
                new_position = self.get_free_position_around()
                self.position = new_position
            except IndexError:
                super().collision(attacker)
        else:
            super().collision(attacker)

    def action(self):
        self.move(2)

    def clone(self):
        return Antelope(self.world, self.position)

    def get_name(self):
        return Antelope.name
