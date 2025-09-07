#De una clase hijo se heredan los atributos de la clase padre
class Animales():
    def hablar(self):
        print("Yo soy un animal")
    
    def descripcion(self):
        print("Yo soy una {}".format(self.animal))

class Perro(Animales): ##Al recibir la clase Animales estamos heredando los atributos de la clase que se recibe (Animales)
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.hablar()

perro = Perro()
perro.hablar()

abeja = Abeja("Abeja")
abeja.descripcion()
