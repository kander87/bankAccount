class BankAccount:
    all_accounts = []     # new class attribute - a list of all the accounts!
    account_count = 0  #new class attribute to track # of accounts

    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self) #adds each new account to the all accounts list
        BankAccount.account_count +=1
    
    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def all_info(cls):
        print(f"{cls.account_count} bank accounts in the program.")
        sum =0
        for account in cls.all_accounts:
            print(account.balance)

    #Add a deposit method to the BankAccount class
    def deposit(self,amount):
        self.balance = self.balance +amount
        print(self.balance)
        return self
    
    #Add a withdraw method to the BankAccount class
    def withdraw(self,amount):
        if (self.balance - amount) >= 0:
            self.balance = (self.balance -amount)
            print(self.balance)
        else: 
            self.balance = (self.balance -amount - 25)
            print(f"You broke! Here is an overdraft fee to make you broker!{self.balance}")
        return self

    #Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Your interest rate is: {self.int_rate}. You have a balance of {self.balance} dollars")
        return self

    # Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        self.balance = self.balance + (1 *self.int_rate)
        print(self.balance)
        return self

#create 2 accounts
kateAccount= BankAccount(0.05,100)
booButtAccount= BankAccount(0.07,1000)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
kateAccount.deposit(150).deposit(75.36).deposit(42).withdraw(225).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
booButtAccount.deposit(30).deposit(55).withdraw(32).withdraw(45).withdraw(90.99).withdraw(1042.42).yield_interest().display_account_info()

#call class method
BankAccount.all_info()
