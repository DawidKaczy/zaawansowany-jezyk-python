import argparse
import sys

p = argparse.ArgumentParser()
p.add_argument("oceny", type=float, nargs='*')
p.add_argument("--srednia", action="store_true")
p.add_argument("--min", action="store_true")
p.add_argument("--max", action="store_true")
p.add_argument("--lista", action="store_true")

args = p.parse_args()

if not args.oceny:
    sys.exit(0)

for ocena in args.oceny:
    if ocena < 2.0 or ocena > 5.0:
        print(f"Błąd: Ocena {ocena} jest spoza zakresu od 2 do 5.")
        sys.exit(1)

if args.srednia:
    print(f"srednia = {sum(args.oceny) / len(args.oceny)}")

if args.min:
    print(f"min = {min(args.oceny)}")

if args.max:
    print(f"max = {max(args.oceny)}")

if args.lista:
    print(f"Lista ocen: {args.oceny}")