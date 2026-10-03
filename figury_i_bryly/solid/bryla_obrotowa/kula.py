pi = 3.14159

def pole_calkowite(r):
    """Oblicza pole powierzchni całkowitej kuli dla danego promienia r."""
    return 4 * pi * r**2


def objetosc(r):
    """Oblicza objętość kuli dla danego promienia r."""
    return (4/3) * pi * r**3

if __name__ == "__main__":
    print("--- Kalkulator: Kula ---")
    r = float(input("Podaj promień r: "))
    print(f"Pole: {pole_calkowite(r):.2f} | Objętość: {objetosc(r):.2f}")