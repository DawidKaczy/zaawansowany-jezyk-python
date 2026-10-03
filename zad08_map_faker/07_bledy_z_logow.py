error_lines = []

with open('logs.csv', 'r', encoding='utf-8') as file:
    for line in file:
        if "ERROR" in line:
            error_lines.append(line.strip())

for line in error_lines:
    print(line)