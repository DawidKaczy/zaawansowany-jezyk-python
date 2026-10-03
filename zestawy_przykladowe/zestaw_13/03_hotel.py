class Hotel:
    def __init__(self, name, price_per_night, discount = 0.0):
        self.name = name
        self.price_per_night = price_per_night
        self.discount = discount
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Must be str")
        if not name.strip():
            raise ValueError("Cant be empty")
        self.__name = name
    @property
    def price_per_night(self):
        return self.__price_per_night
    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if type(price_per_night) not in (int, float):
            raise TypeError("Must be int or float")
        if price_per_night <= 0:
            raise ValueError("Must be positive")
        self.__price_per_night = price_per_night
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount):
        if type(discount) not in (int, float):
            raise TypeError("Must be int or float")
        if not 0 <= discount <= 100:
            raise ValueError("Must be between 0 and 100")
        self.__discount = discount
    @property
    def final_price(self):
        wynik = self.price_per_night * (1 - (self.discount / 100))
        return round(wynik, 2)
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price_per_night}, Discount: {self.discount}, Final price: {self.final_price}"

v1 = Hotel("V1", 200, 25.3)
print(v1)

try:
    v1 = Hotel("v1", 200, 101)
except ValueError and TypeError as e:
    print(e)



