from functools import partial

def power(pod, wyk):
    return pod ** wyk

square= partial(power, wyk = 2)

cube= partial(power, wyk = 3)

wynik = square(5)
wynik2 = cube(3)

print(wynik)
print(wynik2)

