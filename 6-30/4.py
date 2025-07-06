n = int(input("Longitud del arreglo > "))
v = n*[0]
b = n*[True]
for i in range(n):
    v[i] = int(input("Ingresar elemento > "))


for i in range(n):
    for j in range(n):
        if v[i] == v[j] and i != j:
            b[i] = False
            b[j] = False

print("Elementos que no se repiten:")
for i in range(n):
    if b[i] == True:
        print(v[i], end=" ")