
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Nie może byc na minusie")
        self.balance = balance

v1 = BankAccount("Dawid", 100)
#v2 = BankAccount("Dawid", -100)
