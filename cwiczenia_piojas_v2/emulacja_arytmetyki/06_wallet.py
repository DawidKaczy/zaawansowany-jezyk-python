

class Wallet:
    def __init__(self, balance):
        self.balance = balance


    def __floordiv__(self, other):
        return Wallet(self.balance // other)

    def __mod__(self, other):
        return Wallet(self.balance % other)

    def __repr__(self):
        return str(self.balance)


v1 = Wallet(100)
print(v1)

print(v1 // 3)
print(v1 % 3)