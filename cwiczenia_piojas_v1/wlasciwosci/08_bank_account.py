
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def owner(self, value):
        if len(value) < 2:
            raise ValueError("Nazwa ownera dłuższa niż jeden")
        if value == "":
            raise ValueError("nie może byc pusta")
        self.__owner = value

    def __repr__(self):
        return f"BankAccount(owner={self.__owner}, balance={self.__balance})"

v1 = BankAccount("1", 2)
print(v1)
v1.owner = "2s"
print(v1)

s = "ok  "
print(len(s))
print(s.strip())
print(len(s.strip()))


