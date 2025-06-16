from users import User,Admin,Customer,Employee
from food_item import Food_itm
from menu import Menu
from order import Order
from restaurant import Resturant


Touka_Restaurant = Resturant("Touka Resturant")
def Customer_Section():
    print("--------- Customer Menu ---------")
    name = input("Enter Your Name: ")
    number = int(input("Enter Your Number: "))
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")

    customer = Customer(name=name,number=number,email=email,address=address)


    while 1:
        print(f"--------Welcome {customer.name}---------------")    
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Pay Bill")
        print("6. Exit")

        # print("--------- Please Select an Option ---------")
        opt=int(input("Please Select an Option: "))

        if opt==1:
            customer.show_menu(Touka_Restaurant)
        elif opt==2:
            itm_name=input("Enter Item Name: ")
            quantity=int(input("Enter Quantity: "))
            customer.add_to_cart(Touka_Restaurant,itm_name=itm_name,quantity=quantity)
        elif opt==3:
            customer.view_cart()
        elif opt==4:
            itm_name=input("Enter Item Name: ")
            customer.remove_from_cart(itm_name=itm_name)
        elif opt==5:
            customer.pay_bill()
        elif opt==6:
            break
        else:
            print("Wrong Option")

def Admin_Section():
    print("--------- Admin Menu ---------")
    name = input("Enter Your Name: ")
    number = int(input("Enter Your Number: "))
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")

    admin = Admin(name=name,number=number,email=email,address=address)


    while 1:
        print(f"--------Welcome {admin.name}---------------")    
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Add Item")
        print("4. Remove Item")
        print("5. Show Item")
        print("6. Exit")

        # print("--------- Please Select an Option ---------")
        opt=int(input("Please Select an Option: "))

        if opt==1:
            emp_name=input("Enter Name: ")
            emp_Number=input("Enter Number: ")
            emp_email=input("Enter Email: ")
            emp_address=input("Enter Address: ")
            emp_age=input("Enter Age: ")
            emp_salary=input("Enter Salary: ")
            emp_designation=input("Enter Designation: ")
            
            employee=Employee(name=emp_name,number=emp_Number,email=emp_email,address=emp_address,age=emp_age,salary=emp_salary,desigation=emp_designation)
            admin.add_employee(Touka_Restaurant,employee=employee)
        elif opt==2:
            admin.view_employees(Touka_Restaurant)
        elif opt==3:
            itm_name=input("Enter Name: ")
            itm_price=int(input("Enter Price: "))
            itm_quantity=int(input("Enter Quantity: "))

            food_itm = Food_itm(name=itm_name,price=itm_price,quantity=itm_quantity)
            admin.add_itm(Touka_Restaurant,food_itm)
        elif opt==4:
            itm_name=input("Enter item Name: ")
            admin.remove_menu(Touka_Restaurant,itm=itm_name)
        elif opt==5:
            admin.show_itm(Touka_Restaurant)
        elif opt==6:
            break
        else:
            print("Wrong Option")


while 1:
    print("-------------WELCOME--------------")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    opt=int(input("Enter Option: "))

    if opt==1:
        Customer_Section()
    elif opt==2:
        Admin_Section()
    elif opt==3:
        break
    else:
        print("Wrong Option")
