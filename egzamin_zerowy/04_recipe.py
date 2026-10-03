

class Recipe:
    def __init__(self, flour, sugar, butter):
        self.flour = flour
        self.sugar = sugar
        self.butter = butter


    def __mul__(self, other):
        return Recipe(
            flour  = self.flour * other,
            sugar = self.sugar * other,
            butter = self.butter * other
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError
        return Recipe(
            flour  = self.flour / other,
            sugar = self.sugar / other,
            butter = self.butter / other
        )



    def __repr__(self):
        return f"Recipe(flour={self.flour}, sugar={self.sugar}, butter={self.butter})"


v1 = Recipe(50,50,50)
print(v1 * 2)
print(3 * v1)
print(v1 / 2)
