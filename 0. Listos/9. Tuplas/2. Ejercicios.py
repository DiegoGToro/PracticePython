## Ejercicio 1
tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mes = int(input("Ingrese el numero del mes(1/12) que desea conocer: "))

if mes >= 1 and mes <= 12:
    print("El mes {} es: {}".format(mes, tupla[mes-1]))
else:
    print("El mes {} no esta dentro de las opciones (No Existe)".format(mes))

## Ejercicio 2
tuplaAlb = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z')
print(len(tuplaAlb))

numero = int(input("Ingrese el numero de la letra del abecedario que quiere imprimir: "))

if numero >= 1 and numero <= len(tuplaAlb):
    print("La Letra del Abecedario que corresponde al numero {} es: {}".format(numero, tuplaAlb[numero-1]))
else: 
    print("El numero {} no esta dentro de las opciones disponibles".format(numero))