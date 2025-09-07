class FabricaTelefonos():
    pass##Para que pase sin realizar nada

print(type(FabricaTelefonos))

celular = FabricaTelefonos() #Objeto creada apartir de la clase FabricaTelefonos
celular2 = FabricaTelefonos()

print(type(celular))
print(type(celular2))

def fabricaTelefonos(): ##Función (Es necesario evitar errores poniendo el mismo nombre para no tener problemas)
    pass

print(type(FabricaTelefonos()))  #<class 'NoneType'> 