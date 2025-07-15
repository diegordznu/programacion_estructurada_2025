import mysql.connector
from mysql.connector import Error

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

# pelicula={
#             "nombre":"",
#             "categoria":"",
#             "clasificacion":"",
#             "genero":"",
#             "idioma":""
#           }

pelicula={}

def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  input("\n\t\t ... ⚠ Oprima cualquier tecla para continuar ⚠ ...")

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"
      )
      return conexion
  except Error as e:
    print(f"El erro que sucedio es: {e}")
    return None



def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: \U0001F4DD Alta de Peliculas \U0001F4DD ::.\n ")
    # pelicula['nombre']=input("\U0001F4DD nombre: ").upper().strip()
    pelicula.update({"nombre":input("\U0001F4DD nombre: ").upper().strip()})
    pelicula.update({"categoria":input("\U0001F4DD categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input("\U0001F4DD clasificación: ").upper().strip()})
    pelicula.update({"genero":input("\U0001F4DD genero: ").upper().strip()})
    pelicula.update({"idioma":input("\U0001F4DD idioma: ").upper().strip()})

    ###### AGREGAR REGISTRO A LA BD
    try:
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) values (%s,%s,%s,%s,%s)"
      val=(pelicula['nombre'],pelicula['categoria'],pelicula['clasificacion'],pelicula['genero'],pelicula['idioma'])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")
    except Error as e:
      print(f"Error al intentar insertar un registro en la BD: {e}")
    
    
def mostrarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D ::.\n ")
     cursor=conexionBD.cursor()
     sql="select * from peliculas"
     cursor.execute(sql)
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
     else:
       print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.") 

def borrarPeliculas():
  borrarPantalla()
  print("\n\t.::\U0001F4DB Borrar o Quitar TODAS laS Películas \U0001F4DB ::.\n ")
  resp=input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No) ")
  if resp=="si":
    pelicula.clear()
    print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")