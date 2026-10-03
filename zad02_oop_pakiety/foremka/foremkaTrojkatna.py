from math import sqrt
from .foremka import Foremka

class ForemkaTrojkatna(Foremka):
    def __init__(self, material: str, bok_mm: float, ksztalt: str = "Trójkąt równoboczny"):
        super().__init__(material, ksztalt)
        self.bok_mm = bok_mm

    def pole(self) -> float:
        # Pole trójkąta równobocznego: (a^2 * sqrt(3)) / 4
        return round((self.bok_mm ** 2 * sqrt(3)) / 4, 2)

    def obwod(self) -> float:
        return round(3 * self.bok_mm, 2)

    def opis(self) -> str:
        base_desc = super().opis()
        return f"{base_desc}, Bok: {self.bok_mm} mm"