from numpy.ma.core import minimum


class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Negative amount")
        self.__balance += amount

    def withdraw(self , amount):
        if amount > self.__balance:
            raise ValueError("Negative amount")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):

    def withdraw(self , amount):
        minimum_savings = amount
        if amount < 0:
            raise ValueError("Negative amount")

