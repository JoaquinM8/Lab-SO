n = int(input("Longitud del arreglo > "))
v = n*[0]
for i in range(n):
    v[i] = int(input("Ingresar elemento > "))
    
e = int(input("Elemento a buscar > "))

if e in v:
    print("Su índice es:",v.index(e))
else:
    print("No se encuentra el elemento en el arreglo")