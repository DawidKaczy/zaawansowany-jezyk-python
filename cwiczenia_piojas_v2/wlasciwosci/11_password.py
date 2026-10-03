
class Password:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return "*" * len(self.__value)

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError("value must be str")
        if len(value) < 8:
            raise ValueError("password must be 8 characters long")
        if not any (char.isdigit() for char in value):
            raise TypeError("password must contain 1 digits")
        if not any(char.isupper() for char in value):
            raise TypeError("password must contain 1 uppercase letters")
        self.__value = value


v1 = Password("a1ctpsiA")
print(v1.value)
