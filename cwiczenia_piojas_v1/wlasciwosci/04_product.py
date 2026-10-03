class Product:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        self.__name = name


        if not isinstance(price, (int, float)):
            raise TypeError("Price must be of type int or float")
        self.__price = price


    def dekorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"Przed {self.__name}, {self.__price} ")
            wynik = func(self, *args, **kwargs)
            print(f"Po {self.__name}, {self.__price} ")
            return wynik
        return wrapper


    @property
    def name(self):
        if not isinstance(self.name, str):
            raise TypeError("Name must be of type str")
        return self.__name


    @property
    def price(self):
        if not isinstance(self.price, (int, float)) and self.price < 0:
            raise TypeError("Price must be of type int or float")
        return self.__price

    @price.setter
    @dekorator
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be of type int or float")
        self.__price = price

    def __str__(self):
        return f"{self.__name}, {self.__price}"

v1 = Product("Jabłko", 1.2)
v1.price = 2
print(v1)