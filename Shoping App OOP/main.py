from user import Seller, Customer
from products import Product
from productitem import ProductItem
from shop import Shop

Dokan = Shop("Dokan")

def seller_section(seller):
    while 1:
        print("--------- Seller Menu ---------")
        # print(f"--------Welcome {seller.email}---------------")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Back")

        opt = int(input("Please Select an Option: "))

        if opt == 1:
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product_item = ProductItem(name, price, quantity)
            seller.add_product(Dokan, product_item)
        elif opt == 2:
            seller.show_products(Dokan)
        elif opt == 3:
            break
        else:
            print("Wrong Option")


def customer_section(customer):
    while 1:
        print("--------- Customer Menu ---------")
        # print(f"--------Welcome {customer.email}---------------")
        print("1. View Products")
        print("2. Place Order")
        print("3. Back")

        opt = int(input("Please Select an Option: "))

        if opt == 1:
            customer.view_products(Dokan)
        elif opt == 2:
            product_name = input("Enter Product Name to Order: ")
            quantity = int(input("Enter Quantity: "))
            customer.place_order(Dokan, product_name, quantity)
        elif opt == 3:
            break
        else:
            print("Wrong Option")


def login():
    print("1. Login as Seller")
    print("2. Login as Customer")
    print("3. Back")
    login_opt = int(input("Enter Your Option:"))
    if login_opt == 1:
        email = input("Enter Your Email:")
        password = input("Enter Your Password:")
        if Dokan.login_seller(email, password):
            print("Seller Login Successful!")
            seller_section(Dokan.find_seller(email))

        else:
            print("Seller Login Failed!")

    elif login_opt == 2:
        email = input("Enter Your Email:")
        password = input("Enter Your Password:")
        if Dokan.login_customer(email, password):
            print("Customer Login Successful!")
            customer_section(Dokan.find_customer(email))
        else:
            print("Customer Login Failed!")
    elif login_opt == 3:
        return
    else:
        print("Invalid Option! Please try again.")
        login()

while 1:
    print("--------- Welcome to Dokan ---------")
    print("1. Sign Up as a Seller")
    print("2. Sign Up as a Customer")
    print("3. Login")
    print("4. Exit")

    opt = int(input("Enter Your Option:"))

    if opt==1:
        email=input("Enter Your Email:")
        password=input("Enter Your Password:")

        new_seller = Seller(email, password)
        Dokan.add_seller(new_seller)
        print("Seller Added Successfully!")
        seller_section(new_seller)
        
    elif opt==2:
        email=input("Enter Your Email:")
        password=input("Enter Your Password:")

        new_customer = Customer(email, password)
        Dokan.add_customer(new_customer)
        print("Customer Added Successfully!")
        customer_section(new_customer)
    elif opt==3:
        login()
    elif opt==4:
        print("Thank you for visiting Dokan!")
        break
    else:
        print("Invalid Option! Please try again.")
