

def multiples_up_to(n, limit):
    for i in range(n, limit + 1, n):
        yield i


if __name__ == "__main__":
    print("--- Wielokrotności liczby 7 do 100 ---")
    wielokrotnosci_7 = list(multiples_up_to(7, 100))
    print(f"Wynik: {wielokrotnosci_7}")

    print("\n--- Sprawdzanie, czy 84 jest wielokrotnością 7 ---")
    szukana_liczba = 84

    if szukana_liczba in multiples_up_to(7, 100):
        print(f"Wynik: Tak, liczba {szukana_liczba} znajduje się wśród wygenerowanych wielokrotności.")
    else:
        print(f"Wynik: Nie, liczba {szukana_liczba} nie jest wielokrotnością.")




