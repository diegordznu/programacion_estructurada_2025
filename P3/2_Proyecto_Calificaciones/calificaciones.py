import mysql.connector
from mysql.connector import Error

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t\U0001F501 ...Oprima cualquier tecla para continuar... \U0001F501")
  input() 

def conectarDB():
  try:
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_calificaciones"   
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def menuPrincipal():
    print("\n\t\t📋 ..::: Sistema de Gestión de Calificaciones :::... 📋\n")
    print("\t\t1️⃣  Agregar Calificaciones\n\t\t2️⃣  Mostrar Calificaciones\n\t\t3️⃣  Calcular Promedio\n\t\t4️⃣  Buscar Calificaciones\n\t\t5️⃣  SALIR 🚪")
    return input("\n\t\tElige una opción: ").strip()
  
def agregarCalificaciones():
  borrarPantalla()
  conexionDB=conectarDB()
  if conexionDB!=None:
    calificaciones=[]
    print("📥 ..::Agregar Calificaciones::.. 📥")
    nombre = input("👤 Nombre del Alumno: ").upper().strip()
    # calificaciones.append({"nombre":input("Ingresa el nombre: ").upper().strip()})
    for i in range(1, 4):
      opc=True
      while opc:
        try:
            cal = float(input(f"📌 Ingrese la calificacion {i}: "))
            if 0 <= cal <= 10:
                calificaciones.append(cal)
                opc=False
            else:
                print("⚠️ Ingresa un número válido entre 0 y 10")
        except ValueError:
                print("⚠️ Ingresa un valor numérico válido")
  try:
    conexion = conectarDB()
    cursor = conexion.cursor()
    sql = "INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)"
    # val=(calificaciones['nombre'], calificaciones['cali1'], calificaciones['cali2'], calificaciones['cali3'])
    cursor.execute(sql, (nombre, *calificaciones) )
    conexion.commit()
    print("✅ Registro agregado exitosamente")
  except Error as e:
    print(f"Erros al intentar insertar un registro en la base de datos {e}")

  
def mostrarCalificaciones():
  borrarPantalla()
  conexion=conectarDB()
  cursor=conexion.cursor()
  sql=("SELECT * FROM alumnos")
  cursor.execute(sql)
  registros=cursor.fetchall()
  
  if registros:
    print("📊 .:: Mostrar Calificaciones ::. 📊\n")
    print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'cal1':<20}{'|'}{'cal2':<15}{'|'}{'cal3':<16}{'|'}")
    print(f"{'-'*120}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'}")
  else: 
    print("\t\u274C No hay calificaciones en el sistema.")  # ❌
   
def promedios():
    borrarPantalla()
    print("📈 ..:: Promedios ::.. 📈")
    conn = conectarDB()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos")
    registros = cursor.fetchall()
    if registros:
        for fila in registros:
            promedio = sum(fila[1:]) / 3
            print(f"{fila[0]} - Promedio: {promedio:.2f}")
    else:
        print("❌ No hay registros para calcular promedios")
    
def buscarCalificacion():
    borrarPantalla()
    nombre = input("🔍 Nombre del alumno a buscar: ").upper().strip()
    conn = conectarDB()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"\n👤 Alumno: {resultado[0]}\n{'-'*20}\n📘 Cal1: {resultado[1]}\n{'-'*20}\n📘 Cal2: {resultado[2]}\n{'-'*20}\n📘 Cal3: {resultado[3]}\n{'-'*20}")
    else:
        print("❌ Alumno no encontrado")
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
def borrarCalificaciones():
  borrarPantalla()
  conexion=conectarDB()
  cursor=conexion.cursor()
  sql=("SELECT * FROM alumnos where nombre=%s")
  cursor.execute(sql)
  registros=cursor.fetchall()
    
  if registros:
    print("📊 .:: Mostrar Calificaciones ::. 📊\n")
    print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'cal1':<20}{'|'}{'cal2':<15}{'|'}{'cal3':<16}{'|'}")
    print(f"{'-'*120}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'}")
    resp=input(f"Deseas borrar el registro de {nombre}? (SI/NO):  ").lower().strip()
    if resp=="si":
      sql="DELETE FROM alumnos where nombre=%s"
      val=(nombre, )
      
      
'''