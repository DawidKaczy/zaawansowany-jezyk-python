from math import pi
from .foremka import Foremka

class ForemkaOkragla(Foremka):
    def __init__(self, material: str, srednica_mm: float, ksztalt: str = "okrągła"):
        super().__init__(material, ksztalt)
        self.srednica_mm = srednica_mm

    def pole(self) -> float:
        r = self.srednica_mm / 2
        return round(pi * r ** 2, 2)

    def obwod(self) -> float:
        return round(pi * self.srednica_mm, 2)

    def opis(self) -> str:
        base_desc = super().opis()
        return f"{base_desc}, Średnica: {self.srednica_mm} mm"