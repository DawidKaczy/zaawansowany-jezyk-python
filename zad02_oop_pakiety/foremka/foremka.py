class Foremka:
    def __init__(self, material: str, ksztalt: str):
        self.material = material
        self.ksztalt = ksztalt

    def pole(self) -> float:
        pass

    def obwod(self) -> float:
        pass

    def wykroj(self ) -> str:
        return "Wykrojono kawałek ciasta"

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}"



