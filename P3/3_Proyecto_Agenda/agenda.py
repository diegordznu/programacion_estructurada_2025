import mysql.connector
from mysql.connector import Error



def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t\U0001F501 ...Oprima cualquier tecla para continuar... \U0001F501")
  input()  
  
def menuMain():
    print("\n\t\t \U0001F4DD ..::: Sistema de Gestión de Agenda de Contactos :::... \U0001F4DD \n")
    print("\t\t \u0031\uFE0F\u20E3  Agregar Contacto \U0001F4DD\n\t\t \u0032\uFE0F\u20E3  Mostrar Todos los contactos \U0001F4BE\n\t\t \u0033\uFE0F\u20E3  Buscar contacto por nombre \U0001F50D \n\t\t \u0034\uFE0F\u20E3  Modificar contacto \U0001F50D \n\t\t \u0035\uFE0F\u20E3  Elminar contacto \U0001F50D \n\t\t \u0036\uFE0F\u20E3  SALIR \U0001F6AA")
    opcion=input("\n\t\tElige una opción (1-4): ").upper()
    return opcion

def conectarDB():
    try:
        conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_agenda"   
        )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
        

def agregar_contacto(agenda):
        borrarPantalla()
        conexionBd=conectarDB()
        if conexionBd!=None:
            print("\U0001F4DD  .:: Alta de Contactos ::. \n")  # 📝
        agenda.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
        agenda.update({"telefono":input("Ingresa el telefono: ").upper().strip()})
        agenda.update({"correo":input("Ingresa el correo: ").upper().strip()})
        ############### AGREGAR REGISTRO A LA BASE DE DATOS
        try:
            cursor=conexionBd.cursor()
            sql=(
            "INSERT INTO contactos (id, nombre, telefono, correo) VALUES (NULL, %s, %s, %s)"
                #  (
                #      pelicula["nombre"],
                #      pelicula["categoria"],
                #      pelicula["clasificacion"],
                #      pelicula["genero"],
                #      pelicula["idioma"]
                #  )
            )
            val=(agenda['nombre'], agenda['telefono'], agenda['correo'])
            
            cursor.execute(sql, val)
            conexionBd.commit()
            print("\n\t\U0001F389 ..:::: La operación se realizó con éxito :::..")  # 🎉
        except Error as e:
            print(f"Erros al intentar insertar un registro en la base de datos {e}")
        
def mostrar_contactos(agenda):
    borrarPantalla()
    conexion=conectarDB()
    
    cursor=conexion.cursor()
    sql="SELECT * FROM contactos"
    cursor.execute(sql)
    registros=cursor.fetchall()
    
    if registros:
        print("\n📄 Contactos registrados:\n")
        print(f"{'|'}{'🆔 id':<10} {'|'}{'👤 nombre':<20} {'|'}{'📞 telefono':<20}{'|'}{'📧 correo':<20}")
        print(f"{'-'*80}")
        for fila in registros:
            print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<20}")
            print(f"{'-'*80}")
    else: 
        print("\t\u274C No hay contactos en el sistema.")  # ❌


def buscar_contacto(agenda):
    borrarPantalla()
    conexion=conectarDB()
    
    cursor=conexion.cursor()
    nombre=input("Dame el nombre del contancto a buscar: ").lower().strip()
    sql="SELECT * FROM contactos where nombre=%s"
    val=(nombre, )
    cursor.execute(sql, val)
    registros=cursor.fetchall()
    if registros:
        print(f"{'|'}{'🆔 id':<10} {'|'}{'👤 nombre':<20} {'|'}{'📞 telefono':<20}{'|'}{'📧 correo':<20}")
        print(f"{'-'*80}")
        for fila in registros:
            print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<20}")
            print(f"{'-'*80}")
    else: 
        print("\t\u274C No hay contactos en el sistema.")  # ❌
    
def borrar_contacto(agenda):
    borrarPantalla()
    conexion=conectarDB()
  
    cursor= conexion.cursor()
    nombre=input("Dame el nombre del contacto a borrar: ").lower().strip()
    sql=("SELECT * FROM contactos where nombre=%s")
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
  
    if registros:
        print(f"{'|'}{'🆔 id':<10} {'|'}{'👤 nombre':<20} {'|'}{'📞 telefono':<20}{'|'}{'📧 correo':<20}")
        print(f"{'-'*80}")
        for fila in registros:
            print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<20}")
            print(f"{'-'*80}")
            
        resp=input(f"¿Deseas borrar el contacto de {nombre}? (SI/NO): ").lower().strip()
        if resp=="si":
            sql="DELETE FROM contactos WHERE nombre=%s"
            val=(nombre, )
            cursor.execute(sql, val)
            conexion.commit()
            input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
        else:
            print("\t..::La accion se canceló con exito::..")
    else: 
        print("\t\u274C Esta a eliminar no se encuentra en el sistema.")  # ❌
            
def modificar_contacto(agenda):
    borrarPantalla()
    conexion=conectarDB()
    try:  
        cursor=conexion.cursor()
        nombre=input("Dame el nombre del contacto a modificar: ").lower().strip()
        sql=("SELECT * FROM contactos where nombre=%s")
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'|'}{'🆔 id':<10} {'|'}{'👤 nombre':<20} {'|'}{'📞 telefono':<20}{'|'}{'📧 correo':<20}")
            print(f"{'-'*80}")
            for fila in registros:
                print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<20}")
                print(f"{'-'*80}")
                resp=input(f"¿Deseas actualizar el contacto de {nombre}? (SI/NO): ").lower().strip()
            if resp=="si":
                agenda["nombre"]=input("👤 Nombre: ").lower().strip()
                agenda["telefono"]=input("📞 Telefono: ").lower().strip()
                agenda["correo"]=input("📧 Correo: ").lower().strip()
                sql=" UPDATE contactos SET nombre = %s, telefono = %s, correo = %s WHERE nombre = %s"
                val=(agenda['nombre'], agenda['telefono'], agenda['correo'], nombre)
                cursor.execute(sql, val)
                conexion.commit()
                input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
            else:
                print("\t..::La accion se canceló con exito::..")
        else: 
            print("\t\u274C Esta a eliminar no se encuentra en el sistema.")  # ❌
    except Error as e:
        print(f"❌ Error al modificar: {e}")

        