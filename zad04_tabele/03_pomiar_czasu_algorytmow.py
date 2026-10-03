import time as tm
from functools import wraps

def powtorz(n):
    def time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = tm.perf_counter()

            for _ in range(n):
                result = func(*args, **kwargs)

            end = tm.perf_counter()
            czas = end - start

            print(f'{func.__name__} took {czas:.2f} seconds')
            return result
        return wrapper
    return time

@powtorz(100000)
def alg1(a, n):
    def power(a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            polowa = power(a, n // 2)
            return polowa * polowa
        else:
            return a * power(a, n - 1)
    return power(a, n)


@powtorz(100000)
def alg2(a, n):
    wynik = 1
    i = 1
    while i <= n:
        wynik = wynik * a
        i = i + 1
    return wynik


@powtorz(1)
def alg3(a, n):
    def power(a, n):
        if n == 0:
            return 1
        else:
            return a * power(a, n - 1)
    return power(a, n)

def algo1(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        polowa = algo1(a, n//2)
        return polowa * polowa
    else:
        return a * algo1(a, n-1)


if __name__ == '__main__':

    print(alg1(100, 100))
    print(alg2(100, 100))
    print(alg3(100, 100))
