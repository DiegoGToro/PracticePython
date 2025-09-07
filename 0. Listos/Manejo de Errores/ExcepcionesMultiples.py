while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        resultado = num1 / 100
        print(resultado)
        break
    except ZeroDivisionError: #Cuando el numero ingresado es = 0
        print("No se puede dividir entre Cero")

while True:
    try:
        edad = int(input("Ingrese tu edad: "))
        print("Tu edad es: ", resultado)
        break
    except ValueError: ##Si ingresa algo diferente a un numero entero
        print("Has colocado un valor invalido")
    except KeyboardInterrupt:
        print("\nHas cancelado la Ejecución")
        break

        
        