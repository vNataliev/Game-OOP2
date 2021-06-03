class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def add_pos(self, pos):
        self.x += pos.x
        self.y += pos.y

    def sub_pos(self, pos):
        self.x -= pos.x
        self.y -= pos.y

    def cut(self):
        if self.x > 0:
            self.x = 1
        if self.x < 0:
            self.x = -1
        if self.y > 0:
            self.y = 1
        if self.y < 0:
            self.y = -1

    def as_tuple(self):
        return self.x, self.y

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Position):
            return self.x == o.x and self.y == o.y
        return False
