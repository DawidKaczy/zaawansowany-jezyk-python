from functools import total_ordering

@total_ordering
class DataPoint:
    def __init__(self, label, value):
        self.label = label
        self.value = value

# __eq__ definiuje ==
    def __eq__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.value == other.value

#__lt__ definiuje <
    def __lt__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.value < other.value

#__le__ definiuje <=
    def __le__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.value <= other.value

    def __repr__(self):
        return f"DataPoint('{self.label}', {self.value})"

pointv1 = DataPoint("c", 30)
pointv2 = DataPoint("b", 30)
#__eq__ definiuje ==
print(pointv1 == pointv2)

#__lt__ definiuje <
print(pointv1 < pointv2)

#__le__ definiuje <=
print(pointv1 <= pointv2)

print(pointv1 >= pointv2)  # False  — wygenerowane automatycznie!
print(pointv1 != pointv2)  # True   — wygenerowane automatycznie!

