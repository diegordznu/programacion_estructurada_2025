'''crear un proyecto que permita gestionar(administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar, y ocnusltar peliculas, notas


1.- utlizar funciones y mandar llamar desde otro archivo
2.- utilizar dicts para almacenar los siguientes atributos de peliculas'''


import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar Características \n\t\t 5.- Modificar Características \n\t\t 6.- Borrar Características \n\t\t 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.borrarPantalla()
            print(".:: Agregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPantalla()
            print(".:: Eliminar Peliculas ::.")
            peliculas.borrarPeliculas()
             
        case "3":
            peliculas.borrarPantalla()
            print(".:: Mostrar Peliculas ::.")
            peliculas.mostrarPeliculas 
        case "4":
            peliculas.borrarPantalla()
            print(".:: agregar características ::.")
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.borrarPantalla() 
            print(".:: modificar caracteristicas ::.")
            peliculas.modificarcaracteristicas()
            
        case "6":
            peliculas.borrarPantalla()
            print(".:: borrar caracteristicas ::.")
            peliculas.borrarcaracteritiscas()
            
        case "7":
            opcion=False
            peliculas.borrarPantalla()    
            print("Terminaste la ejecucion del SW")
        case _:
            peliculas.borrarPantalla() 
            input("Opción invalida vuelva a intentarlo ... por favor")