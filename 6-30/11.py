n = int(input("Longitud del arreglo > "))
arr = n*[0]
for i in range(n):
    arr[i] = int(input("Ingresar elemento > "))
        
arr.reverse()
print(arr)