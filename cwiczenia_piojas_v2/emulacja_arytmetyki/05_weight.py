


class Weight:
    def __init__(self, kg):
        if type(kg) not in (int, float):
            raise TypeError
        self.kg = kg

    def __add__(self, other):
        if isinstance(other, Weight):
            return Weight(self.kg + other.kg)
        if type(other) in (int, float):
            return Weight(self.kg + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Weight):
            return Weight(self.kg - other.kg)
        if type(other) in (int, float):
            return Weight(self.kg - other)
        return NotImplemented


    def __repr__(self):
        return f"Weight({self.kg})"

v1 = Weight(10)
v2 = Weight(25)
print(v1 + 10.0)
print(v1 - v2)