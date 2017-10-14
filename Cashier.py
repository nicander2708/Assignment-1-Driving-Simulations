class cashier():
    def __init__(self, itemname, price):
        self.itemname = itemname.title()
        self.price    = int(price)

    def purchase(self):
        itemlist = 'The price of '+ self.itemname + ' is '+ str(self.price)
        x = input('How much do you want to pay ?')
        if x >= str(self.price):
            a = (int(x)-int(self.price))
            print ('This will be your return: '+ str(a))
        return itemlist

items = cashier('coke',25)
print(items.purchase())
