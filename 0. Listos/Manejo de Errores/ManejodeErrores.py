#try (intentar)
while True:
    try:
        edad = int(input("Ingrese su Edad: "))
        print("Su edad es: ", edad)
        break
    except:
        print("Ingresaste un valor no valido...")
    
print("La ejecución a terminado...")