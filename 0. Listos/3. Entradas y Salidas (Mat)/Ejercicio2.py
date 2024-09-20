"""Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un
determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final"""

import system # type: ignore

print("Ingrese cuanto sacaste por cada item de Clase durante el semestre a continuaciòn...")
Prac1 = float(input("Practica 1: "))
Prac2 = float(input("Practica 2: "))
Prac3 = float(input("Practica 3: "))

Parcial = float(input("Examen Parcial: "))
Final = float(input("Examen Final"))

print(system.cls())
Pp = (Prac1 + Prac2 + Prac3)/3
Prom = (Pp + (Parcial*2) + (Final*3))/6

print("El Promedio por Practica es: " + Pp)
print("La nota Final es: " + Final)

