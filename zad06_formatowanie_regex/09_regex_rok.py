import re

text = "Raport_2024 raport_2025 RAPORT_2026"
wzorzec = r"\d{4}"

print(re.findall(wzorzec, text))
