# Simulate a simple bank with multiple accounts. Your program should:
# 1.Store accounts as a dictionary — key = account number (integer), value = another dict with "name", "balance", and "transactions" (a list).
# 2.Pre-load 3 accounts with sample names and balances to start.
# 3.Run a while loop presenting a menu: Deposit / Withdraw / Transfer / View Statement / Exit.
# 4.Use if / elif / else to route to the correct action. Validate every input — reject negative amounts, overdrafts, and invalid account numbers.
# 5.Every successful transaction appends a tuple to the account's "transactions" list — e.g. ("deposit", 500, "2024-01-10").
# 6.For Transfer, deduct from source and add to destination atomically — only if source has enough balance.
# 7.View Statement: use a for loop to print all transactions with a running balance, and show total credits vs debits using arithmetic operators.
# 8.On exit, print a summary report of all accounts showing final balances, sorted from highest to lowest using a loop.

from claude1_1 import deposite, withdraw, detail, transfer
# Account Details we have in our DB
Account = {
    2001 : {
        "Name" : "Aditya",
        "Balance" : 50000,
        "transaction": [5000, 11000, 3000]
    },
    1999 : {
        "Name" : "Jyoti",
        "Balance" : 100000,
        "transaction": [15000, 31000, 30000]
    },
    2003 : {
        "Name" : "Aman",
        "Balance" : 20000,
        "transaction": [500, 200]
    }
}

while True:
    # First enter your account to check you are vaild customer or not!!!
    acc_no = int(input("Enter you Account Number:"))
    if acc_no in Account:
        print("Account Holder Name is ",Account[acc_no]["Name"])
        while True:
            print("\n ===BANK MENU ===")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. View Statement")
            print("5. Exit")
            choice = int(input("Enter a number mentioned above:"))
            if choice == 1:
                print("You select Deposit")
                amount = int(input("Enter Amount:"))
                deposite(acc_no,amount,Account)
                print("Your current Balance: ", Account[acc_no]["Balance"])
            elif choice == 2:
                print("You select Withdraw")
                amount = int(input("Enter Amount:"))
                withdraw(acc_no,amount, Account)                
                print("Your current Balance: ", Account[acc_no]["Balance"])
            elif choice == 3:
                print("You select Transfer")
                to_acc = int(input("Enter a Reciver's Account No.:"))
                amount = int(input("Enter Amount you want to sent:"))
                transfer(acc_no, to_acc, Account, amount)

            elif choice == 4:
                print("You select View Statement")
                detail(acc_no,Account)

            elif choice == 5:
                print("You select to Exit")
                break
            else:
                print("Invalid Statement...")
    elif acc_no not in Account:
        print("Not Found Your Account Please check your Account Number:")
        skip = input("If you want to exit press E: ") 
        if skip == "E":
            break
            