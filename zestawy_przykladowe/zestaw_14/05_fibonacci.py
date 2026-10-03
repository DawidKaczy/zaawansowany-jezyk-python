def fibonacci_up_to(n):
    a, b = 0, 1

    while a <= n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("--- Ciąg Fibonacciego do 100 ---")
    fib_100 = list(fibonacci_up_to(100))
    print(f"Wynik: {fib_100}")

    print("\n--- Sprawdzanie przynależności liczby 21 ---")
    szukana_liczba = 21

    if szukana_liczba in fibonacci_up_to(szukana_liczba):
        print(f"Wynik: Tak, liczba {szukana_liczba} należy do ciągu Fibonacciego.")
    else:
        print(f"Wynik: Nie, liczba {szukana_liczba} nie należy do ciągu Fibonacciego.")