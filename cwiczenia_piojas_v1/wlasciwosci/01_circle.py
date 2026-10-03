
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be greater than 0")


v1 = Circle(1)
v1.radius = -1
print(v1.radius)
