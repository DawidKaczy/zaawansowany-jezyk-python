from vector.vector3D import Vector3D

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
v3 = Vector3D(0, 0, 0)

print(v1)


print("Dodawanie:", v1 + v2)

print("Odejmowanie:", v1 - v2)

print("Długość v1:", v1.length())
print("len(v1):", len(v1))

print("v1 == v2:", v1 == v2)
print("v1 != v2:", v1 != v2)
print("v1 > v2:", v1 > v2)
print("v1 < v2:", v1 < v2)

print("bool(v1):", bool(v1))
print("bool(v3):", bool(v3))