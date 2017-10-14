list = ['coke','soda','pepsi','fanta']
price = [10,25,15,20]

for x in list:
    x = input('Please choose a drink to buy:')
    if x == list[0]:
        cprice = price[0]
        print (cprice)
        a = input('Do you want to buy another drink ?')
        if a == 'Yes':
            print(x)
        elif a == 'no':
            break
    elif x == list[1]:
        sprice = price[1]
        print (sprice)
        a = input('Do you want to buy another drink ?')
        if a == 'Yes':
            print(x)
        elif a == 'no':
            break
    elif x == list[2]:
        pprice = price[2]
        print (pprice)
        a = input('Do you want to buy another drink ?')
        if a == 'Yes':
            print(x)
        elif a == 'no':
            break
    elif x == list[3]:
        fprice = price[3]
        print (fprice)
        a = input('Do you want to buy another drink ?')
        if a == 'Yes':
            print(x)
        elif a == 'no':
            break
