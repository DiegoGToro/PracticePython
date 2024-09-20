pesoPayaso = 112
pesoMuñeco = 75

print("Señor usuario por favor digite la cantidad de productos que desea adicionar a su pedido")
print("Cantidad Payasos: ")
canPayasos= int(input())
print("Cantidad Muñecos: ")
canMuñecos= int(input())
pesoTotalPedido = canPayasos* pesoPayaso + canMuñecos * canMuñecos
print("El peso total de su pedido es: " + str(pesoTotalPedido) + "g")
Cadena = "Ejemplo sobre devanaciòn de Cadenas"
print(Cadena[2 : 30])