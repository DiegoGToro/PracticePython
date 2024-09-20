Diccionario = {'Usuarios':"DiegoGT", 'Contrasena':1001, 'Estatura':1.76}

print(Diccionario)
print(Diccionario.keys()) ##Imprime solo las Claves
print(Diccionario.values()) ##Imprime solo los Valores
print(Diccionario["Estatura"]) ##Imprime el valor de X Clave

Diccionario["Peso KG"] = 49 ##Se puede añadir Nuevos parametros dentro del diccionario sin ningun metodo
print(Diccionario)

Diccionario["Contrasena"] = 1111 ##Modifica de determinada Clave el Valor
print(Diccionario)