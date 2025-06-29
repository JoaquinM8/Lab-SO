n = int(input("Longitud del vector > "))
v = n*[0]

for i in range(n):
    v[i] = int(input("Ingresar elemento > "))

def ordenar(v):
    for i in range(len(v)):
        for j in range(len(v)-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return v

v = ordenar(v)
print(v)

e = int(input("Agregar un elemento > "))
v.append(e)

v = ordenar(v)
print(v)