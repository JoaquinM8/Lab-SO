n = int(input("Longitud del arreglo > "))
v1 = n*[0]
for i in range(n):
    v1[i] = int(input("Ingresar elemento > "))

n = int(input("Longitud del arreglo > "))
v2 = n*[0]
for i in range(n):
    v2[i] = int(input("Ingresar elemento > "))
    
v3 = []    

if len(v1) == len(v2):
    for i in range(n):
        v3.append(v1[i] + v2[i])

print("Suma de los arreglos:", v3)