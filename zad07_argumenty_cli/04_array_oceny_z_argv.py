import sys
import array

arg = sys.argv[1:]
if not arg:
    sys.exit(1)

try:
    oceny = array.array('i', [int(arg[0]) for arg in arg])
    print(oceny)
    lista = oceny.tolist()
    print(lista)
    print(f"średnia = {sum(lista)/len(lista)}")
    print(f"max = {max(lista)}")
    print(f"min = {min(lista)}")

except ValueError:
    sys.exit(1)