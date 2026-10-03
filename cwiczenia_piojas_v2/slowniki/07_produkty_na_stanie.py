inventory = {"apples": 10, "bananas": 0, "cherries": 5, "dates": 0}

in_stock = {key: value for key, value in inventory.items() if value > 0}
print(in_stock)
