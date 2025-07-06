e=0
while e>=0:

    num = int(input("Ingresa un numero > "))
    sum = 0

    for i in range(1,num+1):
        if num % i == 0:
            sum += i
    print("La suma de los divisores de",num," es:",sum)

    e = int(input("Ingrese un número negativo si desea terminar > "))