cant = int(input("Ingrese la cantidad de numeros a evaluar: "))
c = 0
for i in range(cant):
    num = int(input("Ingrese los numeros: "))
    if num == 0:
        c += 1
print("Hay", c ,"Ceros")        