

class Product:
    def __init__(self, name, price):
        self.__name = name
        if isinstance(price, (int, float)):
            self.__price = price
        else:
            raise TypeError('Price must be int or float')
        if price >= 0:
            self.__price = price
        else:
            raise TypeError('Price must >= 0')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)):
            self.__price = price
        else:
            raise TypeError('Price must be int or float')
        if price >= 0:
            self.__price = price
        else:
            raise TypeError('Price must >= 0')

v1 = Product("Name", 1)

v1.price = 2

print(v1.price)


