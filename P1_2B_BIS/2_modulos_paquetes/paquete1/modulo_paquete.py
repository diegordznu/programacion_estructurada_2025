import os

# Un modulo es simplemente un archivo con extensión .py que contiene código de python (funciones, clases, variables, etc.).

# Un paquete es una carpeta que contiene varios módulos (archivos .py) y un archivo especial llamado __init__.py, que le indica a Python que esa carpeta debe tratarse como un paquete.

os.system("cls")

def solicitarDatos():
   nombre = input("Nombre: ")
   tel = input("teléfono: ")
   print(f"El nombre es: {nombre} y su telefono es: {tel}")

def solicitarDatos2(nombre, tel):
   nombre =  input("Nombre: ")
   tel = input("Telefono: ")
   return nombre, tel

def solicitarDatos3(nombre, tel):
   print(f"El nombre es: {nombre} y el teléfono es: {tel}")

def solicitarDatos4(nombre, tel):
   return f"El nombre es {nombre} y el teléfono es {tel}"

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("...Oprima una tecla para continuar...")

def saludar(nombre):
    nom = nombre
    return f"Hola, bienvenido {nom}"

