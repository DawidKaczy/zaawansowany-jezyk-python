

class ColorPalette:
    def __init__(self, palette):
        self.palette = palette


    def __getitem__(self, item):
        return self.palette[item]


    def __setitem__(self, key, value):
        self.palette[key] = value

    def __repr__(self):
        return repr(self.palette)


v1 = ColorPalette(["red", "green", "blue"])
ostatni = v1[-1]

v1[1] = "klocek"

print(v1)