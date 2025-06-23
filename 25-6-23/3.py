v = []
b = 100*[True]

for i in range(1,101):
    v.append(i)

b[0] = False

for i in range(1,99):
    for j in range(i+1,100):
        if v[j] % v[i] == 0:
            b[j] = False

for i in range(100):
    if b[i] == True:
        print(v[i])