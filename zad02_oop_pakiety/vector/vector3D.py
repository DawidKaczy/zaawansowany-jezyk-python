import math
from .vector2D import Vector2D

class Vector3D(Vector2D):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __len__(self):
        return int(self.length())

    def __eq__(self, other: "Vector3D") -> bool:
        return self.length() == other.length()

    def __ne__(self, other: "Vector3D") -> bool:
        return self.length() != other.length()

    def __lt__(self, other: "Vector3D") -> bool:
        return self.length() < other.length()

    def __le__(self, other: "Vector3D") -> bool:
        return self.length() <= other.length()

    def __gt__(self, other: "Vector3D") -> bool:
        return self.length() > other.length()

    def __ge__(self, other: "Vector3D") -> bool:
        return self.length() >= other.length()

    def __bool__(self):
        return self.length() != 0

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()