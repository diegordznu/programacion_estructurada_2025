#Un modulo es simplemente un archovo con extension py que contiene código de python (funciones, clases, variables, etc)
#un paquete es una carpeta que contiene varios modulos (archivos py) y un archivo especial llamado _init_py, que le indica a python
#que esa carpeta debe de tratarse como un paquete


import os
def solicitardatos1():
    nombre=input("nombre: ")
    telefono=input("telefono: ")

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")


def solicitardatos3(nombre,telefono):
    nombre=nombre
    telefono=telefono

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

nombre=input("nombre: ")
telefono=input("telefono: ")



def solicitardatos2():
    nombre=input("nombre: ")
    telefono=input("telefono: ")
    return nombre,telefono


def solicitardatos4(nombre,telefono):
    nombre=nombre
    telefono=telefono
    return nombre,telefono


solicitardatos1()
nom3=input("nombre: ")
tel3=input("telefono: ")
solicitardatos3(nom3,tel3)

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("...oprima una tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"hola bienvenido {nom}"