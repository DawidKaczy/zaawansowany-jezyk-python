import re

record = "  Jan Kowalski  (ur. 1990) "
wzorzec = r"\(ur\. \d{4}\)"

wynik = re.sub(wzorzec, "", record)

print(f"Oryginał: '{record}'")
print(f"Wynik:    '{wynik}'")