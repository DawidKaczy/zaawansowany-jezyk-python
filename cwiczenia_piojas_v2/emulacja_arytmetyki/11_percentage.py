

class Percentage:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Percentage):
            return self.value / 100 * other.value / 100
        if type(other) in (int, float):
            return self.value/100 * other
        return NotImplemented

    def __repr__(self):
        return str(self.value)


v1 = Percentage(50)
print(v1 * v1)