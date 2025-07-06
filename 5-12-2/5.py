s = 0
num = int(input("Ingrese un numero de terminos: "))
for x in range(1,num+1):
    if x % 2 == 0:
        s-=(1/x)
    else:
        s+=(1/x)

print("La suma sera: ", s)    
