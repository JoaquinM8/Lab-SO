n = int(input("Longitud del arreglo > "))
v = n*[0]
for i in range(n):
    v[i] = int(input("Ingresar elemento > "))

dv = n*[0]
for i in range(n):
    dv[i] = v[i-1]
print(dv)