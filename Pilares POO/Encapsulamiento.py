##Aplicar sobre atributos el alcance de consulta
#Evita el desbordamiento de memoria

class A():
    def __init__(self):
        self.contador = 1

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador


class B(): ## (No es la opción más optima) Al poner doble guión bajo "__" estamos encapsulando un atributo poniendolo en privado solo para que se tenga acceso desde la clase
    def __init__(self):
        self.__contador = 5

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


print("Objeto A")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador) #Lo idea es no consultarlo por medio del atributo directamente por seguridad

print("Objeto B")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
#print(b.__contador) el atributo tiene doble guion bajo __, ya solo puede ser consultado unica y exclusivamente dentro de la clase