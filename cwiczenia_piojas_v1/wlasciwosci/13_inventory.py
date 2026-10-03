

class Inventory:
    def __init__(self, items: dict):
        self.__items = items


    @property
    def items(self):
        return self.__items.copy()

    @items.setter
    def items(self, items):
        if not isinstance(items, dict):
            raise TypeError('items must be a dictionary')
        for key, value in items.items():
            if not key:
                raise TypeError('items cannot be empty')
            if not isinstance(key, str):
                raise TypeError('key must be a string')
            if not isinstance(value, int):
                raise TypeError('value must be a int')
        self.__items = items


v1 = Inventory({'Chleb': 3, 'Jabłka': 1, 'Ogórki': 5, 'Kajzerki': 9,})
print(v1.items)
v1.items = {'Garnki': 10}
print(v1.items)