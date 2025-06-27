def menu_principal():
    print("\n\t\t..::: CALIFICACIONES  :::... \n\t\t\U0001F4DD..::: Sistema de Gestión de calificaciones :::...\U0001F4DD \n\t\t\U00000031\U000020E3 Agregar Calificaciones  \n\t\t \U00000032\U000020E3 Mostrar calificaciones \n\t\t \U00000033\U000020E3 Promedio del Estudiante \n\t\t \U00000034\U000020E3 SALIR ")
    opcion=input("\t \u2705 Elige una opción: ").upper()
    return opcion


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t \u2192 Oprima cualquier tecla para continuar ...")
  input()

def agregar_calificaciones(lista):
   borrarPantalla()
   print("\U0001F4DD agregar calificaciones")
   nombre=input("\U0001F464 nombre del alumno: ").upper().strip()
   calificaciones=[]
   for i in range(1,4):
      continua=True
      while continua:
         try:
            cal=float(input(f" calificacion{i}: "))
            if cal>=0 and cal<11:
                calificaciones.append(cal)
                continua=False
            else:
                print("\n\u274C ingresa un numero valido")
         except ValueError:
            print("\n\t\u274C ingresa un valor numerico")
   lista.append([nombre]+calificaciones)
   print("\n\t\U0001F389accion realizada con exito\U0001F389")

def mostrar_calificaciones(lista):
   borrarPantalla()
   if len(lista)>0:
     print(f"{'nombre':<15}{'calif.1':<10}{'calif.2':<10}{'calif.3':<10}")
     print(f"{'-'*40}")
     for fila  in lista:
        print(f"{fila[0]:<15} -- {fila[1]:<10} -- {fila[2]:<10} -- {fila[3]:<10}")
     print(f"{'-'*40}")
     cuantos=len(lista)
     print(f"son {cuantos} almunos")
   else:
      print("\n\t \u274C no hay calificaicones registradas en el sistema")
    
def calcular_promedio(lista):
   borrarPantalla()
   print("\n\t \U0001F4DD promedio de calificaciones \U0001F4DD")
   if len(lista)>0:
      print(f"{'alumno':<15}{'promedio':<10}")
      print(f"{'-'*30}")
      for fila in lista:
         nombre=fila[0]
         promedio=sum(fila[1:])/3
         print(f"{nombre:<15}{promedio:<.2f}")
         promedio_grupal+=promedio
      print(f"{'-'*30}")
      promedio_grupal=promedio_grupal/len(lista)
      print(f"\n\t \U0001F4DD el promedio grupal es: {promedio_grupal}")
   else:
      print("\n\t \u274C no hay calificaciones en el sistema ")   
