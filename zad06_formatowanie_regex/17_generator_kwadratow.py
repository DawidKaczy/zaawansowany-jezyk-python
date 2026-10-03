def kwadraty_do_n(n):
    for i in range(1, n + 1):
        yield i ** 2


for x in kwadraty_do_n(5):
    print(x)