class Enemy:

    def __init__(self,name, attack ,health):
        self.name = name
        self.attack = attack
        self.health = health

    def __str__(self):
        return "\nName: {}\nAttack: {}\nHealth: {}".format(self.name, self.attack, self.health)


class CaveSpider(Enemy):

    def __init__(self):
        super().__init__(name="CaveSpider", attack =3,health=42)

class GiantSerpent(Enemy):

    def __init__(self):
        super().__init__(name="GiantSerpent", attack =2,health= 50)

class NinjaMole(Enemy):

    def __init__(self):
        super().__init__(name="NinjaMole", attack =2, health= 60)
    
class GrizzlyBear(Enemy):

    def __init__(self):
        super().__init__(name="GrizzlyBear", attack=3, health= 70)
