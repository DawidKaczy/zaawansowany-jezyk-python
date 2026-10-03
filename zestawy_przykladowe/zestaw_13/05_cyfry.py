
def digits(n):
    for i in str(n):
        yield int(i)


print(list(digits(78652)))

if sum(list(digits(12345))) % 3 == 0:
    print("Jest podzielna")
else:
    print("nie jest podzielna")