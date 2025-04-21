# 11

nota = int(input("Ingresa la nota del alumno: "))
if nota >= 10:
    print("Aprobado")
else:
    print("desaprobado")


# 12

salario = int(input("Ingrese el salario del trabajador: "))
if salario <= 1000:
    aumento = salario * 0.15
    salarioactual = salario + aumento
    print("El salario actual es: ", salarioactual)
else:
    print("El sueldo sigue igual")


# 13

año = int(input("Ingrese el año"))
if año % 4 == 0:
    if año % 100 == 0 and año % 400 != 0: 
        print("No es un año bisiesto")
    else:
        print("Es un año bisiesto")
else:
    print("El año no es bisiesto")
    
    
# 14

v = int(input("Ingrese un número > "))
c = int(input("Ingrese el tipo de cálculo > "))

if c == 1:
    print(100*v)
elif c == 2:
    print(100**v)
elif c == 3:
    print(100/v)
else:
    print(0)
    

# 15

n = int(input("Ingrese un número entre 0 y 10 > "))

if n < 0 or n > 10:
    print("Número inválido")
else:
    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


# 16

a = int(input("Ingrese a > "))
b = int(input("Ingrese b > "))
c = int(input("Ingrese c > "))

if a > b:
    if a > c:
        if b > c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if b > c:
        if a > c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)