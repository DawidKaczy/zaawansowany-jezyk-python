

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float) or other == 0:
            return Vector2D(self.x / other, self.y / other)
        return NotImplemented

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(3 ,4)
print(v1 * 2)
print(0,5 * v1)
print(v1 / 4)
