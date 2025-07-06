d = int(input("Ingresa la dimension del vector: "))
v = d*[0]

for i in range(d):
    v[i] = int(input("Ingresa un numero: "))

for i in range(d):
    for j in range(d-1):   
        if v[j] < v[j+1]:
            m = v[j]
            v[j] = v[j+1]
            v[j+1] = m

print(v)