

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __add__(self, other):
        if not isinstance(other, Temperature):
            raise TypeError("Ten sam typ Temperature")
        return Temperature(self.celsius + other.celsius)

    def __repr__(self):
        return f"Temperature({self.celsius})"


v1 = Temperature(10)
v2 = Temperature(20)
v3 = Temperature(30)
print(v1 + v2)


