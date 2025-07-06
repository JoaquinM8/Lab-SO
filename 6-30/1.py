arr = []
numsarr = -1
while numsarr != 0:
    numsarr = int(input("Ingresa los numeros del arreglo (0 para finalizar)"))
    if numsarr != 0:
        arr.append(numsarr)

print(arr)    
producto = 1
for num in arr:
    producto *= num

print("El producto de los elementos del arreglo es:", producto)