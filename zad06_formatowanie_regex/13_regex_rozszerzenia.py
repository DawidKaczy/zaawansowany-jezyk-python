import re

all_files = ["notes.txt", "data.csv", "image.png", "report.xlsx", "archive.parquet"]

rozszerzenia = ["csv", "xlsx", "parquet"]

wzorzec = rf"\.({'|'.join(rozszerzenia)})$"

pliki_danych = [plik for plik in all_files if re.search(wzorzec, plik)]

print(f"Zbudowany wzorzec: {wzorzec}")
print(f"Pliki danych:      {pliki_danych}")