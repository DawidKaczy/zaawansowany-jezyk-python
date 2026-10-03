

class Counter:
    def __init__(self, liczba):
        self.liczba = liczba

    def __add__(self, other):
        if not isinstance(other, Counter):
            raise TypeError
        return Counter(self.liczba + other.liczba)

    def __sub__(self, other):
        if not isinstance(other, Counter):
            raise TypeError
        return Counter(self.liczba - other.liczba)

    def __repr__(self):
        return f"({self.liczba})"

v1 = Counter(10)
v2 = Counter(20)
print(v1 - v2)

