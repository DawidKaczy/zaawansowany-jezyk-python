import argparse

parser = argparse.ArgumentParser(description="Program wutajacy")
parser.add_argument("imie", help="imie uzytkownika")
args = parser.parse_args()
print(f"Witaj {args.imie}")