prices = {"milk": 3.50, "bread": 2.00, "eggs": 5.99, "butter": 4.25}

for key, value in prices.items():
    if value > 3.0:
        print(key, value)