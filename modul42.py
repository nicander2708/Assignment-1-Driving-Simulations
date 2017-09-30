def modul():

    b = []
    for a in range(0,10):#this allows the loop to be set to a maximum of 10 inputs
        a = int(input())
        x = a % 42
        b.append(x)
    print(len(set(b)))

modul()


