##Ejercicio 2 (Palabras que riman)
print("Programa hecho con el objetivo de verificar si dos palabras ingresadas riman")
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if palabra1[-3 : ] == palabra2[-3 : ]:
    print("Estas dos palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Estan palabras riman un poco")
else:
    print("Estan palabras no riman")
    

##Ejercicio 2 (Candidato a votar)
voto = input("· Elija por favor a que candidato desea Votar\n-> A. Partido Rojo\n-> B. Partido Verde\n-> C. Partido Azul\n --> ")

if voto.upper() == "A":
    print("Usted Voto por el Partido Rojo")
elif voto.upper() == "B":
    print("Usted Voto por el Partido Verde")
elif voto.upper() == "C":
    print("Usted Voto por el Partido Azul")
else: 
    print("Su voto no esta dentro de las opciones")