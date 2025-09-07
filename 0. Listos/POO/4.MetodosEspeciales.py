class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado.".format(self.marca))

    #Permite dale una mejor descripción al Objeto llamado
    def __str__(self):
        return "El objeto es {}".format(self.marca)

    ##Metodo destructor - Elimina todos los objetos al terminar ejecución del Codigo
    def __del__(self):
        print("Acabas de finalizar el programa, el objeto {} ha sido destruido").format(self.marca)


telefono = FabricaTelefonos("Huawei", "Azul Marino")
print(telefono.marca + " - " + telefono.color)
print(telefono)