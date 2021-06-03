class InfoBox:
    report_size = 30

    def __init__(self):
        self.report = []

    def report_kill(self, o1, o2):
        self.report.insert(0, '{} has killed {} on [{}, {}]'.format(
            o1.name, o2.name, o2.position.x, o2.position.y
        ))
        self.check_size()

    def report_guarana(self, o1):
        self.report.insert(0, 'Guarana has been eaten by {} and rise his strength by 3 on [{}, {}]'.format(
            o1.name, o1.position.x, o1.position.y
        ))
        self.check_size()

    def report_turtle(self, o1):
        self.report.insert(0, 'Turtle pushed back {} on [{}, {}]'.format(
            o1.name, o1.position.x, o1.position.y
        ))
        self.check_size()

    def report_sosnowsky(self, o1):
        self.report.insert(0, "Sosnowsky's hogweed has killed {} and himself on [{}, {}]".format(
            o1.name, o1.position.x, o1.position.y
        ))
        self.check_size()

    def report_cyber(self, o1):
        self.report.insert(0, "Cyber-Sheep has killed Sosnowsky's Hogweed on [{}, {}]".format(
            o1.position.x, o1.position.y
        ))
        self.check_size()

    def report_sosnowsky_neighbour(self, o1):
        self.report.insert(0, "Sosnowsky's hogweed has killed {} like all neighbours on [{}, {}]".format(
                o1.name, o1.position.x, o1.position.y
            ))
        self.check_size()

    def report_spawn(self, o1):
        self.report.insert(0, '{} has spawn on [{}, {}]'.format(
                o1.name, o1.position.x, o1.position.y
                ))
        self.check_size()

    def check_size(self):
        while len(self.report) > InfoBox.report_size:
            self.report.pop(-1)
