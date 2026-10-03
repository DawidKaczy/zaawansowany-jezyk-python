class Account:
    def __init__(self, owner, balance, interest_rate = 0.0):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, str):
            raise TypeError("Owner musi byc str")
        if not owner.strip():
            raise ValueError("Owner nie może być pusty")
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if type(balance) not in (int, float):
            raise TypeError("Balance musi byc int lub float")
        if balance < 0:
            raise ValueError("Balance musi być dodatni")
        self.__balance = balance

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        if type(interest_rate) not in (int, float):
            raise TypeError("Interest musi byc int lub float")
        if not (0 <= interest_rate <= 100):
            raise ValueError("Interest musi być pomiędzy 0 a 100")
        self.__interest_rate = interest_rate

    @property
    def final_balance(self):
        wynik = (self.balance * (self.interest_rate / 100)) + self.balance
        return round(wynik, 2)

    def __str__(self):
        return f"Owner:{self.owner}, Balance:{self.balance}, InterestRate:{self.interest_rate}, Final:{self.final_balance:.2f}"


v1 = Account("wielki ", 200,2)
print(v1)
