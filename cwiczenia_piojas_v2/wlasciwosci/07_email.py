

class Email:
    def __init__(self, address):
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError('The address must be a string')
        if address.count('@') != 1:
            raise ValueError("Adres email musi zawierać dokładnie jeden znak '@'.")
        local_part, domain_part = address.split('@')
        if "." not in domain_part:
            raise TypeError('The email address must be a valid email address')
        self.__address = address

v1 = Email("okok@wp.pl")
print(v1.address)

