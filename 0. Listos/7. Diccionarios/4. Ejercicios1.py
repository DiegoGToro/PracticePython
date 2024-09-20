##Ejercicio 1
Diccionario = {'Guatemala':'Cuidad de Guatemala', 'Honduras':"Honduras", 'Nicaragua':"Managua",
               'Costa Rica': "San Jose", 'Panama': "Panama", 'Argentina': "Buenos Aires",
               'Colombia': "Bogota", 'Venezuela': "Caracas", 'España': "Madrid"}

pais = input("Ingrese un Pais del cual desea consultar la Capital: ")
##letra = pais.capitalize() in Diccionario

if pais.capitalize() in Diccionario:
    print("La Capital de {} es: {}".format(pais, Diccionario[pais.capitalize()]))
    Diccionario.update({pais.capitalize(): "Nueva Capital"}) ##Actualizar Capital de Pais
    print("La Capital de {} es: {}".format(pais, Diccionario[pais.capitalize()]))
else:
    print("El Pais No Existe Dentro Del Diccionario")