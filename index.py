class BankAccount:
    # Initializes the account with account holder name and balance
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
    
    # Adds the amount to the account balance
    def deposit(self, amount):
        if amount > 0 : self.balance += amount
    
    # Widthdraws amount from the account if sufficient funds are available
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def account_info(self):
        return f"Account Holder: {self.account_holder} \nBalance: {self.balance}"

class SavingsAccount(BankAccount):
    interest_rate = 0.02
    
    # Applies interest to the current balance
    def apply_interest(self):
        self.balance =  (1 + self.interest_rate) * self.balance

class CheckingAccount(BankAccount):
    transaction_fee = 1

    def withdraw(self, amount):
        #Adds transaction fee to the amount before withdraw
        amount += self.transaction_fee
        super().withdraw(amount)


# Testing of classes
def main():
    # Creates a standard bank account
    standard = BankAccount("Lars",100)

    # Withdraws 30 from the account and prints the account info (Balance should be 70)
    standard.withdraw(30)
    print("Balance should be 70 with the name Lars\n"+standard.account_info())

    # Should print "Insufficient funds"
    print("\nShould print 'Insufficient funds' after trying to withdraw too much")
    standard.withdraw(90)

    # Withdraws 70 from the account (Balance should be 0)
    standard.withdraw(70)
    print("\nBalance should be 0 with the name Lars\n"+standard.account_info())
    
    # Adds 20 to account and prints the account info (Balance should be 20)
    standard.deposit(20)
    print("\nBalance should be 20 with the name Lars\n"+standard.account_info())

    # Adds negative amount to account and prints the account info (Balance should still be 20)
    standard.deposit(-10)
    print("\nBalance should still be 20 with the name Lars after negative deposit\n"+standard.account_info())

    # Creates another standard bank account with default balance (0)
    standard2 = BankAccount("Henrik")
    print("\nBalance should be 0 with the name Henrik\n"+standard2.account_info())

    # Creates a savings account
    saving = SavingsAccount("Jens",100)

    # Applies intrest, then balance should be 102
    saving.apply_interest()
    print("\nBalance should be 102 with the name Jens\n"+saving.account_info()) 

    
    # Creates a checking account
    checking = CheckingAccount("Abdullah",100)

    # Withdraws 50 from the account and prints the account info (Balance should be 49)
    checking.withdraw(50)
    print("\nBalance should be 49 with the name Abdullah\n"+checking.account_info()) 
    print("\nShould print 'Insufficient funds' after tryint to withdraw too much with transaction fee")
    checking.withdraw(49) # Should print "Insufficient funds"


# Calls the main function to run the tests
if __name__ == "__main__":
    main()