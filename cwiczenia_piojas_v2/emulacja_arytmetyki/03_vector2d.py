

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return

    def __repr__(self):
        return f"({self.x}, {self.y})"

v1 = Vector2D(1,4)
print(v1 * 3)

