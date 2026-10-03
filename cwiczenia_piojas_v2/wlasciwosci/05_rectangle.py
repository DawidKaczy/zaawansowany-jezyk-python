

class Rectangle:
    def __init__(self, width, height):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("width must be > 0")
        if height > 0:
            self.__height = height
        else:
            raise ValueError("height must be > 0")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("height must be > 0")

    @property
    def area(self):
        return self.__width * self.__height

v1 = Rectangle(2,3)

v1.width = 3

print(v1.area)