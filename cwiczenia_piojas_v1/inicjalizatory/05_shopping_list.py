class ShoppingList:
    def __init__(self, owner):
        self.owner = owner
        self.items = []



list1 = ShoppingList("Jan")

list1.items.append("chleb")
list1.items.append("mleko")

print("Właściciel:", list1.owner)
print("Lista zakupów:", list1.items)