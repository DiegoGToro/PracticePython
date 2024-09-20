##Ejercicio 2
Diccionario = {1:"Casillas", 15:'Ramos', 3:"Pique", 5: "Poyul", 16: "Busquets", 8: "Diego G.",
               11: "Capdevilla", 14: "Xabi H", 18: "Pedrito", 6:"Iniesta"}

id = int(input("Ingresa el numero para identificar el Jugador: "))
if id in Diccionario:
    print("El Jugador con el numero {} es: {}".format(id, Diccionario[id]))
else:
    print("El Jugador no esta dentro de las opciones Disponibles")