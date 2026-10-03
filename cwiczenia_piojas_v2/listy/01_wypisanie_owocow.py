fruits = ["jabłko", "banan", "śliwla", "jarzębina", "ananas"]

for fruit in fruits:
    print(fruit)

print("\n")
print(fruits[1])
print(fruits[-1])


temp = [2.0, 1.2, 0.3, 2.4]
temp_sorted = sorted(temp)
temp.sort(reverse=True)
print(temp_sorted)
print(temp)
