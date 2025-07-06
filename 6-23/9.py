n = int(input("Cantidad de animales > "))
a = n*[""]

for i in range(n):
    a[i] = input("Nombre del animal > ")

v = input("Conocer vecinos del animal > ")

if v in a:
    if v == a[0]:
        print("El vecino es:", a[1])
    elif v == a[-1]:
        print("El vecino es:", a[-2])
    else:
        print("Vecinos:", a[a.index(v)-1], "y", a[a.index(v)+1])