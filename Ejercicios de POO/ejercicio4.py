#Ejercicio 4
"""Crear una clase llamada Marino(), con un metodo que sea hablar, en do
nde muestre un mensaje que diga "Hola..". Luego, crear una clase Pulp
o() que herede Marino, pero modificar el mensaje de hablar por "Soy u
n Pulpo". Por ultimo, crear una clase Focal), heredada de Marino, pero
que tenga un atributo nuevo llamado mensaje y que muestre ese mesj
ae como parametro"""

class Marino():
    def hablar(self):
        print("Hola :)")

class Pulpo(Marino):
    def hablar(self):
        print("soy un pulpo")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino= Marino()
marino.hablar()

pulpo= Pulpo()
pulpo.hablar()

foca= Foca()
foca.hablar("Hola, Soy una Foca hermosa")

