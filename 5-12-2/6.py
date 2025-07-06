num = int(input("Ingresad el número > "))
n = ""
while num > 0:
    resto = num % 10
    n += str(resto)
    num = num//10
int(n)
print(n)
