from menu import Menu

class Food_itm(Menu):
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    