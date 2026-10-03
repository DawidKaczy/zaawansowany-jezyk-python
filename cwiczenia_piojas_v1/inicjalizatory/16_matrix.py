
class Matrix:
    def __init__(self, data):
        self.row = len(data)
        self.col = len(data[0])
        if data:
            for row in data:
                if len(row) != len(data[0]):
                    raise ValueError("Data must be of the same length")
        self.data = data

    def __str__(self):
        wynik = ""
        for row in self.data:
            wynik += str(row) + "\n"
        return wynik

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) == len(other.data) and any(len(r1) == len(r2) for r1, r2 in zip(self.data, other.data)):
                new_values = [[a + b for a, b in zip(r1, r2)]for r1, r2 in zip(self.data, other.data)]
                return Matrix(new_values)
            else:
                raise ValueError("Data must be of the same length")
        return Matrix([[a + other for a in row] for row in self.data])


    def __eq__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) == len(other.data) and any(len(r1) == len(r2) for r1, r2 in zip(self.data, other.data)):
                value = [[a == b for a, b in zip(r1, r2)] for r1, r2 in zip(self.data, other.data)]
                return Matrix(value)
            else:
                raise ValueError("Data must be of the same length")
        return Matrix([[a == other for a in row] for row in self.data])

    def __radd__(self, other):
        return self.__add__(other)

matrix = [[1,2,3],
          [3,4,5]]

matrixv2 = [[1,2],
            [3,4]]

v1 = Matrix(matrix)
v2 = Matrix(matrixv2)
print(v1.row)   #2
print(v1.col)   #3
print(v1)       #[1, 2, 3]
                #[3, 4, 5]


print(5 + v1)   #[6, 7, 8]
                #[8, 9, 10]

print(v1 == 5)  #[False, False, False]
                #[False, False, True]