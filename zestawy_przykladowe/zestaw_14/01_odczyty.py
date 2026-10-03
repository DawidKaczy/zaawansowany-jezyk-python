

def process_readings(readings, condition, transform):
    return [transform(x) for x in readings if condition(x)]


lista = [0.5, 1.2, 3.4, 5.0, 7.8, 10.5, 15.0, 22.3]

condition = lambda x: x>5
transform = lambda x: x*0.8

print(process_readings(lista, condition, transform))

condition2 = lambda x: x<2
transform2 = lambda x: round(x)

print(process_readings(lista, condition2, transform2))

condition3 = lambda x: (2 <= x <= 10)
transform3 = lambda x: x*2

print(process_readings(lista, condition3, transform3))