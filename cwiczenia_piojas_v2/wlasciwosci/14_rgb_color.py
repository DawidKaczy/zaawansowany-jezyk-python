

class RGBColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__r

    @r.setter
    def r(self, r):
        if type(r) != int:
            raise TypeError("R must be int")
        if not (0 <= r <= 255):
            raise TypeError("R must be between 0 and 255")
        self.__r = r

    @g.setter
    def g(self, g):
        if type(g) != int:
            raise TypeError("R must be int")
        if not (0 <= g <= 255):
            raise TypeError("R must be between 0 and 255")
        self.__g = g

    @b.setter
    def b(self, b):
        if type(b) != int:
            raise TypeError("R must be int")
        if not (0 <= b <= 255):
            raise TypeError("R must be between 0 and 255")
        self.__b = b

    @property
    def hex(self):
        return f"#{self.__r:02x}{self.__g:02x}{self.__b:02x}"



v1 = RGBColor(255, 0, 12)
print(v1.hex)





