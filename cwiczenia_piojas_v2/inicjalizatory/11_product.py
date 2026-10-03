class Product:
    def __init__(self, name, price, tags: list = None):

        if not name.strip():
            raise ValueError("Nazwa produktu nie może być pustym ciągiem znaków.")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Cena musi być liczbą dodatnią.")

        self.name = name.strip()
        self.price = price  

        if tags is None:
            self.tags = []
        else:
            self.tags = list(tags)

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, tags={self.tags})"

try:
    p3 = Product(" a", 100, [""])
except ValueError as e:
    print(f"Błąd: {e}")

try:
    p4 = Product("Chleb", -5.50)
except ValueError as e:
    print(f"Błąd: {e}")