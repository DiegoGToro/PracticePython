##Ejercicio 1
lista = [20,50,"Curso",'Python',3.14]

print(lista.insert(0,(input("Ingrese el segundo dato para la lista que reemplazara {}: ".format(lista[0])))))
print(lista.insert(1,(input("Ingrese el segundo dato para la lista que reemplazara {}: ".format(lista[1])))))
print(lista)
lista.remove(20) ##Esto solo sirve cuando sabes que dato esta dentro de la lista
lista.remove(50)
print(lista)

##Ejercicio 2
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista1[3] = lista1[3]*2
lista1[6] *=2
lista1[8] = lista1[8]*2
print(lista1)