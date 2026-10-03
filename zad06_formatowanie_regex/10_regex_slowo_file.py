import re

log = "ERROR: file not found at /data/input.csv"
wzorzec = r"\bfile\b"

print(re.findall(wzorzec, log))