class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensjae):
        return mensjae
    
    def escucharMusica():
        print("Estas escuchando Música")

telefono = FabricaTelefonos()

telefono.color = "Blanco" ##
print(telefono.marca)
print(telefono.color)

print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()