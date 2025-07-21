import os
import funciones_movies



movies = []
opcion = True

while opcion:
    os.system("cls")
    print("\n\t CINPOLIS" \
          "\n sistema de gestion de peliculas \n 1.- agregar \n 2.- eliminar \n 3.- actualizar \n 4.- consultar \n 5.-buscar \n 6.- vaciar \n 7.- salir")
    resp = input("elige una opcion: ")

    match resp:
        case "1":
            os.system("cls")
            print("Agregar películas")
            pelicula = input("Nombre de la película: ")
            funciones_movies.agregar(pelicula)
            input("Presiona Enter para continuar...")

        case "2":
            os.system("cls")
            print("Eliminar películas")
            pelicula = input("Nombre de la película a eliminar: ")
            if pelicula in movies:
                funciones_movies.quitar(pelicula)
                print("Película eliminada.")
            else:
                print("Película no encontrada.")
            input("Presiona Enter para continuar...")

        case "3":
            os.system("cls")
            print("Modificar lista de películas")
            vieja = input("Nombre de la película a modificar: ")
            if vieja in movies:
                nueva = input("ingrese el nuevo nombre de la pelicula: ")
                index = funciones_movies.modificar(vieja)
                movies[index] = nueva
                print("nombre actualizado.")
            else:
                print("no está.")
            input("Presiona Enter para continuar...")

        case "4":
            os.system("cls")
            print("Lista de películas:")
            for movie in movies:
                print(f"- {movie}")
            input(" Enter para continuar...")

        case "5":
            os.system("cls")
            print("Buscar una película")
            buscar = input("Nombre de la película: ")
            if buscar in movies:
                print("si está")
            else:
                print("no está.")
            input("Presiona Enter para continuar...")

        case "6":
            os.system("cls")
            funciones_movies.limpiar()
            print("Lista vaciada.")
            input("Presiona Enter para continuar...")

        case "7":
            print("Saliendo del sistema...")
            opcion = False

        case _:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")
