conjunto = {1,2,2,3,4,5,7} ##Los Conjuntos solo imprime los datos no repetidos
print(conjunto)

conjunto.add("H")
print(conjunto)
conjunto.remove("H") ##Lo mismo que conjunto.discard("H")
print(conjunto)
conjunto.pop() ##Eliminar un Dato al Azar del conjunto
print(conjunto)

conjunto.update([6]) ##Añadir elementos Iterables
print(conjunto)