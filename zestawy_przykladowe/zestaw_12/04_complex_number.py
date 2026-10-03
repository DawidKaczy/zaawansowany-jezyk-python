

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, other):
        if type(other) in (int, float):
            return ComplexNumber(self.real * other, self.imag * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other == 0:
            return NotImplemented
        if type(other) in (int, float):
            return ComplexNumber(self.real / other, self.imag / other)
        return NotImplemented

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

z = ComplexNumber(3, 4)
print(z * 2)
print(0.5 * z)
print(z / 4)


