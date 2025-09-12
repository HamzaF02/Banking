class StandardBankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def account_info(self):
        return f"Account Holder: {self.account_holder} \nBalance: {self.balance}"

class SavingsAccount(StandardBankAccount):
    interest_rate = 0.02
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)
    
    def apply_interest(self):
        self.balance =  (1 + self.interest_rate) * self.balance

class CheckingAccount(StandardBankAccount):
    transaction_fee = 1
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    def withdraw(self, amount):
        #Adds transaction fee to the amount to withdraw
        amount += self.transaction_fee
        super().withdraw(amount)


# Testing of classes
def main():
    # Creates a standard bank account
    standard = StandardBankAccount("Lars",100)

    # Withdraws 30 from the account and prints the account info (Balance should be 70)
    standard.withdraw(30)
    print(standard.account_info())

    # Should print "Insufficient funds"
    standard.withdraw(90)

    # Adds 20 to account and prints the account info (Balance should be 90)
    standard.deposit(20)
    print(standard.account_info())


    # Creates a savings account
    saving = SavingsAccount("Jens",100)

    # Applies intrest, then balance should be 102
    saving.apply_interest()
    print(saving.account_info()) 

    
    # Creates a checking account
    checking = CheckingAccount("Abdullah",100)

    # Withdraws 50 from the account and prints the account info (Balance should be 49)
    checking.withdraw(50)
    print(checking.account_info()) 
    checking.withdraw(49) # Should print "Insufficient funds"




if __name__ == "__main__":
    main()