class A():
    def __init__(self):
        self._contador = 0 #cuando se tienes diferentes atributos es importante ponerle un guion bajo
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador
    
a = A()
print(a.cuenta())
a._cuenta = 20 ##Evitar este tipo de practica
print(a._cuenta)
