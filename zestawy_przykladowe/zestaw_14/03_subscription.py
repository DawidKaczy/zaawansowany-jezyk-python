class Subscription:
    def __init__(self, name, base_monthly_price, loyalty_discount = 0.0):
        self.name = name
        self.base_monthly_price = base_monthly_price
        self.loyalty_discount = loyalty_discount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name must not be empty")
        self.__name = name

    @property
    def base_monthly_price(self):
        return self.__base_monthly_price

    @base_monthly_price.setter
    def base_monthly_price(self, base_monthly_price):
        if type(base_monthly_price) not in (int, float):
            raise TypeError("base_monthly_price must be a number")
        if base_monthly_price <= 0:
            raise ValueError("base_monthly_price must be a positive number")
        self.__base_monthly_price = base_monthly_price

    @property
    def loyalty_discount(self):
        return self.__loyalty_discount

    @loyalty_discount.setter
    def loyalty_discount(self, loyalty_discount):
        if type(loyalty_discount) not in (int, float):
            raise TypeError("loyalty_discount must be a number")
        if not 0 <= loyalty_discount <= 100:
            raise ValueError("loyalty_discount must be a number between 0 and 100")
        self.__loyalty_discount = loyalty_discount

    @property
    def final_monthly_price(self):
        wynik = self.base_monthly_price * (1 - (self.loyalty_discount / 100))
        return round(wynik, 2)

    def __repr__(self):
        return f"{self.name} {self.base_monthly_price} {self.loyalty_discount} {self.final_monthly_price}"

v = Subscription("V1", 100)
v1 = Subscription("V1", 100, 15)
print(v1)
print(v)

try:
    v1 = Subscription("", 100, 15)
except TypeError and ValueError as e:
    print(e)

try:
    v2 = Subscription("Ok", -1, 15)
except TypeError and ValueError as e:
    print(e)

try:
    v2 = Subscription("Ok", 100, 101)
except TypeError and ValueError as e:
    print(e)
