import re

info = "PIOTR   Wiśniewski(ur.2000)"

info = re.sub(r"\(ur\.\d{4}\)", "", info)

info = re.sub(r"\s+", " ", info)

info = info.strip().title()

print(info)