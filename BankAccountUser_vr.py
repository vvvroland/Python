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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self,amount):
       # self.account+=amount
        #print(f"{self.name}'s new balance is {self.account}.")
        self.account.deposit(amount)
    	# your code here

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

Rhodes=User("Rhodes", "Bad.Rhodes@mail.com")


Rhodes.make_deposit(500)
Rhodes.make_deposit(7001)
Rhodes.display_user_balance()