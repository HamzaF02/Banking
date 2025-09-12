class StandardBankAccount:
    def _init_(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds")
            return False
    
    def account_info(self):
        return f"Account Holder: {self.account_holder} \n Balance: {self.balance}"

class SavingsAccount(StandardBankAccount):
    interest_rate = 0.02
    def _init_(self, account_holder, balance):
        super(account_holder, balance)
    
    def apply_interest(self):
        self.balance =  (1 + self.interest_rate) * self.balance
    

class CheckingAccount(StandardBankAccount):
    transaction_fee = 1
    def _init_(self, account_holder, balance):
        super(account_holder, balance)

    def withdraw(self, amount):
        if amount <= self.balance - self.transaction_fee:
            self.balance -= amount+self.transaction_fee
            return True
        else:
            print("Insufficient funds")
            return False
    