import math
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        if length == 0:
            raise ValueError("Nie można znormalizować wektora zerowego")
        return Vector2D(self.x / length, self.y / length)

    def dot_product(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: "Vector2D") -> float:
        len1 = self.length()
        len2 = other.length()

        if len1 == 0 or len2 == 0:
            raise ValueError("Nie można obliczyć kąta z wektorem zerowym")

        dot = self.dot_product(other)
        cos_theta = dot / (len1 * len2)

        cos_theta = max(-1, min(1, cos_theta))

        angle_rad = math.acos(cos_theta)
        return math.degrees(angle_rad)