
class Order:
    def __init__(self)->None:
        self.items={}

    def add_item(self,itm):
        if itm in self.items:
            self.items[itm] += itm.quantity
        else:
            self.items[itm] = itm.quantity
    
    def find_item(self,name):
        for itm in self.items:
            if itm.name.lower() == name.lower():
                return itm
        return None 
    
    def remove_item(self,itm):
        if itm in self.items:
            print(f"{itm.name} removed from cart")
            del self.items[itm]
        else:
            print(f"{itm.name} not found in cart")
    
    @property
    def total_price(self):
        return sum(itm.price * quantity for itm,quantity in self.items.items())
    
    def clear(self):
        self.items={}
        
