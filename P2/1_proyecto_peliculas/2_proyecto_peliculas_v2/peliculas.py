peliculas=[]
pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")
  pelicula={}

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def crearPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula.update({"nombre":input ("ingresa el nombre:").upper().strip()})
  pelicula.update({"categoría":input ("ingresa la categoria:").upper().strip()})
  pelicula.update({"clasificacion":input ("ingresa la clasificacion:").upper().strip()})
  pelicula.update({"genero":input ("ingresa el genero").upper().strip()})
  pelicula.update({"idioma":input ("ingresa el idioma:").upper().strip()})
  print("\n\t\t operacion realizada con exito")

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t consultar o mostrar las peliculas")
  if len(pelicula)>0:
    for i in pelicula:
        print(f"\t {(i)} : {pelicula[i]}")
    else:
        print("\n\t no hay peliculas en el sistema")
    
def agregarcarteristicas():
  borrarPantalla()
  print("\n\t agregar característica a películas")
  atributo=input("ingrese la nueva caracteristica de la pelicula: ").lower().strip( )
  valor=input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
  pelicula[atributo]=valor
  print("\t\n la operacion fue realizada con exito")

def modificarcaracteristicas():
  borrarPantalla()
  print("Modificar caracteristicas de peliculas")
  if len(peliculas)>0:
        print("Valores actuales")
        for i in peliculas:
          print(f"{(i)} : {peliculas[i]}")
          resp = input("Desea modificar una caracteristica?(Si/No)").lower().strip()
          if resp =="si":
            peliculas.update({i: input("El nuevo valor: ").upper().strip()})
            print("La operación se ha realizado con exito")
            esperarTecla()
          borrarPantalla()
  else:
        print("No hay peliculas en el sistema")
        esperarTecla()

def borrarcaracteritiscas():
    try:
        borrarPantalla()
        print("Modificar características de películas")
        
        if len(peliculas) > 0:
            print("Valores actuales")
            for i in peliculas:
                print(f"{i} : {peliculas[i]}")
                resp = input("¿Desea modificar una característica? (Si/No) ").lower().strip()
                if resp == "si":
                    atributo = input("Escribe la característica que deseas borrar o quitar: ")
                    if atributo in peliculas[i]:
                        peliculas[i].pop(atributo)
                        print(f"Se eliminó la característica '{atributo}' correctamente.")
                    else:
                        print(f"La característica '{atributo}' no existe en la película.")
            print("\n\t La operación fue realizada con éxito ")
        else:
            print("\n\t No hay películas en el sistema ")
    except Exception as e:
        print(f"\n Ocurrió un error durante la operación: {e}")
    finally:
        esperarTecla()
        borrarPantalla()


     

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
        print(f"{i+1}: {peliculas[i]}")
    else:
     print("\t no hay peliculas en el sistmea")

  def borrarPeliculas():
    borrarPantalla()
    print("\n\t borrar o quitar todas las películas")
    resp=input("deseas quitar o borrar todas las peliculas del sistema?: (Si/No)").lower()
    if resp == "si":
      peliculas.clear()
      print("\n\t\t la operacion se realizó con exito")

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