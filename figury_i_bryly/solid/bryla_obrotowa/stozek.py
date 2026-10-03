import math

pi = 3.14159

def pole_calkowite(r, h):
    """
    Oblicza pole powierzchni całkowitej stożka.

    Argumenty:
    r (float): promień podstawy stożka
    h (float): wysokość stożka

    Zwraca:
    float: pole powierzchni całkowitej
    """
    l = math.sqrt(r**2 + h**2)  # tworząca stożka
    return pi * r**2 + pi * r * l

def objetosc(r, h):
    """
    Oblicza objętość stożka.

    Argumenty:
    r (float): promień podstawy stożka
    h (float): wysokość stożka

    Zwraca:
    float: objętość stożka
    """
    return (1/3) * pi * r**2 * h

if __name__ == "__main__":
    print("--- Kalkulator: Stożek ---")
    r = float(input("Podaj promień r: "))
    h = float(input("Podaj wysokość h: "))
    print(f"Pole: {pole_calkowite(r, h):.2f} | Objętość: {objetosc(r, h):.2f}")