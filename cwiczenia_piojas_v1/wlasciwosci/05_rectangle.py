
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = width


v1 = Rectangle(2,3)

print(v1.area)