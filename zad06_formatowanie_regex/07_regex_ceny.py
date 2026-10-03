import re

tekst = "Cena: 49.99 PLN, rabat: 10.50 PLN"
wzorzec = r"\d+\.\d+"

liczby = re.findall(wzorzec, tekst)

print(liczby)