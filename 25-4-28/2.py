vel = int(input("Ingresar velocidad (km/h) > "))

if vel <= 60:
    print("Velocidad permitida")
elif vel > 60 and vel < 81:
    print("Exceso leve")
else:
    print("Exceso grave")