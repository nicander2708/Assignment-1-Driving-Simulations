class Locations:

    def __init__(self, item, monster):
        self.item = item
        self.monster = monster

    def __str__(self):
        return "Obtainable Item: {}\nMonster: {}".format(self.item, self.monster)


class CaveSpiderRoom(Locations):

    def __init__(self):
        super().__init__(item="Clover", monster="Cave Spider")


class GiantSerpentRoom(Locations):

    def __init__(self):
        super().__init__(item="Toad Stool", monster="Giant Serpent")


class NinjaMoleRoom(Locations):

    def __init__(self):
        super().__init__(item="Eye Glasses, Iron Branch", monster="Ninja Mole")


class GrizzlyBear(Locations):

    def __init__(self):
        super().__init__(item="Bearpaw", monster="Grizzly Bear")

