class Characters:

    def __init__(self,name, weapon,attack,health=10):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.attack = attack

    def __str__(self):
        return "Character: {}\nWeapon: {}\nAttack: {}\nHealth: {}".format(self.name, self.weapon, self.attack, self.health)


class Player(Characters):

    def __init__(self):
        super().__init__(name=input("Enter your name: "), weapon="Sword", attack=14,health=10)
