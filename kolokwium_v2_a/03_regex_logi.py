import re

with open("logs.txt", "r", encoding="utf-8") as f:
    linie = f.readlines()

print("--- ERRORY ---")
for linia in linie:
    if "ERROR" in linia:
        print(linia.strip())

print("\n--- DATY ---")
for linia in linie:
    daty = re.findall(r"\d{4}-\d{2}-\d{2}", linia)
    if daty:
        print(daty[0])

print("\n--- GODZINY ---")
for linia in linie:
    godziny = re.findall(r"\d{2}:\d{2}:\d{2}", linia)
    if godziny:
        print(godziny[0])

print("\n--- POZIOM KOMUNIKATU ---")
for linia in linie:
    poziomy = re.findall(r"\d{2}:\d{2}:\d{2}\s+([A-Z]+)", linia)
    if poziomy:
        print(poziomy[0])

print("\n--- TREŚĆ KOMUNIKATU ---")
for linia in linie:
    tresci = re.findall(r"\d{2}:\d{2}:\d{2}\s+[A-Z]+\s+(.*)", linia.strip())
    if tresci:
        print(tresci[0])