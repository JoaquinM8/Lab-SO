e = int(input("Cantidad de empleados > "))
m = 0
o = 0
for i in range(e):
    sueldo = float(input("Sueldo del empleado > "))
    if sueldo > m:
        m = sueldo
        o = i+1
print("El empleado con mayor sueldo es el", o, "con un sueldo de", m)