##Programa que imprime la Vocal1 en Minuscula y la Vocal2 en Mayuscula

vocal1 = input("Ingresar una Vocal (Minuscula): ")
vocal2 = input("Ingresar una Vocal (Mayuscula): ")

print(vocal1.lower(), vocal2.upper())


##Programa que le pida al usuario Nombre, edad, Sexo y los muestre 
##Te llamas: <Nombre>
##Tu edad es: <Nombre>
##Tu Sexo es: <Nombre>

nombre = input("Ingrese el nombre: ")
Edad = int(input("Ingresa la Edad: "))
Sexo = input("Ingresa tu Sexo: ")

##print("Te llamas: {}".format(nombre))
print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre, Edad, Sexo))