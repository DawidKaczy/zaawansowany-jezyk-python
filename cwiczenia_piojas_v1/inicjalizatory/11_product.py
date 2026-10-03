class Product:
    def __init__(self, name, price, tags: list = None):
        if name == "":
            raise ValueError("Name cannot be an empty string")
        self.name = name
        if price < 0:
            raise ValueError("Price must be greater than 0")
        self.price = price
        self.tags = list(tags)

    def __repr__(self):
        return f"name: {self.name}, price: {self.price}, tags: {self.tags}"


v1 = Product("V1", 100, ["python"])

print(v1)