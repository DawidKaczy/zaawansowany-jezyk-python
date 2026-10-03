class Color:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue


color1 = Color(red=255, green=100, blue=50)

print("Kolor:")
print("R:", color1.red)
print("G:", color1.green)
print("B:", color1.blue)