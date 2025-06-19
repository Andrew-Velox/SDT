from datetime import datetime

class Bank:
    def __init__(self,name,initail_balance):
        self.name=name
        self.users=[]
        self.admins=[]
        self.isbanckrupt=False
        self.initial_balance=initail_balance
        self.bank_balance=initail_balance
    
    def add_user(self,user):
        self.users.append(user)

    def Bankrupt(self,value):
        self.isbanckrupt=value

    def view_users(self):
        for user in self.users:
            print(user)
    
  



class User(Bank):
    def __init__(self,name,email,address,account_type,password,bank):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.account_type = account_type
        self.bank = bank
        self.balance = 0
        self.Transaction_historys=[]
        self.account_number=name+email
        self.loan_count=2
        bank.add_user(self)


    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print("Diposit Successfull")
            print(f"Your account Balance is now {self.balance}")
            self.Transaction_historys.append(f"{amount}tk has been deposite to your account at: {datetime.now()}\nYour Current Balane:{self.balance}")
            
        else:
            print("Amount is less then 1!")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded!")
        else:
            if self.bank.isbanckrupt:
                print("Bank is bankrupt, cannot withdraw!")
                return
     
            self.balance-=amount
            print("Withdraw Successfull")
            print(f"Your account Balance is now {self.balance}")
            self.Transaction_historys.append(f"{amount}tk has been Withdraw from your account at: {datetime.now()}\nYour Current Balane:{self.balance}")
    
    def check_available_balance(self):
        return self.balance
    
    def Transaction_history(self):
        print("Transiction History:")
        for history in self.Transaction_historys:
            print(history)

    def take_loan(self,amount):
        if self.bank.isbanckrupt:
            print("Bank is bankrupt, cannot take loan!")
            return
        if self.loan_count > 0:
            if self.bank.bank_balance<amount:
                print(f"You can take Maximum {self.bank.bank_balance}tk Loan!")
            else:
                self.bank.bank_balance-=amount
                self.balance+=amount
                a=(f"{amount}tk loan has been added to your account")
                b=(f"Current Ballance: {self.balance}")
                print(a)
                print(b)
                self.Transaction_historys.append(f"{a} at {datetime.now()}\n{b}")
                self.loan_count-=1
        else:
            print("Maximum Loan Taking Limit Exeed")

    def Transfer_amount(self,name,amount):
        if amount <= self.balance:
            for user in self.bank.users:
                if user.name.lower() == name.lower():
                    user.balance += amount
                    self.balance -= amount
                    print(f"Transferred {amount} to {user.name}. Your new balance is {self.balance}.")
                    self.Transaction_historys.append(f"{amount}tk has been Transfered to {user.name} at: {datetime.now()}\nYour Current Balane:{self.balance}")
                    user.Transaction_historys.append(f"{amount}tk has been Transfered from {self.name} at: {datetime.now()}\nYour Current Balane:{user.balance}")
                    return
            print(f"User {name} not found in the bank.")
        else:
            print(f"You dont have {amount} in your Account!")


    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Address: {self.address}, Account Type: {self.account_type}, Balance: {self.balance}, Account Number: {self.account_number}"

class Admin():
    def __init__(self,name,email,password,bank):
        self.name = name
        self.email = email
        self.password = password
        self.bank = bank

    def create_user(self,name,email,address,account_type, password):
        new_user = User(name, email, address, account_type,password, self.bank)
        print(f"User {new_user.name} created successfully.")

    def view_users(self):
        print(f"-----Users in Bank {self.bank.name}----")
        for user in self.bank.users:
            print(user)
        
    def delete_user(self,name):
        for x, user in enumerate(self.bank.users):
            if user.name.lower() == name.lower():
                print(f"User: {user.name} Deleted")
                del self.bank.users[x]
                return
        print(f"User Not Found")
    

    def total_bank_balance(self):
        print(f"Total Available Bank Balane: {self.bank.bank_balance}")

    def check_loan_amount(self):
        print(f"Total Loan Amount: {self.bank.initial_balance - self.bank.bank_balance}")
    
    def loan_feature(self, value):
        if value ==1:
            print("Loan Feature is Enabled")
            self.bank.isbanckrupt=False
        else:
            print("Loan Feature is Disabled")
            self.bank.isbanckrupt=True
        
    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Password: {self.password}"
    




Mafu = Bank("Mafu",1000000)
# Saimon = User("Saimon","saimon@gmail.com","Dhaka","Savings",Mafu)
# Farhan = User("Farhan","farhan@gmail.com","Chittagong","Current",Mafu)
# Tanvir = User("Tanvir","tanvir@gmail.com","Khulna","Savings",Mafu)

# Admin1 = Admin("Admin1","admin1@gmail.com","123",Mafu)

# Admin1.view_users()
# Admin1.total_bank_balance()
# Admin1.check_loan_amount()


# print(Saimon)
# # Saimon.withdraw(100)
# Saimon.deposit(500)
# Saimon.withdraw(100)
# Saimon.Transaction_history()
# print("Users----")
# Mafu.view_users()

def login_or_signup(option):
    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            if option == 1:
                input_name = input("Enter Admin Name: ")
                input_password = input("Enter Admin Password: ")
                for admin in Mafu.admins:
                    if admin.name.lower() == input_name.lower() and admin.password == input_password:
                        print("Admin logged in successfully.")
                        admin_section(admin)
                        return
                else:
                    print("Admin not found. Please try again.")
            elif option == 2:
                input_name = input("Enter User Name: ")
                input_password = input("Enter User Password: ")
                for user in Mafu.users:
                    if user.name.lower() == input_name.lower() and user.password == input_password:
                        print("User logged in successfully.")
                        user_section(user)
                        return
                print("User not found. Please try again.")
        elif choice == 2:
            if option == 1:
                input_name = input("Enter Admin Name: ")
                input_email = input("Enter Admin Email: ")
                input_password = input("Enter Admin Password: ")
                admin = Admin(input_name, input_email, input_password, Mafu)
                Mafu.admins.append(admin)
                print("Admin signed up successfully.")
                admin_section(admin)
                return
        
            elif option == 2:
                input_name = input("Enter User Name: ")
                input_email = input("Enter User Email: ")
                input_address = input("Enter User Address: ")
                input_account_type = input("Enter Account Type (Savings/Current): ")
                input_password = input("Enter User Password: ")

                user = User(input_name, input_email, input_address, input_account_type, input_password, Mafu)
                print("User signed up successfully.")
                user_section(user)
                return
        elif choice == 3:
            print("Returning to Main Menu...")
            return
        else:
            print("Invalid choice. Please try again.")

def admin_section(admin):
    while True:
        print("----Admin Section----")
        print("1. Create Account")
        print("2. View Users")
        print("3. Delete User")
        print("4. Check Total Bank Balance")
        print("5. Check Loan Amount")
        print("6. Loan Feature Enable/Disable")
        print("7. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            address = input("Enter User Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            password = input("Enter User Password: ")
            admin.create_user(name, email, address, account_type, password)
        elif choice == 2:
            admin.view_users()
        elif choice == 3:
            name = input("Enter User Name to Delete: ")
            admin.delete_user(name)
        elif choice == 4:
            admin.total_bank_balance()
        elif choice == 5:
            admin.check_loan_amount()
        elif choice == 6:
            value = int(input("Enter 1 to Enable Loan Feature, 0 to Disable: "))
            admin.loan_feature(value)
        elif choice == 7:
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

def user_section(user):
    while True:
        print(f"----Welcome {user.name}----")
        print("----User Section----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Available Balance")
        print("4. Transaction History")
        print("5. Transfer Amount")
        print("6. Take Loan")
        print("7. Logout")

        opt = int(input("Enter your choice: "))
        if opt == 1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif opt == 2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif opt == 3:
            print(f"Available Balance: {user.check_available_balance()}")
        elif opt == 4:
            user.Transaction_history()
        elif opt == 5:
            name = input("Enter the name of the user to transfer amount: ")
            amount = float(input("Enter amount to transfer: "))
            user.Transfer_amount(name, amount)
        elif opt == 6:
            amount = float(input("Enter loan amount: "))
            user.take_loan(amount)
        elif opt == 7:
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")

while 1:
    print(f"----Welcome to {Mafu.name} Bank----")
    print("1.Admin")
    print("2.User")
    print("3.Exit")

    opt = int(input("Enter your option: "))
    
    if opt == 1:
        login_or_signup(1)
    elif opt == 2:
        login_or_signup(2)
    elif opt == 3:
        print("Exiting the Bank Management System. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

