num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

for i in range(num1, num2 + 1):
    if i%2 == 0:
        continue
    print(i)