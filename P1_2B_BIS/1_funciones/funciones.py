"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#caso 1 funcion que no recibe parametros ni regresa valor
def solicitardatos1():
    nombre=input("nombre: ")
    telefono=input("telefono: ")

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

#caso 3 funcion que recibe parametros y regresa valor
def solicitardatos3(nombre,telefono):
    nombre=nombre
    telefono=telefono

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

nombre=input("nombre: ")
telefono=input("telefono: ")

#caso 2 funcion que no reciba parametros y regresa valor

def solicitardatos2():
    nombre=input("nombre: ")
    tel=input("telefono: ")
    return nombre,telefono

#caso 4 funcion que recibe parametros y regresa valor
def solicitardatos4(nombre,teledono):
    nombre=nombre
    telefono=telefono
    return nombre,telefono

#llamar funciones
solicitardatos1()
nom3=input("nombre: ")
tel3=input("telefono: ")
solicitardatos3(nom3,tel3)