class Bank:
    def __init__(self,account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            return f"Insufficient balance. Your current balance is {self.balance}"
    def bank_fees(self):
        fees = self.balance * 0.05
        # self.balance -= fees
        return fees
    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

acc1 = Bank("1234567890", "John Doe", 1000)
# print(acc1.account_number)
# print(acc1.display())
# print(acc1.deposit(500))
print(acc1.bank_fees())
# print(acc1.balance())