import re

files = ["data.csv", "report.pdf", "sales.xlsx", "model.pkl"]
wzorzec = r"\.(csv|xlsx)$"

przefiltrowane_pliki = [plik for plik in files if re.search(wzorzec, plik)]

print(przefiltrowane_pliki)