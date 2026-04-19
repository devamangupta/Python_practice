print("Here we create a ATM class and create a object of that class and call the method of that class")
class Atm:
    def __init__(self):
        self.pin ="1234"
        self.balance = 10000
        self.show_menu()
        # self.menu(self)

    def show_menu(self):
        print("Welcome to ATM\n How can I help you\n 1. Create Pin\n 2. Deposit\n 3. Withdraw\n 4. Check Balance\n 5. Change pin\n 6. Exit")
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            # Here we create user pin and store it in the object
            self.create_pin()
            self.show_menu
        elif user_input == 2:
            # Here we deposit the amount in our account and update the balance
            self.deposit()
            self.show_menu()
        elif user_input == 3:
            # Here we withdraw the amount from our account and update the balance
            self.withdraw()
            self.show_menu()
        elif user_input == 4:
            # Here we check the balance of our account
            self.check_balance()
            self.show_menu()
        elif user_input == 5:
            # For changing pin or our ATM 
            self.change_pin()
            self.show_menu()
        elif user_input == 6:
            exit()
        else:
            print("Invalid choice")
            self.show_menu()


    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin
        print("Pin created successfully")
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Invalid pin")
            self.show_menu()
    def deposit(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
            print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin")
            # self.show_menu()
    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount you want to withdraw:"))
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully")
                print("Your current balance is: ", self.balance)
            else:
                print("Insufficient balance")
                self.show_menu()
        else:
            print("Invalid pin")
            self.show_menu()
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin")
            self.show_menu()
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Invalid pin")
            self.show_menu()

__init__main__ = Atm()
aman = Atm()
# print(aman.pin)
# print(aman.balance)
print(aman)
