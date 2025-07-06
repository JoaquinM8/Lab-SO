n = int(input("Ingresa el valor del vector: "))
v = n*[""]
print(v)
for i in range(n):
    v[i] = input("Ingrese el caracter: ")

z = ""
d = n

for i in range(n//2):
    z = v[i]
    v[i] = v[d-1]
    v[d-1] = z
    d = d - 1

for i in range(n):
    print(v[i])