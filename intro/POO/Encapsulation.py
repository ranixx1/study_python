class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private variable

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())
        
