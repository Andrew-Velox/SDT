from menu import Menu
   
class Resturant:
    def __init__(self,name):
        self.name=name;
        self.employees=[]
        self.menu=Menu()
    
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} is Added Successfull")

    def view_employees(self):
        if len(self.employees)==0:
            print("There is no Employees")
        else:
            print("\n \tEmployee List: \n")
            for employee in self.employees:
                print(f"Name:{employee.name}  Age:{employee.age}")
        
