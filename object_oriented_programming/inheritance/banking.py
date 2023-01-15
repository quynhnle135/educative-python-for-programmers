class Account():
    def __init__(self, title=None, balance=0):
        self.title = title
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f"Title is {self.title} and Balance is {self.getBalance()}"


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        interest_amount = (super().getBalance() * self.interestRate) / 100
        return interest_amount

