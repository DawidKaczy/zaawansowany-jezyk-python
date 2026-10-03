

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, str):
            raise TypeError("owner must be a string")
        clean_owner = owner.strip()
        if not clean_owner:
            raise ValueError("Imię właściciela nie może być puste.")
        if len(clean_owner) < 2:
            raise ValueError("Imię właściciela musi składać się z co najmniej 2 znaków.")
        self.__owner = clean_owner


v1 = BankAccount("        d   a", 12)

print(v1.owner)