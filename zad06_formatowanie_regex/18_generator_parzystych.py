
def parzyste_do_n(n):
    for i in range(0, n + 1, 2):
        yield i


for x in parzyste_do_n(10):
    print(x)