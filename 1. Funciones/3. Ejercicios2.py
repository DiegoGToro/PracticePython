def factorial():
    from math import factorial ##Libreria para sacar el Factorial

    num = int(input("Ingrese un Numero del cual desea conocer su factorial: "))
    factor = 1
    if num > 0:
        ##print(factorial(num)) //Funciòn de Python màs directa
        for i in range(1, num+1):
            factor = factor * i    
        print("El Factorial Es: ", factor)    
    else:
        print("El numero es negativo y no se puede proceder")
        
factorial()