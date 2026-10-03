class DataSeries:
    def __init__(self, name, values):
        self.name = name
        self.values = list(values)

#__len__ długość obiektu
    def __len__(self):
        return len(self.values)

#__getitem__ indeksowanie i wycinki
    def __getitem__(self, index):
        if isinstance(index, slice):
            return DataSeries(self.name, self.values[index])
        return self.values[index]

#__setitem__ przypisanie po indeksie
    def __setitem__(self, index, value):
        self.values[index] = value

    def __repr__(self):
        return f"DataSeries(name='{self.name}', values={self.values})"

#__add__ operator +
    def __add__(self, other):
        if isinstance(other, DataSeries):
            if len(self.values) != len(other.values):
                raise ValueError("Serie muszą mieć tę samą długość")
            new_values = [a + b for a, b in zip(self.values, other.values)]
            return DataSeries(f"{self.name}+{other.name}", new_values)
        new_values = [v + other for v in self.values]
        return DataSeries(self.name, new_values)

#__sub__ (operator -)
    def __sub__(self, other):
        if isinstance(other, DataSeries):
            new_values = [a - b for a, b in zip(self.values, other.values)]
            return DataSeries(f"{self.name}-{other.name}", new_values)
        return DataSeries(self.name, [v - other for v in self.values])

#__mul__ (operator *)
    def __mul__(self, other):
        if isinstance(other, DataSeries):
            new_values = [a * b for a, b in zip(self.values, other.values)]
            return DataSeries(f"{self.name}*{other.name}", new_values)
        return DataSeries(self.name, [v * other for v in self.values])

#__radd__ operatory odwrócone (5 + series)
    def __radd__(self, other):
        return self.__add__(other)

##__rmul__ operatory odwrócone (5 * series)
    def __rmul__(self, other):
        return self.__mul__(other)

#__eq__ operator ==
    def __eq__(self, other):
        if not isinstance(other, DataSeries):
            return NotImplemented
        return self.name == other.name and self.values == other.values

#Metoda __contains__ definiuje zachowanie operatora in.
#Przydatna do sprawdzania, czy wartość istnieje w naszym zbiorze danych.
    def __contains__(self, item):
        return item in self.values

#Prostsza wersja __iter__ z generatorem
    def __iter__(self):
        for value in self.values:
            yield value


#__len__ — długość obiektu
s = DataSeries("scores", [88, 92, 75, 91])
print(len(s))      # 4

#__getitem__ — indeksowanie i wycinki
s = DataSeries("scores", [88, 92, 75, 91, 84])

print(s[0])      # 88
print(s[-1])     # 84
print(s[1:3])    # DataSeries(name='scores', values=[92, 75])

#__setitem__ — przypisanie po indeksie
s = DataSeries("scores", [88, 92, 75, 91])
s[2] = 99
print(s)

#__add__ operator +
a = DataSeries("x", [1, 2, 3])
b = DataSeries("y", [10, 20, 30])
print(b + a)    # DataSeries(name='x+y', values=[11, 22, 33])
print(a + 100)  # DataSeries(name='x', values=[101, 102, 103])

#__sub__ (operator -)
s = DataSeries("x", [10, 20, 30])
print(s - 5)    # DataSeries('x', [5, 15, 25])

#__mul__ (operator *)
s = DataSeries("x", [10, 20, 30])
print(s * 2)    # DataSeries('x', [20, 40, 60])

#__radd__ operatory odwrócone (5 + series)
s = DataSeries("x", [1, 2, 3])
print(10 + s)   # DataSeries('x', [11, 12, 13])

##__rmul__ operatory odwrócone (5 * series)
s = DataSeries("x", [1, 2, 3])
print(3 * s)    # DataSeries('x', [3, 6, 9])

#__eq__ — operator ==
s = DataSeries("x", [1, 2, 3])
z = DataSeries("x", [1, 2, 3])
print(s == z)

#Metoda __contains__ definiuje zachowanie operatora in.
#Przydatna do sprawdzania, czy wartość istnieje w naszym zbiorze danych.
s = DataSeries("temperatures", [36.6, 37.0, 36.8, 38.1])
print(37.0 in s)   # True
print(40.0 in s)   # False

#Prostsza wersja __iter__ z generatorem
s = DataSeries("scores", [88, 92, 75])
print(list(s))        # [88, 92, 75]
print(sum(s))         # 255
print(max(s))         # 92
print(min(s))         # 75
