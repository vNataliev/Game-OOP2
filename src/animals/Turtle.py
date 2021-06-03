from animals.Animal import Animal
import random


class Turtle(Animal):
    name = 'Turtle'

    def __init__(self, world, position):

        super().__init__(world, 2, 1, position)

    def collision(self, attacker):
        if attacker.strength < 5:
            self.world.info_box.report_turtle(attacker)
            attacker.go_back()
        else:
            super().collision(attacker)

    def action(self):
        r = random.randint(0, 3)
        if r == 0:
            super().action()

    def clone(self):
        return Turtle(self.world, self.position)

    def get_name(self):
        return Turtle.name
