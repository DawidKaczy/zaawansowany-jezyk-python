

class Matrix1D:
    def __init__(self, lista):
        if not isinstance(lista, list):
            raise TypeError("Matrix must be of type list")
        for i in lista:
            if type(i) not in (int, float):
                raise TypeError("Matrix must be of type int or float")
        self.lista = lista


    def __mul__(self, other):
        if isinstance(other, Matrix1D):
            new_values = [a * b for a, b in zip(self.lista, other.lista)]
            return Matrix1D(new_values)
        if type(other) in (int, float):
            new_values = [a * other for a in self.lista]
            return Matrix1D(new_values)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)




    def __repr__(self):
        return str(self.lista)


v1 = Matrix1D([1,2,3])
print(v1*2)
print(2*v1)

