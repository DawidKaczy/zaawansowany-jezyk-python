studenci = [
    ("Anna", "Kowalska", 91),
    ("Jan", "Nowak", 64),
    ("Ola", "Wiśniewska", 78),
    ("Piotr", "Zieliński", 45),
    ("Maria", "Wójcik", 100),
    ("Tomasz", "Lewandowski", 33),
]

oceny = list(map(
    lambda x: 2.0
    if x[2] <= 49 else 3.0
    if x[2] <= 64 else 3.5
    if x[2] <= 74 else 4.0 
    if x[2] <= 84 else 4.5
    if x[2] <= 94 else 5.0,
    studenci
))

zaliczeni = list(filter(lambda x: x[2] >= 50, studenci))

posortowani = sorted(studenci, key=lambda x: x[2], reverse=True)

pary = list(zip(map(lambda x: f"{x[0]} {x[1]}", studenci), oceny))

print(oceny)
print(zaliczeni)
print(posortowani)
print(pary)