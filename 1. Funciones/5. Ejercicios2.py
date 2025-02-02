def CalcularTotalFactura(bill, vat):
    print(bill, " ", vat, "%")
    print("Total Facturado: ", ((bill*vat)/100)+bill)
 
print("programa que calcula el total de una Factura aplicando IVA")
CalcularTotalFactura(float(input("Valor Factura sin IVA: ")), float(input("Porcentaje del IVA (0/100%): ")))
