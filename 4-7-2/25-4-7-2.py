print() # 6

ax = float(input("Ingrese la coordenada X de A > "))
ay = float(input("Ingrese la coordenada Y de A > "))

print()

bx = float(input("Ingrese la coordenada X de B > "))
by = float(input("Ingrese la coordenada Y de B > "))

d = ( (ax-bx) ** 2 + (ay-by) ** 2 ) ** (1/2)

print(f'La distancia entre el punto A ({ax},{ay}) y el punto B ({bx},{by}) es: {round(d,2)})')



print() # 7

n1 = int(input("Ingresar primer número > "))
n2 = int(input("Ingresar segundo número > "))

p = (n1+n2) / 2

print(f'El promedio es {p}')



print() # 8

b = float(input("Ingrese la base del rectángulo > "))
h = float(input("Ingrese la altura del rectángulo > "))

per = b*2 + h*2
sup = b*h

print(f'El perímetro es {per} y la superficie es {sup}')



print() # 9

lxg = 3.785
pxl = 1.28

g = float(input("Cantidad de galones > "))

pt = g*lxg*pxl

print(f'El precio total es {round(pt,2)}')



print() # 10

r = float(input("Ingrese el radio del cilindro > "))
h = float(input("Ingrese la altura del cilindro > "))

a = 3.14 * r**2 * h
v = 2*3.14 * r * (r+h)

print(f'El área es {round(a,2)} y el volumen es {round(v,2)}')