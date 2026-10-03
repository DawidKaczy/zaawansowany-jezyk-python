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
            raise TypeError('radius cannot be negative')

v1 = Circle(5)
v2 = Circle(10)

v1.radius = 2

print(v1.radius)


