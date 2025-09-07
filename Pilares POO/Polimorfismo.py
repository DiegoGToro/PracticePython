#Es la modificación de Metodos cuando se heredan de otras clases
#Crear objetos que apunten o que usen el mismo metodo pero que un objeto sea diferente

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def correr(self):
        print(self.mensaje)

##Como no tenemos metodo __init__ en la clase perro no es necesario el Super
class Perro(Animales):
    def correr(self):
        print("Yo solo corro")

class Pez(Animales):
    def correr(self):
        print("Yo solo nado")

animal = Animales("No me digas!!")
animal.correr()

perro= Perro("Guau!")
perro.correr()

pez = Pez("Glu, Gluu!")
pez.correr()