
##Ejercicio 1 (Re Facil)
num = int(input("Ingrese un numero del cual desea conocer las tablas de multiplicar: "))
i = 0
while i < 10:
    i += 1
    print("{}X{}:{}".format(num,i,num*i))
    
##Ejercicio 2 
edad = int(input("Ingrese su edad: "))
edadAux =edad
while edad > 1:
    print("Has Cumplido {} Años".format((edadAux+1)-edad))
    edad -= 1
    if edad == 1:
        print("Tienes {} años".format(edadAux))