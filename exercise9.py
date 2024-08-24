# A program to manage my bank Account


class Account:
    def __init__(self,bal,acc):
        self.balance = bal 
        self.account_no= acc 

    # for debit
    def deb(self,amount):
        self.balance-=amount
        print("Rs.",amount,"Was debited")
        print("Total balance",self.get_balance())

    # for credit
    def cred(self,amount):
        self.balance+=amount
        print("Rs.",amount,"Was credited")
        print("Total balance",self.get_balance())
    

    # for balance
    def get_balance(self):
        return self.balance


a1 = Account(9000, 4004)
a1.cred(500)
a1.deb(1000)