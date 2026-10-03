import argparse

p = argparse.ArgumentParser()
p.add_argument('liczba', type = int)
p.add_argument('--desc', action = 'store_true')
args = p.parse_args()

wynik = args.liczba ** 2
if args.desc:
    print(f"Liczę kwadrat liczby {args.liczba} \n Wynik: {wynik}")
else:
    print(wynik)