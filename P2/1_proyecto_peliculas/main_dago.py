import peliculas_dago

opcion=True
while opcion:
    peliculas_dago.borrarPantalla
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.-\U0001F4DD Agregar  \n\t\t 2.- \U0001F4DBEliminar \n\t\t 3.-\U0001F501 Actualizar \n\t\t 4.-\U0001F50D  Consultar \n\t\t 5.-\U0001F50D Buscar \n\t\t 6.-\U0001F4DB Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.borrarPantalla()
            print(".:: Agregar Peliculas ::.")
            peliculas_dago.agregarPeliculas()
            peliculas_dago.esperarTecla()
        case "2":
            peliculas_dago.borrarPantalla()
            print(".:: Eliminar Peliculas ::.")
            peliculas_dago.borrarPeliculas()
             
        case "3":
            peliculas_dago.borrarPantalla()
            print(".:: Modificar Peliculas ::.") 
        case "4":
            peliculas_dago.borrarPantalla()
            print(".:: Consultar Peliculas ::.")
            peliculas_dago.consultarPeliculas()
            peliculas_dago.esperarTecla()
        case "5":
            peliculas_dago.borrarPantalla() 
            print(".:: Buscar Peliculas ::.")
            peliculas_dago.buscarPeliculass()
            
        case "6":
            peliculas_dago.borrarPantalla()
            print(".:: Vacias Peliculas ::.")
            peliculas_dago.vaciarPeliculas()
            
        case "7":
            opcion=False
            peliculas_dago.borrarPantalla()    
            print("Terminaste la ejecucion del SW")
        case _:
            peliculas_dago.borrarPantalla() 
            input("Opción invalida vuelva a intentarlo ... por favor")