import math

def pole_calkowite(a):
    """ok"""
    return 2 * math.sqrt(3) * a**2

def objetosc(a):
    """okok"""
    return (math.sqrt(2)/3) * a**3

if __name__ == "__main__":
    print("--- Kalkulator: Ośmiościan Foremny ---")
    a = float(input("Podaj krawędź a: "))
    print(f"Pole: {pole_calkowite(a):.2f} | Objętość: {objetosc(a):.2f}")