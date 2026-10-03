
class Price:
    def __init__(self, price):
        if type(price) != float:
            raise TypeError("Price must be a float")
        self.price = price

    def __truediv__(self, other):
        return Price(self.price / other)\

    def __repr__(self):
        return f"Price({self.price})"

v1 = Price(10.0)
print(v1 / 3)