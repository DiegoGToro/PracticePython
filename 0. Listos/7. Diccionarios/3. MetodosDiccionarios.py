Diccionario = {1:2, 2:3, 3:4}
Diccionario2 = {7:5, 8:6, 9:0}
print(Diccionario)
Diccionario.pop(3) ##Medoto para eliminar una clave determinada
print(Diccionario)
##Diccionario.clear() ##Limpiar todo el Diccionario
print(Diccionario)
print(Diccionario.get(2)) ##Para obtener el Valor de una Clave
Diccionario.setdefault(4, 10) #Adicionar Nueva Clave con Valor
print(Diccionario)
Diccionario.update({1:50}) ##Metodo para Actualizar Valor de una Clave
print(Diccionario)
##------------------------------
Diccionario.update(Diccionario2) ##Adicionar en Diccionario el Diccionario2
print(Diccionario)
print(Diccionario2)
Diccionario2=Diccionario.copy() ##Copia del Diccionario
print(Diccionario2)

