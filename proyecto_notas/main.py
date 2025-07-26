import funciones

import conexionBD

def main():
    funciones.borrarPantalla()
    opcion=funciones.menu_principal()

    if opcion =="1" or opcion=="REGISTRO":
        print("estoy en la opcion 1")
    elif opcion =="2" or opcion=="LOGIN":
        print("estoy en la opcion 2")
    elif opcion=="3" or opcion=="SALIR":
        print("Estyot en la opcion 3")
        print("saliste del sistema")
        opcion=False
        funciones.esperarTecla()
        

main()