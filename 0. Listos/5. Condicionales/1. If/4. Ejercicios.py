##Ejercicio 1
letra = input("Ingrese por favor una Letra, De preferencia Vocal: ")

##if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
if letra.lower() in "aeiou":
    print("La letra ingresada es la Vocal ", letra.upper())
else:
    print("La letra no es una Vocal")
    
##Ejercicio 2
Num = int(input("Ingrese por favor un numero: "))

if Num < 0:
    Num = Num * -1
print("El numero absoluto del numero ingresado es: {}".format(Num))