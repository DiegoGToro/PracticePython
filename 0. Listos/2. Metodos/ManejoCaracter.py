cadena = 'Estoy utilizando los metodos de Python'
cadena1 = 'ESTOY UTILIZANDO LOS METODOS NECESARIOS'

print(cadena.upper())
print(cadena1.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.swapcase())

"""Ejercicios Basicos de Cadenas"""
"Imprimir los dos primeros caracteres"
print(cadena[0 : 2])
"imprimir los tres ultimos caracteres"
print(cadena[-3:len(cadena)])
"imprimir dicha cadena cada dos caracteres. Ej, Si la cadena fuera 'recta' deberia imprimir rca"
print(cadena[::2])
"Imprimir cadena en sentido contrario"
print(cadena[::-1])
print(cadena[-10:-3:1])

print(cadena.replace('',','))