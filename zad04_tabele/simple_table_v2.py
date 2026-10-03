class SimpleTableV2:
    __slots__ = ['data']
    def __init__(self, data):

        if data:
            row_length = len(data[0])
            for row in data:
                if len(row) != row_length:
                    raise ValueError("Wszystkie wiersze muszą mieć tę samą długość")
        self.data = data

    def shape(func):
        def wrapper(self, *args):
            ilosc_kolumn = len(self.data[0])
            ilosc_wierszy = len(self.data)
            wynik = func(self, *args)
            print(f"Ilość kolumn: {ilosc_kolumn} \nIlość wierszy: {ilosc_wierszy}")
            return wynik
        return wrapper

    @shape
    def __str__(self):
        wynik = ""
        for row in self.data:
            wynik += str(row) + "\n"
        return wynik

    def __del__(self):
        self.data.clear()

    def add_row(self, row):
        if len(self.data[0]) == len(row):
            self.data.append(row)
        else:
            raise ValueError("Wszystkie wiersze muszą mieć tę samą długość")

    def add_column(self, column):
        if len(self.data) == len(column):
            for i in range(len(self.data)):
                self.data[i].append(column[i])
        else:
            raise ValueError("Liczba elementów kolumny musi odpowiadać liczbie wierszy")

if __name__ == '__main__':

    d1 = SimpleTableV2([[1, 2, 3, 6],
                        [7, 8, 9, 10],
                        [11, 12, 13, 14],
                        [11, 12, 13, 14]])

    d2 = SimpleTableV2([[11, 12, 13, 14],
                        [1, 2, 3, 6],
                        [7, 8, 9, 10]])

    print(str(d1))
    print(str(d2))
    del d1
    d2.add_row([1, 2, 3, 6])
    print(str(d2))
    d2.add_column([11, 12, 13, 14])
    print(str(d2))
