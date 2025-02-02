def valores(): ##Función Estatica
    global num1, num2 ##Declaración de Variables Globales
    num1 = 110
    num2 = 12
    resultado = num1 + num2
    return resultado

def resta():
    resultado = num1 - num2
    return resultado

print("Valor de Suma: ", valores())

print("Valor de Resta: ", resta())