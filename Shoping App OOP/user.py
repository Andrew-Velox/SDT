
class User:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    


class Seller(User):
    def __init__(self,email,password):
        super().__init__(email,password)
        
    def add_product(self, shop, itm):
        shop.product.add_product(itm)
    
    def show_products(self,shop):
        shop.product.show_products()

    




class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
    
    
    def view_products(self, shop):
        shop.product.show_products()
    
    def place_order(self,shop,product_name,quantity):
        get_product = shop.product.find_product(product_name)

        if get_product and get_product.quantity >= quantity:
            get_product.quantity -= quantity
            print(f"Order placed for {quantity} {get_product.name}(s).")
        else:
            print(f"Product not available or insufficient quantity for {product_name}.")

    



# Dokan = Shop("Dokan")
# seller_1 = Seller("Alice","1111")
# seller_2 = Seller("Bob","2222")


# customer_1 = Customer("Charlie","3333")
# customer_2 = Customer("David","4444")

# Owner_1 = Owner("Andrew","1111")
# Owner_1.add_seller(Dokan, seller_1)
# Owner_1.add_seller(Dokan, seller_2)
# Owner_1.add_customer(Dokan, customer_1)
# Owner_1.add_customer(Dokan, customer_2)

# Owner_1.view_sellers(Dokan)
# Owner_1.view_customers(Dokan)

# prod_1 = ProductItem("Apple", 50, 100)
# prod_2 = ProductItem("Banana", 30, 200)
# prod_3 = ProductItem("Orange", 40, 150)

# Andrew = Seller("Andrew", "1111")
# Andrew.add_product(Dokan, prod_1)
# Andrew.add_product(Dokan, prod_2)

# Andrew.show_products(Dokan)
# Dokan.add_seller(Andrew)
# print(Dokan.login_seller("Andrew", "1111"))

