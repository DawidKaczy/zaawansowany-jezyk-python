import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.radius * self.radius * math.pi

v1 = Circle(5)
print(v1.area)


