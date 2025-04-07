print() # 1

v = float(input("Ingrese la velocidad del objeto (m/s) > "))
t = float(input("Ingrese el tiempo (s) > "))

m = v*t

print()
print(f'El objeto recorrió {m}m')



print() #2

n1 = float(input("Ingrese la primer nota > "))
n2 = float(input("Ingrese la segunda nota > "))
n3 = float(input("Ingrese la tercer nota > "))

p = (n1+n2+n3) / 3

print(f'El promedio es {round(p,2)}')



print() #3

rc = int(input("Cantidad de respuestas correctas > "))
ri = int(input("Cantidad de respuestas incorrectas > "))
rb = int(input("Cantidad de respuestas en blanco > "))

pf = rc*3 + ri*(-1)
pt = (rc+ri+rb) * 3 

print(f'Puntaje final: {pf}/{pt}')



print() #4

pg = int(input("Partidos ganados > "))
pe = int(input("Partidos empatados > "))
pp = int(input("Partidos perdidos > "))

pf = pg*3 + pe*1
pt = (pg+pe+pp) * 3 

print(f'Puntaje final: {pf}/{pt}')



print() #5

gb = float(input("Ingresar Gigabytes > "))
mb = gb*1024
md = mb/1.44

print(f'Se necesitan {round(md)} micro discos 3.5')