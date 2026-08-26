#Ejercicio 5
"""Crear un programa con tres clases Universidad, con atributos nombre (
Donde se almacena el nombre de la Universidad). Otra llamada Carerra
, con los atributos especialidad (En donde me guarda la especialidad d
e un estudiante). Una ultima llamada Estudiante, que tenga como atrib
utos su nombre y edad. El programa debe imprimir la especialidad, eda
d, nombre y universidad de dicho estudiante con un objeto llamado pe
rsona."""

class Universidad():
    def __init__(self, nombreUniversidad):
        self.nombreUni= nombreUniversidad

class Carrera():
    def carrera(self, especialidad):
        self.especialidad= especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

    def imprimir(self):
        print("El estudiante {} con {} años de edad, se encuentra en la Universidad '{}' cursando la especialidad '{}'".format(self.nombre,self.edad,self.nombreUni,self.especialidad))

persona= Estudiante("PCJIC")
persona.carrera("Ing. Informatica")
persona.datos("Diego", 24)
persona.imprimir()