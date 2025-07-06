n = int(input("Longitud del arreglo > "))
arr = n*[0]
for i in range(n):
    arr[i] = int(input("Ingresar elemento > "))
        
print(arr)
ordenado = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        ordenado = False
        print("No premio")
        break

if ordenado == True:
    print("Premio")