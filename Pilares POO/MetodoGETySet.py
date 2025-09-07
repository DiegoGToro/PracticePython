class A():
    def __init__(self): 
        self._contador = 0
        self._cuenta = 1

    @property 
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, cont):
        self._contador = cont
    
    @property #Se le indica al programa que este es un metodo y puede ser reconocido sin llamarlo con los "()"
    def cuenta(self): ##Metodo get para returnar el valor de la variable Cuenta
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self, cuent): ##Metodo set para asignar un valor a la variable Cuenta
        self._cuenta = cuent
    
a = A()
print(a.cuenta)
a.cuenta = 20
print(a.cuenta) #El @property  se agrego para que el metodo se pudiera llamar de esta manera
print(a.contador)
a.contador = 10
print(a.contador)