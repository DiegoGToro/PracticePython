lista = [232,123,8658]
print(lista)

##Metodos para agregar datos nuevos dentro de una lista
##lista.append(int(input("Ingresa un nuevo dato a la lista: "))) Agregar elemento al final de la lista
print(lista)
lista.insert(2,67.7) ##Agregar dato en determinada posiciòn de la lista sin reemplazar los datos existentes
print(lista)

##Metodos de consultas dentro de lista
lista2 = [8,9,0,8,7,8]
print(lista2.count(8)) ##Cantidad de veces que se repite determinado dato
print(lista2.index(9)) ##Identifica la posiciòn de determinado dato dentro de la lista
lista2.sort()          ##Ordena lista de manera ascendente (Es obligatorio ejecutar por aparte)
print(lista2)
lista2.reverse()       ##Ordena lista de manera descendente
print(lista2)

##Metodos para MODIFICAR DATOS DENTRO DE LA LISTA
lista3 = [8,'pe','Edad',8,'7',8]
lista3[3] = 22
print(lista3)
lista3.pop() ##Eliminar Ultimo dato dentro de la lista
print(lista3)
lista3.remove(8) ##Eliminar determinada dato dentro de la lista
print(lista3)