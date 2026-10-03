import math
pi = 3.14159
def pole_calkowite(r, h):
    """
        Oblicza pole powierzchni całkowitej walca.

        Argumenty:
            r (float): Promień podstawy walca.
            h (float): Wysokość walca.

        Zwraca:
            float: Pole powierzchni całkowitej (Pc = 2πr² + 2πrh).
        """
    return 2 * pi * r**2 + 2 * pi * r * h

def objetosc(r, h):
    """
        Oblicza objętość walca.

        Argumenty:
            r (float): Promień podstawy walca.
            h (float): Wysokość walca.

        Zwraca:
            float: Objętość walca (V = πr²h).
        """
    return pi * r**2 * h

if __name__ == "__main__":
    print("--- Kalkulator: Walec ---")
    r = float(input("Podaj promień podstawy r: "))
    h = float(input("Podaj wysokość h: "))
    print(f"Pole: {pole_calkowite(r, h):.2f} | Objętość: {objetosc(r, h):.2f}")