#ejemplo 1 crear una lista de numeros e imprimir el contenido
import os
os.system("cls")

num=[12,24,8,30,34]
print(num)

#ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidenica de una palabra
#1er forma
lista=["hola","adios","chao","uno"]
print(lista)
resp=input("escriibe la palabra a buscar: ") in lista
print(f"el numero de veces que se econtro la palabra lista.count(resp)")
if resp:
    print("si hay")
else:
    print("no hay")

#2da forma
encontro=False
for i in range(0,len(lista)):
    if lista[i]==resp:
        encontro=True

if encontro:
    print(f"si econtro la palabra")
else:
    print(f"no eocntro la palabra")

#3er forma
encontro=False
for i in lista:
    if i==resp:
        encontro=True

if encontro:
    print(f"si econtro la palabra")
else:
    print(f"no eocntro la palabra")


#añadir elementos a la lista
numeros=[]
opc=True
print(numeros)

while opc:
    numero=float(input("dame un numero entero o decimal: "))
    numeros.append(numero)
resp.input("deseas agregar otro numero?: ").lower()
if resp=="si":
    opc=True
else:
    opc=False
print(numeros)

#ejemplo 4 crear una lista multidimensional que sea una agenda
agenda=[
        ["Carlos", "618543029"],
        ["Alberto", "61895209"],
        ["Martin", "61803980"]
]
for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r] [c])

cadena=""
for r in range(0,3):
    for c in range (0,2):
        cadena+=f"{agenda [r] [c]}, "
        cadena+="\n"
print(cadena)
