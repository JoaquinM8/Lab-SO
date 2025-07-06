n = int(input("Longitud del arreglo > "))
v = n*[0]
for i in range(n):
    v[i] = int(input("Ingresar elemento > "))

maxv = max(v)
maxvi = v.pop(v.index(max(v)))

print("El segundo mayor es", max(v))

v.insert(maxvi, maxvi)
