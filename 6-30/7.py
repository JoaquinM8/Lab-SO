arr = []
numsarr = -1
while numsarr != 0:
    numsarr = int(input("Ingresa los numeros del arreglo (0 para finalizar)"))
    if numsarr != 0:
        arr.append(numsarr)

num = int(input("Ingrese un numero para saber si esta en la lista: "))
for numero in arr:
    if num in arr:
        print("Premio")
        break
    else:
        print("No premio")
        break