'''crear un proyecto que permita gestionar(administrar) calificaciones colocar un menu de opciones para agregar, mostrar, y calcular promedio de calificaciones de un estudiante, notas


1.- utlizar funciones y mandar llamar desde otro archivo
2.- utilizar una lista (bidimensional) para almacenar el nombre del alumno, así como sus 3 calificaciones'''


import calificaciones

def main():
    datos = []
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla

            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla
                
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperarTecla

            case "4":
                opcion=False
                calificaciones.borrarPantalla()
                print("terminaste la ejecución del SW")
            case _ :
                opcion=True
                print("opcion invalida vuelve a intentarlo")
                calificaciones.esperarTecla
if __name__ =="__main__":
    main()