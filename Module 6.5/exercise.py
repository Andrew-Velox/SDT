class Product:
    def __init__(self,name,price,quantity)->None:
        self.name=name
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        return (f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})")



class Shop:
    products = []
    def add_poduct(self,product):
        self.products.append(product)

    def buy_product(self,product,quantity):
        for x in range(0,len(self.products)):
            if product == self.products[x].name:
                if quantity<= self.products[x].quantity:
                    self.products[x].quantity-=quantity
                    return f"Congrass! now the current quantity is {self.products[x].quantity}"
                else:
                    return f"Sorry our Quantity is: {self.products[x].quantity}"

        return f"{product} is not in Shop"


shop1 = Shop()
shop1.add_poduct(Product("Watch",100000,43))
shop1.add_poduct(Product("Book",4400,32))
shop1.add_poduct(Product("Car",412000,3))
shop1.add_poduct(Product("Phone",500000,10))

# print(shop1.products)

print(shop1.buy_product("Watch",3))
print(shop1.buy_product("Watcfh",100))