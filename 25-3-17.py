
"""
#1.

n = int(input("Ingrese un número entero > "))

if n > 0:
    print("El número es positivo")
elif n < 0:
    print("El número es negativo")
else:
    print("El número es cero")    



#2.

list = []

for i in range(3):
    list.append(int(input("Ingrese un número > ")))

print(f'El número máximo ingresado es: {max(list)}')



#3.

n = int(input("Ingrese un número > "))

if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")



#4.

y = int(input("Ingrese un año > "))

if y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
        print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")



#5.

c = int(input("Ingrese la calificación 0 - 100 > "))

if c < 60:
    print("F")
elif c < 70:
    print("D")
elif c < 80:
    print("C")
elif c < 90:
    print("B")
else:
    print("A")



#6.

u = input("Ingrese el nombre de usuario > ")
p = input("Ingrese la contraseña > ")

if u == "admin" and p == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")
    


#7.

e = int(input("Ingrese la edad > "))

if e >= 18:
	print("Puede votar")
else:
	print("No puede votar")



#8.

d = float(input("Ingrese el precio > "))

if d > 100:
	d = d * 0.9

print(f'El precio a pagar es: {d}')

"""