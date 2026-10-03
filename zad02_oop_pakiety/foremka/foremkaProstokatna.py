from .foremka import Foremka

class ForemkaProstokatna(Foremka):
    def __init__(self, material: str, a_mm: float, b_mm: float, ksztalt: str = "Prostokątna"):
        super().__init__(material, ksztalt)
        self.a_mm = a_mm
        self.b_mm = b_mm

    def pole(self) -> float:
        return self.a_mm * self.b_mm

    def obwod(self) -> float:
        return 2 * (self.a_mm + self.b_mm)

    def opis(self) -> str:
        base_desc = super().opis()
        return f"{base_desc}, Wymiary: {self.a_mm} x {self.b_mm} mm"

