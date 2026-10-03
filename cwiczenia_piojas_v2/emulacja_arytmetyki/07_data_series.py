

class DataSeries:
    def __init__(self, lista):
        if not isinstance(lista, list):
            raise TypeError
        for i in lista:
            if type(i) not in (int, float):
                raise TypeError
        self.lista = lista


    def __add__(self, other):
        if len(self.lista) != len(other.lista):
            raise ValueError("Muszą być tej samej długości")
        if not isinstance(other, DataSeries):
            raise TypeError("Nie są tej same dane")
        new_values = [a + b for a, b in zip(self.lista, other.lista)]
        return DataSeries(new_values)


    def __repr__(self):
        return str(self.lista)

v1 = DataSeries([1, 2, 3])
v2 = DataSeries([4, 5, 3])
print(v1 + v2)
