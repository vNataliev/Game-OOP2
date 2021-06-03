from animals.Animal import Animal


class Fox(Animal):
    name = 'Fox'

    def __init__(self, world, position):

        super().__init__(world, 3, 7, position)

    def action(self):
        new_pos_counter = 0
        while True:
            new_position = self.get_position_around(1)
            new_pos_counter += 1
            def_o = self.world.get_defender(self)
            if def_o is None or self.strength >= def_o.strength:
                self.prev_position = self.position
                self.position = new_position
                return
            if new_pos_counter == 100:
                return

    def clone(self):
        return Fox(self.world, self.position)

    def get_name(self):
        return Fox.name
