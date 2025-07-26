import agenda

def main():
    agenda_contactos = {}
    opcion = True
    
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuMain()
        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contactos(agenda_contactos)
                agenda.esperarTecla()
            case "3":
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "4":
                agenda.modificar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "5":
                agenda.borrar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "6":
                opcion = False
                agenda.borrarPantalla()
                print("\n\t🚪 Terminaste la ejecución del sistema de agenda.") 
                        
                
                
                
if __name__=="__main__":
    main()