c=0

for i in range(1,1000):
    p=True
    for j in range(2,i):
        if i%j == 0:
            p=False
            break
    if p == True:
        print(i)
        c += 1
                

