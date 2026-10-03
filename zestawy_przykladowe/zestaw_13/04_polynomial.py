class Polynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __mul__(self, other):
        if type(other) in (int, float):
            return Polynomial(self.a * other, self.b * other, self.c * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Polynomial(self.a / other, self.b / other, self.c / other)
        return NotImplemented

    def __repr__(self):
        return f"Polynomial({self.a}, {self.b}, {self.c})"

p = Polynomial(1, -3, 2)
print(p)
print(p * 3)
print(0.5 * p)
print(p / 2)
