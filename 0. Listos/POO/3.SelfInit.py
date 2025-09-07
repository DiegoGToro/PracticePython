#Self = Permite equiparar atributos a metodos de la instancia (objeto)
#Sirve para englobar un atributo a toda una clase 
# Self (es lo mismo que 'this' utilizado en otros lenguajes en temas de funcionamiento)
class FabricaTelefonos():
    
    ##Init = Primer metodo que se ejecuta al crear un objeto (Como un contructor)
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("Estoy en metodo init porque se ha creado un nuevo objeto")

    def ElaborarHuawei(self):
        self.marca = "Huawei"
        self.color = "Blanco"

telefono = FabricaTelefonos("Samsung", "Negro")
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)

telefono2 = FabricaTelefonos("Samsung", "Negro")