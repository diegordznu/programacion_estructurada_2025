peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  peliculas.append(input("ingresa el nombre:").upper().strip())
input("\n\t\t operacion realizada con exito")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
        print(f"{i+1}: {peliculas[i]}")
    else:
     print("\t no hay peliculas en el sistmea")

def vaciarPeliculas():
  borrarPantalla()
  print("\n\t borrar o quitar todas las películas")
  resp=input("deseas quitar o borrar todas las peliculas del sistema?: (Si/No)").lower()
  if resp == "si":
    peliculas.clear()
    input("\n\t\t la operacion se realizó con exito")

def buscarPeliculas():
  borrarPantalla()
  print("\n\t buscar peliculas")
  pelicula_buscar=input("ingrese el nombre de la pelicula a buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t no se encuentra la oelicula a buscar")
  else:
    for i in range(0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"la pelicula {pelicula_buscar}si la tenemos y está en la casilla:{i}")
        encontro+=1
    if encontro>0:
        print(f"tenemos {encontro} pelicula(S) con este titulo")      
        input("\n\t\t la operacion se realizó con exito")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t borrar peliculas")
    pelicula_borrar=input("ingrese el nombre de la pelicula a borrar: ").upper().strip()
    encontrar=0
    resp="si"
    if not(pelicula_borrar in peliculas):
        print("\n\t\t no se encuentra la pelicula a buscar")
    else:
        for x in range(0,len(peliculas)):
            if pelicula_borrar==peliculas[x]:
                print=input("está seguro de eliminar la pelicula?: (si/no)")
                if resp=="si":
                    peliculas.remove(pelicula_borrar)
                print(f"se eliminó la pelicula {pelicula_borrar} se econtraba en la casilla: {x}")
            else:
                input("oprima cualquier tecla para continuar")
    


  