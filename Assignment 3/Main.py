from Assignment_3 import Items, Enemies, Locations, Intro

Intro.play()
invent = []


def gameplay():

        loc = int(input("Level 1/2/3/4"))
        user_hp = 10
        if loc == 1:
            hp = Enemies.CaveSpider().health
            print("\n")
            print(Locations.CaveSpiderRoom())
            print(Enemies.CaveSpider())
            for x in range(0, 5):
                a = str(input('Please attack! Y')).title()
                if a == 'Y':
                    hp -= 14
                    print('Cave Spider Health= ', hp)
                    print("Cave Spider attacks")
                    user_hp -= Enemies.CaveSpider().attack
                    print('Health= ', user_hp)
                if hp <= 0:
                    print('You won, you obtained Clover x1')
                    a = Items.clover()
                    print(a)
                    invent.append('clover')
                    print(invent)
                    break
                if user_hp <= 5:
                        inp = input('Do you want to use an item ?Y/N').title()
                        print(invent)
                        if inp == 'Y':
                            print(Items.clover(),"\n",Items.toadstool(),"\n",Items.bearpaw(),"\n",Items.eyeglasses())
                            inp = input('Which Item do you want to use ? Clover ToadStool BearPaw Eye Glasses').lower()
                            if inp in invent:
                                if inp == "clover":
                                    invent.remove('clover')
                                    user_hp += 5
                                elif inp == "toadstool":
                                    invent.remove('toadstool')
                                    user_hp += 7
                                elif inp == "bearpaw":
                                    invent.remove('bearpaw')
                                    hp -= 17
                                elif inp == "eyeglasses":
                                    invent.remove('eyeglasses')
                                    hp -= 15
                            elif inp not in invent:
                                print("Item not in inventory, you lost a chance to use an item.")
                                pass
                elif user_hp <= 0:
                    print('You died')
                    break
            print("\nDo you want to play again? Y/N")
            x = input().title()
            if x == "Y":
                return gameplay()
            elif x == 'N':
                print('Thanks for playing !')

        elif loc == 2:
            hp = Enemies.GiantSerpent().health
            print(Locations.GiantSerpentRoom())
            print(Enemies.GiantSerpent())
            for x in range(0, 5):
                a = str(input('Please attack! Y')).title()
                if a == 'Y':
                    hp -= 14
                    print('Giant Serpent health = ', hp)
                    print("Giant Serpent attacks")
                    user_hp -= Enemies.GiantSerpent().attack
                    print('Health= ', user_hp)
                    if user_hp <= 5:
                        inp = input('Do you want to use an item ?Y/N').title()
                        print(invent)
                        if inp == 'Y':
                            print(Items.clover(),"\n",Items.toadstool(),"\n",Items.bearpaw(),"\n",Items.eyeglasses())
                            inp = input('Which Item do you want to use ? Clover ToadStool BearPaw Eye Glasses').lower()
                            if inp in invent:
                                if inp == "clover":
                                    invent.remove('clover')
                                    user_hp += 5
                                elif inp == "toadstool":
                                    invent.remove('toadstool')
                                    user_hp += 7
                                elif inp == "bearpaw":
                                    invent.remove('bearpaw')
                                    hp -= 17
                                elif inp == "eyeglasses":
                                    invent.remove('eyeglasses')
                                    hp -= 15
                            elif inp not in invent:
                                print("Item not in inventory, you lost a chance to use an item.")
                                pass

                if hp <= 0:
                    print('You won, you obtained ToadStool x1')
                    a = Items.toadstool()
                    print(a)
                    invent.append('toadstool')
                    print(invent)
                    break
                elif user_hp <=0:
                    print('You died')
                    break
            print("\nDo you want to play again? Y/N")
            x = input().title()
            if x == "Y":
                return gameplay()
            elif x == 'N':
                print('Thanks for playing !')

        elif loc == 3:
            print(Locations.NinjaMoleRoom())
            print(Enemies.NinjaMole())
            hp = Enemies.NinjaMole().health
            for x in range(0, 5):
                a = str(input('Please attack! Y')).title()
                if a == 'Y':
                    hp -= 14
                    print('Ninja Mole health = ', hp)
                    print("Ninja Mole attacks")
                    user_hp -= Enemies.NinjaMole().attack
                    print('Health= ', user_hp)
                    if user_hp <= 5:
                        inp = input('Do you want to use an item ?Y/N').title()
                        print(invent)
                        if inp == 'Y':
                            print(Items.clover(),"\n",Items.toadstool(),"\n",Items.bearpaw(),"\n",Items.eyeglasses())
                            inp = input('Which Item do you want to use ? Clover ToadStool BearPaw Eye Glasses').lower()
                            if inp in invent:
                                if inp == "clover":
                                    invent.remove('clover')
                                    user_hp += 5
                                elif inp == "toadstool":
                                    invent.remove('toadstool')
                                    user_hp += 7
                                elif inp == "bearpaw":
                                    invent.remove('bearpaw')
                                    hp -= 17
                                elif inp == "eyeglasses":
                                    invent.remove('eyeglasses')
                                    hp -= 15
                            elif inp not in invent:
                                print("Item not in inventory, you lost a chance to use an item.")
                                pass
                if hp <= 0:
                    print('You won, you obtained EyeGlasses x1')
                    print(Items.eyeglasses())
                    invent.append('eyeglasses')
                    print(invent)
                    break
                elif user_hp <= 0:
                    print('You died')
                    break
            print("\nDo you want to play again? Y/N")
            x = input().title()
            if x == "Y":
                return gameplay()
            elif x == 'N':
                print('Thanks for playing !')

        elif loc == 4:
            print(Locations.GrizzlyBear())
            print(Enemies.GrizzlyBear())
            hp = Enemies.GrizzlyBear().health
            for x in range(0, 5):
                a = str(input('Please attack! Y')).title()
                if a == 'Y':
                    hp -= 14
                    print('Grizzly Bear health = ', hp)
                    print("Grizzly Bear attacks")
                    user_hp -= Enemies.GrizzlyBear().attack
                    print('Health= ', user_hp)
                    if user_hp <= 5:
                        inp = input('Do you want to use an item ?Y/N').title()
                        print(invent)
                        if inp == 'Y':
                            print(Items.clover(),"\n",Items.toadstool(),"\n",Items.bearpaw(),"\n",Items.eyeglasses())
                            inp = input('Which Item do you want to use ? Clover ToadStool BearPaw Eye Glasses').lower()
                            if inp in invent:
                                if inp == "clover":
                                    invent.remove('clover')
                                    user_hp += 5
                                elif inp == "toadstool":
                                    invent.remove('toadstool')
                                    user_hp += 7
                                elif inp == "bearpaw":
                                    invent.remove('bearpaw')
                                    hp -= 17
                                elif inp == "eyeglasses":
                                    invent.remove('eyeglasses')
                                    hp -= 15
                            elif inp not in invent:
                                print("Item not in inventory, you lost a chance to use an item.")
                                pass
                if hp <= 0:
                    print('You won, you obtained Bear Paw x1')
                    print(Items.bearpaw())
                    invent.append('bearpaw')
                    print(invent)
                    break
                if user_hp <=0:
                    print('You died')
                    break

            print("\nDo you want to play again? Y/N")
            x =input().title()
            if x == "Y":
                return gameplay()
            elif x == 'N':
                print('Thanks for playing !')
gameplay()
