def AreaCuadrado():
    base = int(input("Ingrese la Base: "))
    altura = int(input("Ingrese la Altura: "))
    print("El area del Circulo es: ", base*altura, "Cm²")

def AreaCirculo():
    radio = int(input("Ingrese el Radio del Circulo: "))
    print("El area del Circulo es: ", 3.1416*pow(radio,2), "Cm²")

print("A continuación procedemos a calcular el Area de un Cuadrado (Metros)")
AreaCuadrado()
print("A continuación procedemos a calcular el Area de un Circulo (Metros)")
AreaCirculo()
print("Gracias por Visitarnos...")
