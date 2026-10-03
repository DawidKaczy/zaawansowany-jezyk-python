class Product:
    def __init__(self, name, base_price, discount = 0):
        self.name = name
        self.base_price = base_price
        self.discount = discount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Product name must be a string")
        if not name.strip():
            raise ValueError("Name is required")
        self.__name = name

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, base_price):
        if type(base_price) not in (int, float):
            raise ValueError("Base price must be a number")
        if base_price < 0:
            raise ValueError("Base price must be a positive number")
        self.__base_price = base_price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        if type(discount) not in (int, float):
            raise ValueError("Discount must be a number")
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100")
        self.__discount = discount

    @property
    def final_price(self):
        wynik = self.__base_price * (1 - (self.__discount/ 100))
        return round(wynik, 2)

    def __str__(self):
        return f"Name:{self.name} | Base price:{self.base_price} | After discount:{self.final_price}"

v1 = Product("V1", 100, 2)
print(v1)






