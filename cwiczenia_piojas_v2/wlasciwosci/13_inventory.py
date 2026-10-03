

class Inventory:
    def __init__(self, items):
        self.items = items

    @property
    def items(self):
        return self.__items.copy()

    @items.setter
    def items(self, items):
        if not isinstance(items, dict):
            raise TypeError("value must be dict")
        for key, value in items.items():
            if not isinstance(key, str):
                raise TypeError("key must be str")
            if not key.strip():
                raise ValueError("key must not be empty")
            if type(value) is not int:
                raise TypeError("value must be int")
            if value < 0:
                raise ValueError("value must be positive")
        self.__items = items.copy()


v1 = Inventory({"f": 1})



