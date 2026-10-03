import array

arr = array.array('i', [1, 2, 3, 4, 5])
arr.append(6)
arr.append(7)
arr.extend([8, 9])
print(arr)
print(len(arr))
print(arr.itemsize)

lista = arr.tolist()
print(lista)