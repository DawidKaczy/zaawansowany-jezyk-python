

class Matrix:
    def __init__(self, data: list[list]):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, list):
            raise TypeError("To musi być lista")
        if not data:
            raise ValueError("Macierz nie może być pusta.")
        if not isinstance(data[0], list):
            raise TypeError("Każdy wiersz macierzy musi być listą.")
        for row in data:
            if len(data) != len(row):
                raise ValueError("Matrix musi miec taką sama długośc wierszy")
            if not isinstance(row, list):
                raise TypeError("Każdy wiersz macierzy musi być listą.")
            for item in row:
                if type(item) not in (int, float):
                    raise TypeError("Elementy macierzy muszą być typu int lub float.")
        self.__data = data



