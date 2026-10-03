
def process_numbers(numbers, condition, transform):
    return [transform(x) for x in numbers if condition(x)]

lista = [-5, -2, 0, 3, 7, 10, 15, 22]
condition = lambda x: x > 0
transform = lambda x: x**2

print(process_numbers(lista, condition, transform))

lista2 = [-5, -2, 0, 3, 7, 10, 15, 22]
condition2 = lambda x: x < 0
transform2 = lambda x: abs(x) + 100

print(process_numbers(lista2, condition2, transform2))

lista3 = [-5, -2, 0, 3, 7, 10, 15, 22]
condition3 = lambda x: x  % 2 == 0
transform3 = lambda x: x / 2

print(process_numbers(lista3, condition3, transform3))