import sys

if len(sys.argv) != 4:
    sys.exit("Długość 3")

try:
    a = float(sys.argv[1])
    op = sys.argv[2]
    b = float(sys.argv[3])

    if op == "+": result = a + b
    elif op == "-": result = a - b
    elif op == "*": result = a * b
    elif op == "/": result = a / b
    else: raise ValueError

    print(result)
except Exception:
    print("Błąd niepoprawna liczba lub znak")


