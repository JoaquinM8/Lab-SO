c = int(input("Cantidad de números > "))
men=103010203190
may=0

for i in range(c):
    n = int(input("Ingresad el número > "))
    if n < men:
        men=n
    elif n > may:
        may=n

print("Mayor:",may)
print("Menor:",men)