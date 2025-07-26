def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t oprima cualquier tecla para continuar:")

def menu_principal():
    print("sistema de gestion de notas \n 1.- Registro \n 2.- Login \n 3.- Salir ")
    opcion=input("elige una opcion: ").upper()
    return opcion