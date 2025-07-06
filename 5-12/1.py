while True:

    c = float(input("Ingrese su capital > "))
    y = int(input("Cantidad de años > "))
    i = int(input("Interés (0-100) > "))

    if c>0 or y>=1 or i>0 or i<=100:
        for j in range(y):
            c = c * (1 + i/100)
        break
    else:
        print("Valores inválidos")
        print()

print()
print("Dinero final:",round(c,2))
