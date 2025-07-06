n = int(input("Longitud del arreglo > "))
v1 = n*[0]
for i in range(n):
    v1[i] = int(input("Ingresar elemento > "))

n = int(input("Longitud del arreglo > "))
v2 = n*[0]
for i in range(n):
    v2[i] = int(input("Ingresar elemento > "))

v3 = v1+v2
print(v3)