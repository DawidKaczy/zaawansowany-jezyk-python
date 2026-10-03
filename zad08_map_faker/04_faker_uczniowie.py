from faker import Faker
import random
faker = Faker()


oceny = []
for i in range(1000):
    oceny.append(random.randint(1, 6))

imiona = []
for i in range(1000):
    imiona.append(faker.first_name())

lista_ucz = list(zip(imiona, oceny))
print(lista_ucz)