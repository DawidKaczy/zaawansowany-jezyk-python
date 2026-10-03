
class Email:
    def __init__(self, address):
        self.__address = address


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string")
        if address.count('@') != 1:
            raise ValueError("Address must contain @")
        local_part, domain_part = address.split('@')
        if '.' not in domain_part:
            raise ValueError("Address must contain @")
        self.__address = address

v1 = Email("<EMAIL>")
v1.address = "koralik@.pl"
print(v1.address)
