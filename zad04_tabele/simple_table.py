import numpy as np

class SimpleTable():
    def __init__(self, data):
        self.data = np.array(data)

    def shapev1(func):
        def wrapper(self, *args):
            print(f"Shape przed: {self.shape}")

            wynik = func(self, *args)

            print(f"Shape po: {self.shape}")
            return wynik

        return wrapper

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def shape(self):
        return self.data.shape

    @shapev1
    def add_row(self, row):
        self._data = np.vstack([self._data, row])

    @shapev1
    def add_column(self, column):
        self._data = np.column_stack((self._data, column))


    def wyswietla(self):
        print(self._data)

    @shapev1
    def insert_column(self, index, column):
        if len(column) != self.shape[0]:
            raise ValueError(f"Kolumna musi mieć {self.shape[0]} elementów!")
        self._data = np.insert(self._data, index, column, axis=1)

    @shapev1
    def insert_row(self, index, row):
        if len(row) != self.shape[1]:
            raise ValueError(f"Wiersz musi mieć {self.shape[1]} elementów!")
        self._data = np.insert(self._data, index, row, axis=0)

if __name__ == '__main__':
    d1 = SimpleTable([[1, 2, 3],
                      [4, 5, 6]])


    d1.wyswietla()
    print(f"shape: {d1.shape} \n")

    d1.add_column([10, 2])
    d1.wyswietla()
    print(f"shape: {d1.shape} \n")

    d1.add_row([10,10,10,10])
    d1.wyswietla()
    print(f"shape: {d1.shape} \n")

    d1.insert_column(0, [10,10,10])
    d1.wyswietla()
    print(f"shape: {d1.shape} \n")

    d1.insert_row(1, [1,1,1,1,1])
    d1.wyswietla()
    print(f"shape: {d1.shape} \n")


