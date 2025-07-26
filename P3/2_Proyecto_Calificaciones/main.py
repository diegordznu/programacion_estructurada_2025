import calificaciones

def main():
    datos=[]
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()
        match opcion:
            case "1":
                calificaciones.agregarCalificaciones()
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones()
                calificaciones.esperarTecla()
            case "3":
                calificaciones.promedios()
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscarCalificacion()
                calificaciones.esperarTecla()
            case "5":
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\t \U0001F389 Terminaste la ejecucion del SW \U0001F389 ")
            case _: 
                input("\n\t \U0001F501 Opción invalida vuelva a intentarlo ... por favor")
                
                
if __name__=="__main__":
    main()