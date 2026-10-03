

class Password:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value[0] + (len(self.__value) - 1) * "*"

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError("Password value must be string")
        if len(value.strip()) < 8:
            raise ValueError("Password value must be at least 8 characters")
        if not any(char.isupper() for char in value):
            raise ValueError("Password value must be at least one uppercase character")
        if not any(not char.isdigit() for char in value):
            raise ValueError("Password value must be at least one digit")
        self.__value = value

v1 = Password('PASSWORD')
print(v1.value)
v1.value = '<PASSWOR!D>'