arr = []
numsarr = -1
while numsarr != 0:
    numsarr = int(input("Ingresa los numeros del arreglo (0 para finalizar)"))
    if numsarr != 0:
        arr.append(numsarr)
par = 0        
for num in arr:
    if num %2 == 0:
        par += 1
print("Los numeros pares son:", par)