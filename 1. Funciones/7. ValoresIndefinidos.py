def argumento(num):
    return type(num)

def argumento1(*num): ##Recibir Tupla
    for i in num:
        print(i)
    print(type(num))
        
print(argumento(10))
print(argumento(10.5))
print(argumento('Cadena'))

argumento1(10, 20, 30, 40, 50)
