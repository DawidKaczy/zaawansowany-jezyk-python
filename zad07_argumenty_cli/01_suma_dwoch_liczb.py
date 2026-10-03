import sys
if len(sys.argv) != 3:
    sys.exit("er")
try:
    suma = int(sys.argv[1]) + int(sys.argv[2])
    print(suma)
except ValueError:
    sys.exit("er")