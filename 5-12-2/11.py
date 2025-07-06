p = 0

for i in range(10):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        p += 1
print("La cantidad de números pares es:", p)