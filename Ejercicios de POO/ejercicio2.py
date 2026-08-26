#Ejercicio 2
"""Realizar un programa en el cual se declaren dos valores enteros por te
clado utilizando el método _init_. Calcular después la suma, resta, m
ultiplicación y división. Utilizar un método para cada una e imprimir los
resultados obtenidos. Llamar a la clase Calculadora."""

class Calculadora():
    def __init__(self):
        self.num1=0
        self.num2=0
    def llenarDatos(self):
        self.num1 = int(input("Ingrese el #1: "))
        self.num2 = int(input("Ingrese el #2: "))
    def suma(self):
        print("La suma de {} + {} es: {}".format(self.num1, self.num2, self.num1+self.num2))
    def resta(self):
        print("La resta de {} - {} es: {}".format(self.num1, self.num2, self.num1-self.num2))
    def multiplicacion(self):
        print("La multiplicación de {} * {} es: {}".format(self.num1, self.num2, self.num1*self.num2))
    def division(self):
        print("La division de {} / {} es: {}".format(self.num1, self.num2, self.num1/self.num2))

calculadora = Calculadora()
calculadora.llenarDatos()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()