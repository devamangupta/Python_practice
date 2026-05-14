# Here we try to create a simple ATM machine using OOPs concepts in python
class Atm:
    # Create a constructor for the Atm class
    def __init__(self, name, pin, balance):
        # The below variavles are instance variables which will be used to store the name, pin and balance of the user which means they different for different objects of the class and they are used to store the data of the user
        self.name = name
        self.pin = pin
        self.balance = balance
        self.menu() # This will call the menu method of the class and display the menu of the ATM machine
    # create a method to display menu of ATM
    def menu(self):
        print("Welcome to the ATM Machine")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        # Take input from the user to select an option from the menu
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            print("You choose to check your balance")
            self.check_balance()
            self.menu()
        elif user_input == 2:
            print("You choose to withdraw money")
            self.withdraw()
            self.menu()
        elif user_input == 3:
            print("You choose to deposit money")
            self.deposit()
            self.menu()
        elif user_input == 4:
            print("You choose to exit")
            exit()
        else:
            print("Invalid choice")
            self.menu()
    # Create a method to check balance of the user
    # First we will ask the user to enter their pin and then we will chekc if the pin is correct or not, if the pin is same then user will be able to see it's balance orther wise it's will show invalid pin as output
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if self.pin == user_pin:
            print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin")
    # Here we create a method for withdrawing money from the user's account
    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance...")
            else:
                self.balance -= amount
                print("Amount withdraw successfully")
                print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin")
    # Here we create a method for depositing money in the user's account
    def deposit(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
            print("Your current balance is: ", self.balance)
        else:
            print("Invalid pin")
# Create an object of the Atm class
atm = Atm("John", "1234", 1000)
