
def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


if __name__ == "__main__":
    print("--- Dzielniki liczby 36 ---")
    print(list(divisors(36)))

    print("\n--- Sprawdzanie liczby pierwszej ---")
    liczba = 17
    dzielniki_17 = list(divisors(liczba))

    print(f"Dzielniki {liczba}: {dzielniki_17}")

    if len(dzielniki_17) == 2:
        print(f"Wynik: Liczba {liczba} JEST liczbą pierwszą.")
    else:
        print(f"Wynik: Liczba {liczba} NIE JEST liczbą pierwszą.")