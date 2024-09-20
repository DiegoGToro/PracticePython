lista = []

def AgregarNumeros():
    num = int(input("ingrese un numero para adiccionar a la lista: "))
    lista.append(num)

def ParesImpares():
    list1 = []
    list2 = []
    
    for i in lista:
        if i%2 == 0:
            list1.append(i)
        else:
            list2.append(i)
    
    print("Numeros Pares: ")
    for j in list1:
        print(j)
    print("Numeros Impares: ")
    for k in list2:
        print(k)

resp = input("Desea agregar elementos a la lista (S/N): ")
while resp.upper() == "S" or resp.upper() == "SI":
    AgregarNumeros()
    resp = input("Desea agregar elementos a la lista (S/N): ")
    
lista.sort()
print("A continuaciòn se imprimira dos listas por aparte (Pares / Impares)")
ParesImpares() 