import getpass
import conexionBD
import funciones
import usuario.usuario as usuario
from ventas import ventas
import re
import datetime
import hashlib
def main():
    opcion=True
    while opcion:
        ventas.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRARSE":
            funciones.borrarPantalla()
            print("\n \t 👩‍💼 ..:: Registrar usuario ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #validar que el email sea correcto
            while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("\n\t⚠️ El email ingresado no es válido. Debe contener '@' y '.'")
                email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña cuidadosamente: ").strip()

            if nombre and apellidos and email and password:
                resultado=usuario.registrar(nombre,apellidos, email, password)
                if resultado:
                    print(f"\n\t🎉 {nombre} {apellidos} se registró correctamente con el email: {email}")
                else:
                    print(f"\n\t⚠️ No fue posible registrar al usuario. Puede que el email ya exista o haya otro error.")
            else:
                print(f"\n\t⚠️ Todos los campos son obligatorios. Intenta de nuevo.")
            
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGEAR": 
            funciones.borrarPantalla()
            print("\n \t 🔐 ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()

            registro = usuario.iniciar_sesion(email, password)
            if registro:
                usuario_id = registro[0]  # Obtener el ID del usuario
                if usuario_id == 1:
                    print("\n\t🔑 Acceso de administrador concedido.")
                    print(menu_admin())
                else:
                    print("\n\t🔑 Acceso de usuario concedido.")
                menu_vaquerita(registro[0], registro[1], registro[2])
            else:
                print(f"\n\t🚫 E-mail y/o contraseña incorrectas, vuelva a intentarlo...")  
                funciones.esperarTecla()  
              
        elif opcion=="3" or opcion=="SALIR": 
            print("📤 Terminó la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("\n\t🔹 Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_vaquerita(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n\t 🤠 Bienvenido {nombre} {apellidos} a La Vaquerita 🥩, has iniciado sesión ...")
        opcion=funciones.menu_vaquerita()

        if opcion == '1' or opcion=="COMPRAR":
            funciones.borrarPantalla()
            print(f"\n \t 🛒 .:: {nombre} {apellidos}, vamos a comprar un producto ::. \n")
            lista_productos=ventas.mostrar_productos()
            if len(lista_productos)>0:
                print(f"\t {'ID':<10}{'Producto':<15}{'Precio':<15}")
                print(f"\t{'-'*31}")

                for fila in lista_productos:
                    print(f"\t {fila[0]:<10}{fila[1]:<15}{fila[2]:<15}")
                print(f"\t{'-'*31}")


                id=int(input("\n\t 🔹 ID del producto a comprar: "))
                ids_disponibles = [fila[0] for fila in lista_productos]
                if id in ids_disponibles:   
                    nombre_producto = ventas.obtener_nombre_producto(id)
                    try:
                        cantidad = int(input("\t 📅 Cantidad a comprar: "))
                        sql = "SELECT precio FROM productos WHERE id = %s"
                        val = (id,)
                        cursor = conexionBD.conexion.cursor()
                        cursor.execute(sql, val)
                        resultado = cursor.fetchone()
                        if resultado:
                            precio = float(resultado[0])
                            total = precio * cantidad
                            print(f"\n\tEl total de tu compra es: ${total}")
                        else:
                            print("\n\tNo se encontró el producto seleccionado.")
                        respuesta = ventas.comprar(usuario_id, id, nombre_producto, cantidad)
                        if respuesta:
                            print(f"\n\t💰 Se compró el producto: {nombre_producto} exitosamente")
                        else:
                            ventas.borrarPantalla()
                            print(f"\n\t⚠️ No fue posible completar en este momento, vuelva a intentar... ")
                    except ValueError:
                        print("\n\t❗ La cantidad debe ser un número entero.")
                else:
                    print(f"\n\t❗ Debes ingresar un ID disponible... vuelve a intentar ")
            funciones.esperarTecla()

        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            print(f"\n \t 📄 .:: {nombre} {apellidos}, estas son tus compras ::. \n")
            lista_ventas=ventas.mostrar(usuario_id)
            if len(lista_ventas)>0:
                print(f"\t{'ID':<10}{'Producto':<15}{'Cantidad':<15}{'Fecha':<15}")
                print(f"\t{'-'*80}")
                for fila in lista_ventas:
                    print(f"\t{fila[0]:<10}{fila[3]:<15}{fila[4]:<15}{fila[5]}")
                print(f"\t{'-'*80}")

            
                exportar = input("\n\t¿Deseas exportar tus compras a PDF? (s/n): ").lower().strip()
                if exportar == "s":
                    try:
                        from fpdf import FPDF
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", size=12)
                        pdf.cell(200, 10, txt=f"Compras de {nombre} {apellidos}", ln=True, align='C')
                        pdf.ln(10)
                        pdf.cell(20, 10, "ID", 1)
                        pdf.cell(50, 10, "Producto", 1)
                        pdf.cell(30, 10, "Cantidad", 1)
                        pdf.cell(50, 10, "Fecha", 1)
                        pdf.ln()
                        for fila in lista_ventas:
                            pdf.cell(20, 10, str(fila[0]), 1)
                            pdf.cell(50, 10, str(fila[3]), 1)
                            pdf.cell(30, 10, str(fila[4]), 1)
                            pdf.cell(50, 10, str(fila[5]), 1)
                            pdf.ln()
                        nombre_archivo = f"compras_{nombre}_{apellidos}.pdf"
                        pdf.output(nombre_archivo)
                        print(f"\n\t✅ PDF generado exitosamente: {nombre_archivo}")
                    except ImportError:
                        print("\n\t❗ Debes instalar la librería fpdf: pip install fpdf")
                    except Exception as e:
                        print(f"\n\t❗ Error al generar el PDF: {e}")
            else:
                print(f"\n\t⚠️ No existen ventas para mostrar de acuerdo al usuario")

            funciones.esperarTecla()

        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t 🔄 .:: {nombre} {apellidos}, vamos a modificar una venta ::. \n")
            lista_ventas=ventas.mostrar(usuario_id)
            if len(lista_ventas)>0:
                print(f"{'ID':<10}{'Producto':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"\t{'-'*80}")

                for fila in lista_ventas:
                    print(f"\t{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"\t{'-'*80}")
                try:
                    id = int(input("\t\t🔹 ID de la venta a actualizar: "))
                    ids_disponibles = [fila[0] for fila in lista_ventas]
                    if id in ids_disponibles:
                        todos_productos=ventas.mostrar_productos()
                        if len(todos_productos)>0:
                            print(f"{'ID':<10}{'Nombre':<15}{'Precio':<15}")
                            print(f"\t{'-'*80}")

                            for fila in todos_productos:
                                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}")
                            print(f"\t{'-'*80}")

                            id_nuevo = input("\n\t🔹 ID del producto a intercambiar: ")
                            cantidad = input("\n\t📅 Cantidad a comprar: ")
                            respuesta=ventas.modificar(id, id_nuevo, cantidad)

                            if respuesta:
                                ventas.borrarPantalla()
                                print(f"\n\t🌟 Se actualizó la venta exitosamente")
                            else:
                                ventas.borrarPantalla()
                                print(f"\n\t⚠️ No fue posible completar la venta en este momento, vuelva a intentar... ")
                    else:
                        print(f"\n\t❌ El ID no coincide con los disponibles, por favor intenta de nuevo...")  

                except ValueError:
                    print("\n\t⚠️ Debes seleccionar un ID...vuelva a intentar")
            else:
                ventas.borrarPantalla()
                print(f"\n\t⚠️ No existen notas para mostrar de acuerdo al usuario... vuelva a intentar")

            funciones.esperarTecla()      

        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t 🛑 .:: {nombre} {apellidos}, vamos a cancelar una venta ::. \n")
            lista_ventas=ventas.mostrar(usuario_id)
            if len(lista_ventas)>0:
                print("\n\t 📃 Ventas realizadas")
                print(f"{'ID':<10}{'Producto':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"\t{'-'*80}")

                for fila in lista_ventas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                print(f"\t{'-'*80}")
                try:

                    id=int((input("\n\t🔹 ID de la nota a eliminar: ")))
                    ids_disponibles=[fila[0] for fila in lista_ventas]

                    if id in ids_disponibles:
                        respuesta=ventas.borrar(id)
                        if respuesta:
                            print(f"\n\t📍 Se borró la compra: {id} exitosamente")
                        else:
                            print(f"\n\t⚠️ No fue posible borrar la venta en este momento, vuelva a intentar... ")
                    else:
                        print(f"\n\t❌ El ID no está disponible, seleccione uno de la tabla...")

                except ValueError:
                    print("\n\t⚠️ Debes seleccionar un ID...vuelva a intentar")
            else:
                ventas.borrarPantalla()
                print(f"\n\t⚠️ No existen notas para mostrar de acuerdo al usuario")   

            funciones.esperarTecla()

        elif opcion == '5' or opcion=="BUSCAR":
            funciones.borrarPantalla()
            print(f"\n \t 🧾 .:: {nombre} {apellidos}, estas son tus compras ::. \n")
            lista_productos=ventas.mostrar_productos()
            if len(lista_productos)>0:
                print("\t\t💵 Ventas")
                print(f"{'ID':<10}{'Producto':<15}{'Precio':<15}")
                print(f"\t{'-'*80}")

                for fila in lista_productos:
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}")
                print(f"\t{'-'*80}")

                try:
                    id = int(input("\n\t🔍 ID del producto a buscar en ventas: "))
                    ids_disponibles = [fila[0] for fila in lista_productos]
                    if id in ids_disponibles:
                        buscar_ventas=ventas.mostrar_con_id(id)
                        if len(buscar_ventas)>0:
                            ventas.borrarPantalla()
                            print(f"\n \t 🌟 .:: {nombre} {apellidos}, Estas son tus compras de '{fila[1]}' ::. \n")
                            print(f"{'ID de producto':<20}{'Nombre':<20}{'cantidad':<15}{'fecha ':<15}")
                            print(f"\t{'-'*80}")

                            for fila in buscar_ventas:
                                print(f"{fila[2]:<20}{fila[3]:<20}{fila[4]:<15}{fila[5]}")
                            print(f"\t{'-'*80}")
                    else:
                        print(f"\n\t❌ Ningún producto disponible con el ID {id}... vuelva a intentar")    

                except ValueError:
                    print("\n\t⚠️ Debes seleccionar un ID...vuelva a intentar")

            else:
                ventas.borrarPantalla()
                print(f"\n\t⚠️ No existen productos para mostrar de acuerdo al usuario")

            funciones.esperarTecla()

        elif opcion == '6' or opcion=="SALIR":
            break

        else:
            print("\n\t❗ Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

def menu_admin():
    while True:
        funciones.borrarPantalla()
        print(f"\n\t🛠️ Menú de Administrador")
        print(f"\n\t1.-👤 Gestionar usuarios")
        print(f"\t2.- 🥩 Gestionar productos")
        print(f"\t3.- 🗑️ Eliminar Venta por ID")
        print(f"\t4.- 🔍 Buscar Venta por ID")
        print(f"\t5.- 🚪 Salir")




        opcion = input("\n\tSelecciona una opción: ")

        if opcion == '1':
            funciones.borrarPantalla()
            print(f"\n\t👤 Gestión de Usuarios")
            conexion=conexionBD.conexion
            cursor=conexion.cursor()
            sql="SELECT * FROM usuarios"
            cursor.execute(sql)
            usuarios=cursor.fetchall()

            if usuarios:
                print("\n📄 Usuarios registrados:\n")
                print(f"{'|'}{'🆔 id':<10} {'|'}{'👤 nombre':<20} {'|'}{'👤 apellidos':<20}{'|'}{'📧 email':<20}{'|'}{'🕒 fecha':<20}")
                print(f"{'-'*80}")
                for fila in usuarios:
                    fecha = fila[5]
                    if hasattr(fecha, "strftime"):
                        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        fecha_str = str(fecha)
                    print(f"{'|'}{fila[0]:<10}{'|'} {fila[1]:<20}{'|'} {fila[2]:<20}{'|'} {fila[3]:<20}{'|'} {fecha_str:<20}")
                    print(f"{'-'*80}")
            else: 
                print("\t\u274C No hay usuarios en el sistema.")  # ❌

            accion=input("\n\tSelecciona la acción que desees realizar (Agregar/Modificar/Eliminar/Salir): ").lower().strip()

            if accion == 'agregar':
                nombre = input("\n\tIntroduce el nombre del nuevo usuario: ")
                apellidos = input("\n\tIntroduce los apellidos del nuevo usuario: ")
                email = input("\n\tIntroduce el email del nuevo usuario: ")
                password = input("\n\tIntroduce la contraseña del nuevo usuario: ")
                password=hashlib.sha256(password.encode()).hexdigest()
                fecha = fecha=datetime.datetime.now()
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (nombre, apellidos, email, password, fecha))
                conexion.commit()
                print("\n\t✅ Usuario agregado exitosamente.")
            elif accion == 'modificar':
                id_usuario = input("\n\tIntroduce el ID del usuario a modificar: ")
                nombre = input("\n\tIntroduce el nuevo nombre del usuario: ")
                apellidos = input("\n\tIntroduce los nuevos apellidos del usuario: ")
                email = input("\n\tIntroduce el nuevo email del usuario: ")
                fecha = fecha=datetime.datetime.now()
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "UPDATE usuarios SET nombre = %s, apellidos = %s, email = %s, fecha = %s WHERE id = %s"
                cursor.execute(sql, (nombre, apellidos, email, fecha, id_usuario))
                conexion.commit()
                print("\n\t✅ Usuario modificado exitosamente.")
            elif accion == 'eliminar':
                id_usuario = input("\n\tIntroduce el ID del usuario a eliminar: ")
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (id_usuario,))
                conexion.commit()
                print("\n\t✅ Usuario eliminado exitosamente.")
            elif accion == 'salir':
                print("\n\t👋 Saliendo de la gestión de usuarios.")
            else:
                print("\n\t❗ Acción no válida. Intenta de nuevo.")

            funciones.esperarTecla()

        elif opcion == '2':
            funciones.borrarPantalla()
            print(f"\n\t🥩 Gestión de Productos")
            conexion=conexionBD.conexion
            cursor=conexion.cursor()
            sql="SELECT * FROM productos"
            cursor.execute(sql)
            productos=cursor.fetchall()

            if productos:
                print("\n📄 Productos registrados:\n")
                print(f"{'|'}{'🆔 id':<10} {'|'}{'🍔 nombre':<20} {'|'}{'💰 precio':<20}{'|'}{'🕒 fecha':<20}")
                print(f"{'-'*80}")
                for fila in productos:
                    fecha = fila[3]
                    if hasattr(fecha, "strftime"):
                        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        fecha_str = str(fecha)
                    print(f"{'|'}{fila[0]:<10}{'|'} {fila[1]:<20}{'|'} {fila[2]:<20}{'|'} {fecha_str:<20}")
                    print(f"{'-'*80}")
            else: 
                print("\t\u274C No hay productos en el sistema.")  # ❌

            accion=input("\n\tSelecciona la acción que desees realizar (Agregar/Modificar/Eliminar/Salir): ").lower().strip()

            if accion == 'agregar':
                nombre = input("\n\tIntroduce el nombre del nuevo producto: ")
                precio = input("\n\tIntroduce el precio del nuevo producto: ")
                fecha = fecha=datetime.datetime.now()
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "INSERT INTO productos (nombre, precio, fecha) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, precio, fecha))
                conexion.commit()
                print("\n\t✅ Producto agregado exitosamente.")
            elif accion == 'modificar':
                id_producto = input("\n\tIntroduce el ID del producto a modificar: ")
                nombre = input("\n\tIntroduce el nuevo nombre del producto: ")
                precio = input("\n\tIntroduce el nuevo precio del producto: ")
                fecha = fecha=datetime.datetime.now()
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "UPDATE productos SET nombre = %s, precio = %s, fecha = %s WHERE id = %s"
                cursor.execute(sql, (nombre, precio, fecha, id_producto))
                conexion.commit()
                print("\n\t✅ Producto modificado exitosamente.")
            elif accion == 'eliminar':
                id_producto = input("\n\tIntroduce el ID del producto a eliminar: ")
                conexion = conexionBD.conexion
                cursor = conexion.cursor()
                sql = "DELETE FROM productos WHERE id = %s"
                cursor.execute(sql, (id_producto,))
                conexion.commit()
                print("\n\t✅ Producto eliminado exitosamente.")
            elif accion == 'salir':
                print("\n\t👋 Saliendo de la gestión de productos.")
            else:
                print("\n\t❗ Acción no válida. Intenta de nuevo.")

            funciones.esperarTecla()

        elif opcion == '3':
            funciones.borrarPantalla()
            print(f"\n\t🗑️ Eliminar Venta por ID")
            conexion = conexionBD.conexion
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM ventas")
            ventas = cursor.fetchall()
            if ventas:
                print("\n📄 Ventas registradas:\n")
                print(f"{'ID':<10}{'Usuario ID':<15}{'Producto ID':<15}{'Cantidad':<10}{'Fecha':<20}")
                print(f"{'-'*70}")
                for fila in ventas:
                    fecha = fila[5]
                    if hasattr(fecha, "strftime"):
                        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        fecha_str = str(fecha)
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<10}{fecha_str:<20}")
                print(f"{'-'*70}")
                id_venta = input("\n\tIntroduce el ID de la venta a eliminar: ")
                sql = "DELETE FROM ventas WHERE id = %s"
                cursor.execute(sql, (id_venta,))
                conexion.commit()
                print("\n\t✅ Venta eliminada exitosamente.")
            else:
                print("\n\t❗ No hay ventas registradas.")
            funciones.esperarTecla()

        elif opcion == '4':
            funciones.borrarPantalla()
            print(f"\n\t🔍 Buscar Venta por ID")
            conexion = conexionBD.conexion
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM ventas")
            ventas_registradas = cursor.fetchall()
            if ventas_registradas:
                print("\n📄 Ventas registradas:\n")
                print(f"{'ID':<10}{'Usuario ID':<15}{'Producto ID':<15}{'Cantidad':<10}{'Fecha':<20}")
                print(f"{'-'*70}")
                for fila in ventas_registradas:
                    fecha = fila[5]
                    if hasattr(fecha, "strftime"):
                        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        fecha_str = str(fecha)
                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<10}{fecha_str:<20}")
                print(f"{'-'*70}")
                id_venta = input("\n\tIntroduce el ID de la venta a buscar: ")
                sql = "SELECT * FROM ventas WHERE id = %s"
                cursor.execute(sql, (id_venta,))
                venta = cursor.fetchone()
                if venta:
                    print("\n📄 Venta encontrada:\n")
                    print(f"{'ID':<10}{'Usuario ID':<15}{'Producto ID':<15}{'Cantidad':<10}{'Fecha':<20}")
                    print(f"{'-'*70}")
                    fecha = venta[5]
                    if hasattr(fecha, "strftime"):
                        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        fecha_str = str(fecha)
                    print(f"{venta[0]:<10}{venta[1]:<15}{venta[2]:<15}{venta[3]:<10}{fecha_str:<20}")
                    print(f"{'-'*70}")
                else:
                    print("\n\t❗ Venta no encontrada.")
            else:
                print("\n\t❗ No hay ventas registradas.")
            funciones.esperarTecla()

        elif opcion == '5':
            break

        else:
            print("\n\t❗ Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()
