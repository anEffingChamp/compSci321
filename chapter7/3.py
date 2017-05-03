# Jonathan Smalls
# computer science 321
# 7.3: account class
class Account:
    def __init__(self):
        self._id = int(0)
        self._balance = float(100)
        self._annualInterestRate = float(0)

    def getMonthlyInterestRate():
        return self._annualInterestRate / 12

    def getMonthlyInterest():
        rate    = getMonthlyInterestRate()
        balance = self._balance + (self._balance * rate)
        return balance

    def withdraw(input):
        self._balance -= input

    def deposit(input):
        self._balance += input
