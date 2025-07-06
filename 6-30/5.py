arr = []
numsarr = -1
while numsarr != 0:
    numsarr = int(input("Ingresa los numeros del arreglo (0 para finalizar)"))
    if numsarr != 0:
        arr.append(numsarr)

sin_duplicados = []
for num in arr:
    if num not in sin_duplicados:
        sin_duplicados.append(num)
print("Arreglo: ", arr)
print("Arreglo sin duplicados:", sin_duplicados)