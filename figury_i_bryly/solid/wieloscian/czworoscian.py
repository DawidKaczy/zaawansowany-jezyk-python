import math

def pole_calkowite(a):
    """Oblicza pole powierzchni całkowitej czworościanu foremnego (a^2 * sqrt(3))."""
    return math.sqrt(3) * a**2

def objetosc(a):
    """Oblicza objętość czworościanu foremnego ((a^3 * sqrt(2)) / 12)."""
    return a**3 / (6 * math.sqrt(2))

if __name__ == "__main__":
    print("--- Kalkulator: Czworościan Foremny ---")
    a = float(input("Podaj krawędź a: "))
    print(f"Pole: {pole_calkowite(a):.2f} | Objętość: {objetosc(a):.2f}")