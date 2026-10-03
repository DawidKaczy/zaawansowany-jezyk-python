import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius * self.radius


v1 = Circle(2)
v2 = Circle(3)

print(f"{v1.radius}, {v1.area}")
print(f"{v2.radius}, {v2.area}")