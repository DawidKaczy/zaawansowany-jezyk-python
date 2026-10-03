

class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other):
        return RGB(self.r * other, self.g * other, self.b * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Division by zero")
        return RGB(self.r / other, self.g / other, self.b / other)

    def __repr__(self):
        return f"RGB:{self.r} {self.g} {self.b}"


c = RGB(100, 150, 200)
print(c)
print(c * 1.2)
print(0.8 * c)
print(c / 2)


