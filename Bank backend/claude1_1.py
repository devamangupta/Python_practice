def deposite(acc_no, amount, Account):
    if amount >= 0:
        Account[acc_no]["Balance"] += amount
        Account[acc_no]["transaction"].append(amount)
    else:
        print("You enter wrong value..\n So please check!!!")

def withdraw(acc_no, amount, Account):
    if amount >= 0:
        Account[acc_no]["Balance"] -= amount
        amount = -amount
        Account[acc_no]["transaction"].append(amount)
    else:
        print("You enter wrong value..\n So please check!!!")
def detail(acc_no, Account):
    print(Account[acc_no]["transaction"])

def transfer(acc_no,to_acc,Account, amount):
    if acc_no == to_acc:
        print("Don't sent amount in same account...")
    elif acc_no not in Account:
        print("Senders Account not found!!!")
    elif to_acc not in Account:
        print("Reciever Account not found!!!")
    Account[to_acc]["Balance"] += amount
    Account[acc_no]["Balance"] -= amount
    Account[to_acc]["transaction"].append(amount)
    amount = -amount
    Account[acc_no]["transaction"].append(amount)