

class BankAccount:
    def __init__(self, balance):
        if type(balance) not in (int, float):
            raise TypeError("Balance must be a number")
        self.balance = balance

    def __iadd__(self, other):
        if type(other) not in (int, float):
            return NotImplemented
        if other <= 0:
            raise ValueError("Kwota wpłaty musi być większa od zera.")

        # Modyfikacja w miejscu
        self.balance += other

        # ZŁOTA ZASADA OPERATORÓW IN-PLACE: Zawsze zwracaj self!
        return self

    def __repr__(self):
        return f"BankAccount(balance={self.balance:.2f} PLN)"
moje_konto = BankAccount(500)
print(f"Stan początkowy: {moje_konto}")

# Używamy operatora += (uruchamia __iadd__)
moje_konto += 200
print(f"Po wpłacie 200:  {moje_konto}")