class Monsters:

    def __init__(self,name, speciality):
        self.name = name
        self.weapon = weapon
        self.speciality = speciality

    def __str__(self):
        return "{} {} {}".format(self.name, self.weapon, self.speciality)


class Swordsman(Characters):

    def __init__(self):
        super().__init__(name="Swordsman", weapon="Sword", speciality="Attack")


class Hunter(Characters):

    def __init__(self):
        super().__init__(name="Hunter", weapon="Bow", speciality="Accuracy")


class Explorer(Characters):

    def __init__(self):
        super().__init__(name="Explorer",weapon="Sword",speciality="Attack")


class Herbalist(Characters):

    def __init__(self):
        super().__init__(name="Herbalist", weapon="Staff", speciality="Health")

