

class RGBColor:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def red(self):
        return self.__red
    @property
    def green(self):
        return self.__green
    @property
    def blue(self):
        return self.__blue
    @red.setter
    def red(self, value):
        if not 0 <= value <= 255:
            raise ValueError("Red value must be between 0 and 255")
        self.__red = value
    @green.setter
    def green(self, value):
        if not 0 <= value <= 255:
            raise ValueError("Green value must be between 0 and 255")
        self.__green = value
    @blue.setter
    def blue(self, value):
        if not 0 <= value <= 255:
            raise ValueError("Blue value must be between 0 and 255")
        self.__blue = value

    @property
    def hex(self):
        return f"#{self.__red:02x}{self.__green:02x}{self.__blue:02x}"

v1 = RGBColor(255, 0, 0)
print(v1.red, v1.green, v1.blue)
v1.red = 0
v1.green = 55
print(v1.red, v1.green, v1.blue)
print(v1.hex)