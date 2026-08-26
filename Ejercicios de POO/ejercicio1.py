##Ejercicio 1
""" Realizar un programa que conste de una clase llamada Estudiante,
que tenga como atributos el nombre y la nota del alumno. Definir los m
étodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
con el resultado de la nota y si ha aprobado o no. """

class Estudiante():
    def __init__(self):
        self.nombre= "ninguno"
        self.nota = 0

    def ingDatos(self):
        self.nombre= input("Ingrese el nombre del estudiante: ")
        self.nota= float(input("Nota del estudiante: "))
    
    def imprimir(self):
        print("Nombre: ", self.nombre)
        if self.nota >= 3 and self.nota <=5:
            print("Nota: ", self.nota)
            print("El estudiante {} a ganado la materia".format(self.nombre))
        elif self.nota < 3 and self.nota >= 0:
            print("Nota: ", self.nota)
            print("El estudiante {} perdio la materia".format(self.nombre))
        else:
            print("La nota del estudiante no es valida")
    
estudiante = Estudiante();
estudiante.ingDatos()
estudiante.imprimir()
print("Gracias por visitarnos...")
