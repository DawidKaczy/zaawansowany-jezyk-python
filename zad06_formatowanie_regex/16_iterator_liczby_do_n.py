class LiczbyDoN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Przykład użycia
for liczba in LiczbyDoN(3):
    print(liczba)