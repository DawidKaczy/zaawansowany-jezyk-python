

def process_temperatures(temps, condition, transform):
    return [transform(x) for x in temps if condition(x)]


lista = [-15.5, -3.0, 0.0, 5.5, 18.2, 25.0, 32.5, 40.0]
condition = lambda x: x > 20
transform = lambda x: x * 9/5 +32

print(process_temperatures(lista, condition, transform))

condition2 = lambda x: x < 0
transform2 = lambda x: abs(x)

print(process_temperatures(lista, condition2, transform2))

condition3 = lambda x: 0 <= x <= 30
transform3 = lambda x: round(x)

print(process_temperatures(lista, condition3, transform3))
