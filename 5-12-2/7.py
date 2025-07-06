num = int(input("Ingresa un numero: "))
p=True
for j in range(2,num):
    if num%j == 0:
        print("No es primo")
        p=False
        break
if p==True:
    print("Es primo")

        