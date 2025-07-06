for i in range(2,30):
    p=True
    for j in range(2,i):
        if i%j == 0:
            p=False
            break
    if p == True:
        print(f'{i} | {i**3}')