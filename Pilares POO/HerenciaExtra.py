class Animales():
    def __init__(self, nombre):#Todos los atributos de la clase padre no siempre son heredados, para eso se usa el super
        self.nombre = nombre
class Perro(Animales):
    def __init__(self, nombre, sonido):
        self.sonido = sonido
        super().__init__(nombre) #Necesario para poder heredar el atributo de la clase padre

perro = Perro("Pedrokz", "Ladrido!!")
print(perro.nombre)
print(perro.sonido)