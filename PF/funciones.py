def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usurios():
   print("\n\t.::🤠 Sistema de Gestión de ventas La Vaquerita 🤠 ::.. \n\t1.- 📝  Registrarse  \n\t2.- 🗝️  Logear \n\t3.- 🚪  Salir ")
   opcion=input("\n\t 👉 Elige una opción: ").upper().strip() 
   return opcion

def menu_vaquerita():
   print("\n\t.:: 🛒 Menu de Ventas 🛒 ::. \n\t1.- 🥩 Comprar \n\t2.- 📋 Mostrar  \n\t3.- 🛠️  Modificar \n\t4.- ❌ Eliminar Compra \n\t5.- 🔍 Buscar \n\t5.- 🚪 SALIR """)
   opcion = input("\t\t 👉 Elige una opción: ").upper().strip()
   return opcion   

def menu_productos():
   print("\n\t.:: 🥩 Menu Productos🥩 ::. \n\t1.- Agregar \n\t2.- Mostrar productos \n\t3.- Modificar Producto \n\t4.- Eliminar Producto \n\t5.- Salir """)
   opcion = input("\t\t 👉 Elige una opción: ").upper().strip()
   return opcion   

def menu_admin():
   print("\n\t.::👨‍🔧Menu Administrador👨‍🔧 ::. \n\t1.- Gestionar Usuarios👤 \n\t2.- Gestionar Productos🥩 \n\t3.- Ver Reportes 📊 \n\t4.- Salir ")
   opcion = input("\t\t 👉 Elige una opción: ").upper().strip()
   return opcion