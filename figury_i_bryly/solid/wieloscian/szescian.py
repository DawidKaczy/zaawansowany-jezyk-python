def pole_calkowite(a):
    """Oblicza pole powierzchni całkowitej sześcianu o boku a."""
    return 6 * a**2

def objetosc(a):
    """Oblicza objętość sześcianu o boku a."""
    return a**3

if __name__ == "__main__":
    print("--- Kalkulator: Sześcian ---")
    a = float(input("Podaj bok a: "))
    print(f"Pole: {pole_calkowite(a)} | Objętość: {objetosc(a)}")