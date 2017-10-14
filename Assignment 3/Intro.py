from Assignment_3 import Characters
def play():
        char = str(input("Welcome traveler, are you ready to embark on your adventure?Y/N").title())
        if char == 'Y':
            print(Characters.Player())
        elif char == 'N':
            quit()
        else:
            raise TypeError
