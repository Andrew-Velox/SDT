from abc import ABC
from order import Order
import copy

class User(ABC):
    def __init__(self,name,number,email,address):
        self.name=name
        self.number=number
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self,name,number,email,address):
        super().__init__(name,number,email,address)
        self.cart=Order()

    def show_menu(self,resturant):
        resturant.menu.show_menu()


    def add_to_cart(self,resturan,itm_name,quantity):
        get_itm=resturan.menu.find_menu(itm_name)
        if get_itm:
            if quantity>get_itm.quantity:
                print("Quantity Exceed")
            else:
                temp_itm=copy.deepcopy(get_itm)
                temp_itm.quantity=quantity
                get_itm.quantity-=quantity
                # get_itm.quantity=quantity

                self.cart.add_item(temp_itm)
                print(f"{itm_name} added to cart")
        else:
            print(f"{itm_name} not found")

            
    def remove_from_cart(self,itm_name):
        get_itm=self.cart.find_item(itm_name)
        if not get_itm:
            print(f"{itm_name} not found in cart")
            return
        # print(get_itm.name)
        self.cart.remove_item(get_itm)
        

    def view_cart(self):
        if not self.cart.items:
            print("Cart is Empty")
        else:
            print("\tCart_Items")
            print(f"\tName:\tPrice:\tQuantity:")
            for itm,quantity in self.cart.items.items():
                print(f"\t{itm.name}\t{itm.price}\t{quantity}")
            print(f"\n\tTotal Price: {self.cart.total_price}")


    def pay_bill(self):
        print(f"Total {self.cart.total_price} Payed Successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, number, email, address,age,salary,desigation):
        super().__init__(name, number, email, address)
        self.age=age
        self.salary=salary
        self.designation=desigation

class Admin(User):
    def __init__(self, name, number, email, address):
        super().__init__(name, number, email, address)
        self.employees=[]
    
    def add_employee(self,resturant,employee):
        resturant.add_employee(employee)

    def view_employees(self,resturant):
        resturant.view_employees()
    
    def add_itm(self,resturant,itm):
        resturant.menu.add_menu(itm)
    
    def remove_menu(self,resturan,itm):
        resturan.menu.remove_menu(itm)
    def show_itm(self,resturant):
        resturant.menu.show_menu()


 

        

# resturant_1 = Resturant("Touka")
# admin = Admin("Mohabbat",3434545,"mohabbat.bd2020@gmail.com","Dhaka")
# emp_1 = Employee("Shamim",1243434,"shamim@gmail.com","Dhaka",20,30000,"Enginer")
# admin.add_employee(resturant_1,emp_1)
# admin.view_employees(resturant_1)


# menu = Menu()
# itm_1 = Food_itm("Burger",10.1,10)
# itm_2 = Food_itm("Pizza",23.2,14)
# itm_3 = Food_itm("Noddle",4.2,20)
# itm_4 = Food_itm("Fries",5,40)


# menu.add_menu(itm_1)
# menu.add_menu(itm_2)
# menu.add_menu(itm_3)
# menu.add_menu(itm_4)
# menu.remove_menu("noddle")
# menu.remove_menu("noddle")
# menu.show_menu()
# emp = Employee("Shamim",1243434,"shamim@gmail.com","Dhaka",20,30000,"Enginer")
# print(emp.name, emp.age)

# admin.add_itm(resturant_1,itm_1)
# admin.add_itm(resturant_1,itm_2)
# admin.add_itm(resturant_1,itm_3)
# admin.add_itm(resturant_1,itm_4)
# admin.show_itm(resturant_1)
# admin.remove_menu(resturant_1,"noodle")
# admin.remove_menu(resturant_1,"noddle")
# admin.show_itm(resturant_1)


# customer = Customer("Halk",432443,"halk@gmail.com","Khulna")
# customer.show_menu(resturant_1)

# customer.add_to_cart(resturant_1,"Burger",3)
# customer.add_to_cart(resturant_1,"noddle",2)
# customer.view_cart()
# customer.show_menu(resturant_1)


# customer.add_to_cart(resturant_1,"noddle",1)
# customer.view_cart()
# customer.show_menu(resturant_1)




        