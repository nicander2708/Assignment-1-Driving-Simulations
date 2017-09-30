def modul():

    b = int()
    for a in range(0,10):#this allows the loop to be set to a maximum of 10 inputs
        a = int(input())
        y = a%42
        if y != 0:
            b += 1
        else:
            b += 0
            if b == 0:
                b += 1

    print(b)

modul()


