n = int(input("Longitud del vector > "))
v = n*[0]

for i in range(n):
    v[i] = int(input("Ingresar elemento > "))
    
b = int(input("Buscar elemento > "))

f = False

for i in range(n):
    if b == v[i]:
        print("El elemento", b, "se encuentra en la posicion", i)
        f = True

if f == False:
    print("El elemento", b, "no se encuentra en el vector")