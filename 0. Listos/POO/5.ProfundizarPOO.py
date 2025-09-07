class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel", "Negro","Rojo","Azul", m1=500, m2=1100)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

#Atributo Temporal para un Objeto Especifico
telefono.memoria = 512
print("Valor de atributo temporal: {}".format(telefono.memoria))