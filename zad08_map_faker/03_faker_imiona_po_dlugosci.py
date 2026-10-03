from faker import Faker
faker = Faker()

imiona = []
for i in range(1000):
    imiona.append(faker.first_name())

print(imiona)
posortowane = list(sorted(imiona, key=lambda imie: len(imie)))
print(posortowane)