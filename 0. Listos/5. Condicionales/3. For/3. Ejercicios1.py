i=0
while i < 10:
    i += 1
    print(i)
 
print("A continuaciòn se imprimira el rango entre dos cifras ingresadas por el Usuario")   
num1 = int(input("Ingrese la cifra 1 (1/10): "))
num2 = int(input("Ingrese la cifra 2 (1/10): "))

if num1 > num2:
    print("Imprimiendo el Rango entre 2 numeros")
    for j in range(num2,num1+1):
        print(j)
elif num2 > num1:
    print("Imprimiendo el Rango entre 2 numeros")
    for k in range(num1,num2+1):
        print(k)
else:
    print("No hay Rango entre 2 cifras iguales")