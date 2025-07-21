"""dict es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener
como las listas, indices numeros tiene alfnamuericos. Es decir es algo parecido como los objetos

tambien se conoce como un arreglo asociativo u objeto JSON

el diccionario es una coleciion ordenada** y modificable. No hay miembros duplicados"""
import os
os.system("cls")

#lista
#paises={"Mexico", "Brasil", "Canada", "España"}
#dict
pais_mexico={"nombre": "Mexico", "Capital": "CDMX", "poblacion": "12000000", "Idioma": "Español"}
pais_brasil={"nombre": "brasil", "Capital": "Brasilia", "poblacion": "10000000", "idioma": "Portugues"}
pais_canada={"nombre": "Canada", "Capital": "Ottawa", "poblacion": "90000000", "idioma": ("Ingles", "Frances")}

alumno={"nombre": "Daniel",
        "apellido1": "Hernandez",
        "apellido2": "Gomez",
        "especialidad": "TI",
        "area": "Software Multiplataforma",
        "modalidad": "BIS",
        "Semestre": "2",
        "Matricula": "1234567",}
#mostrar el coontenido del dict
for i in alumno:
    print(f"{i}={alumno[i]}")

#agregar un campo o atributo
alumno["telefono"]= "6181234568"
for i in alumno:
    print(f"{i}={alumno[i]}")