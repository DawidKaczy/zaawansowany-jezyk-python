class BankAccount:
    def __init__(self, owner , balance = 0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

v1 = BankAccount("Dawid", 15)
v2 = BankAccount("Kamil", 15)
