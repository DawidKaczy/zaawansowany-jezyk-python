from bigInt.bigInt import BigInt

a = BigInt("100")
b = BigInt("20")
c = BigInt("5")

print("a + b =", a + b)
print("a - b =", a - b)
print("b * c =", b * c)

print("a += b ->", a)
print("a -= c ->", a)
print("a *= c ->", a)

x = BigInt("50")
y = BigInt("50")

print("x == y:", x == y)
print("x != z:", x != x)
print("x > z:", x > y)
print("z < x:", y < x)
print("x >= y:", x >= y)
print("z <= x:", x <= x)