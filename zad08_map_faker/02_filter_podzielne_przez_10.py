import random

lista = []
for i in range(1000):
    lista.append(random.randint(1, 100))

podzielne10 = list(filter(lambda x: x % 10 == 0, lista))
print(podzielne10)
