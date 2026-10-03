class ShoppingList:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def __repr__(self):
        return f"ShoppingList<{self.owner}> {self.items}"

    def __str__(self):
        return f"ShoppingList{self.owner} {self.items}"


v1 = ShoppingList("Dawid")
v1.items.append("Klocki")

print(v1)