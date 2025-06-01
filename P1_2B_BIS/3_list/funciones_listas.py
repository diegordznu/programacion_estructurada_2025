'''
List (array)
Son colecciones o conjunto de datos/valores bajo un  mismo nombre, para acceder a los valores se hace con un índice numerico

Nota: vus valores si son modificables

La lista es una coleccion ordenada y modificable, Permite miesmbros duplicados'''

import os
os.system("clear")


#funciones mas comunes en las listas

paises=["Mexico", "Brasil", "España", "Canada"]
numeros=[23,12,100,34]

#ordernar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#añadir o ingresar o insertar elementos a una lista
#1er forma
paises.append("honduras")

#2da forma
paises.insert(1,"honduras")

#eliminar o borrar o quitar elementos de una lista
#1er forma
paises.pop(1)
print(paises)

#2da forma
paises.remove("honduras")
print(paises)

#buscar elemento dentro de la lista
resp="Brasil" in paises
if resp:
    print("si encontraste el pais")
else:
    print("no encontraste el pais")

paises=["Mexico", "Brasil", "España", "Canada"]

for i in range(0,len(paises)):
        if paises[i]=="Brasil":
             print("si encontraste el pais")
        else:
             print("no encontraste el pais")

#cuantas veces aparece un elemento dentro de una lista
print(f"este numero aparece : {numeros.count(12)}")

#indentificar o conocer el indice de un valor
#paises=["Mexico", "Brasil", "España", "Canada"]
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#recorres los valores de la lista
for i in paises:
     print(i)

#2da forma
for i in range (0,len(paises)):
     print(f"paises[i] es: {paises[i]}")
#unir contenido de listas
##paises=["Mexico", "Brasil", "España", "Canada"]
#numeros=[23,12,100,34]
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)