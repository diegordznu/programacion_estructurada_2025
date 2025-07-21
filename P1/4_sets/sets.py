"""set es una coleccion desrodenada, inmutable y no indexada. no hay miembros duplicados"""
import os
os.system("cls")

personas={"Ramiro", "Choche", "Lupe"}
print(personas)
personas.add("Choche")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"hola"}
print(varios)

#ejemplo crear un programa que solicite los emails de los alumnos de la utd almacenar en una lista y posteriormente mostrar en pantalla los mails sin duplicados
opc="si"
emails=[]
while opc=="si":
    emails.append(input("dame el email: "))
    opc=input("Deseas solicitar otro email? si/no)").lower()

print(emails)
set1=set(emails)
print(set1)
emails=list(set1)
print(emails)