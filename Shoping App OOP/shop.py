from user import User, Seller, Customer
from products import Product

class Shop: # like restaurant
    def __init__(self, name):
        self.name = name
        self.customers=[]
        self.sellers=[]
        self.product = Product()
        
    

    
    
    def add_seller(self, seller):
        self.sellers.append(seller)
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def find_seller(self, email):
        for seller in self.sellers:
            if seller.email.upper() == email.upper():
                return seller
        return None
    def find_customer(self, email):
        for customer in self.customers:
            if customer.email.upper() == email.upper():
                return customer
        return None

    def login_seller(self,email, password):
        return self.find_seller(email) is not None and self.find_seller(email).password == password

    def login_customer(self,email, password):
        return self.find_customer(email) is not None and self.find_customer(email).password == password

