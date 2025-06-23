v1 = []
v2 = []
esc = 0

print("Vector 1")
for i in range(3):
    n = int(input("Ingresa un valor > "))
    v1.append(n)

print("Vector 2")
for i in range(3):
    n = int(input("Ingresa un valor > "))
    v2.append(n)

for i in range(3):
    esc += v1[i] * v2[i]

print("El producto escalar es:", esc)

x = v1[1]*v2[2] - v1[2]*v2[1]
y = - (v1[0]*v2[2] - v1[2]*v2[0])
z = v1[0]*v2[1] - v1[1]*v2[0]

print(f'El producto vectorial es: {x}i, {y}j, {z}k')