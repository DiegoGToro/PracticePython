"""Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, 
y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”"""
"import math"

from math import sqrt

print("En este ejercicio se hara algoritmo para soluciòn a Ecuaciòn General")
NumA = float(input("Ingresar el Valor de A: ")) 
NumB = float(input("Ingresar el Valor de B: ")) 
NumC = float(input("Ingresar el Valor de C: ")) 

if ((NumB**2)-(2*NumA*NumC)) < 0 :
    print("No se puede realiza proque no se puede sacar raiz a un numero: ")
else:
    x1 = (-NumB + sqrt((NumB**2) - (4*NumA*NumC)))/(2*NumA)
    x2 = (-NumB - sqrt((NumB**2) - (4*NumA*NumC)))/(2*NumA)
    print("La soluciòn es= \nX1: ", x1, "\nX2: ", x2)

