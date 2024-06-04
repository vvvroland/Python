class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        	
    def deposit(self, amount):
        self.balance+=amount
        print(f"Customer balance is {self.balance}.")
        return self

    def withdraw(self, amount):
        self.balance-=amount
        print(f"Customer balance is {self.balance}.")
        return self

    def display_account_info(self):
        print(f"Customer balance is {self.balance}. and their interest rate is {self.int_rate}.")
        return self

    def yield_interest(self):
        if self.balance>=0:
            self.balance+=self.balance*self.int_rate
            print(f"Customer balance is {self.balance}.")
        return self




poor = BankAccount(.09, 90)
rich = BankAccount(.05, 5000000)

poor.deposit(350).deposit(260).deposit(100).withdraw(75).yield_interest()
rich.deposit(35000).deposit(750000).withdraw(5900).withdraw(1000000).withdraw(58000).withdraw(490000).yield_interest()
