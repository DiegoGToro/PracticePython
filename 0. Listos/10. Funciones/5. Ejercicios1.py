def PedirNumeros():
    num1 = input("Ingrese Numero 1: ")
    num2 = input("Ingrese Numero 2: ")
    
    print("Si Num1>Num2=1, Si Num2>Num1=-1, Si Num1=Num2=0")
    if(num1 > num2):
        return 1
    elif(num1 < num2):
        return -1
    else:
        return 0

    
print("Programa que compara dos numeros ingresados (Mayor|Menor|Igual)")
print("El resultado es: ", PedirNumeros())