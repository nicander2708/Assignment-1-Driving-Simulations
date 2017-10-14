class Items:

    def __init__(self,name,ability):
        self.name = name
        self.ability = ability

    def __str__(self):
        return "Item: {}\nAbility: {}".format(self.name, self.ability)

class clover(Items):

    def __init__(self):
        super().__init__(name ='clover',ability ='add 5 health')

class toadstool(Items):

    def __init__(self):
        super().__init__(name ="toadstool",ability ='add 7 health')

class eyeglasses(Items):

    def __init__(self):
        super().__init__(name ="eyeglasses",ability ="increase attack by 1")

class bearpaw(Items):

    def __init__(self):
        super().__init__(name ='bearpaw', ability ='Increase attack by 3')


