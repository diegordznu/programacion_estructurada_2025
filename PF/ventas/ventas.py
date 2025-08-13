"""
 Sistema informatico en consola para administración de un puesto de carne seca

"""
from conexionBD import *
import datetime


costo_carne=145.00

def borrarPantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input("\n\t\U0001F4DD Oprima cualquier tecla para continuar...")


def menuPrincipal():
    print("\n\t\t.:::\U0001F920  Sistema de Gestión de ventas de La Vaquerita \U0001F920  :::..\n\t\t 1.-\U0001F6D2 Agregar\n\t\t 2.-\U0001F4DB Eliminar\n\t\t 3.-\U0001F50D Actualizar \n\t\t 4.-\U0001F6AA Mostrar \n\t\t 5.-\U0001F50D Buscar \n\t\t 6.-\U0001F6AASalir"  )
    opcion=input("\n\t\t\U0001F50D Seleccione una opcion (1-6): ")
    return opcion

def obtener_nombre_producto(id_nuevo):
    try:
        sql = "SELECT nombre FROM productos WHERE id = %s"
        val = (id_nuevo,)
        cursor.execute(sql, val)
        resultado = cursor.fetchone()
        return resultado[0] #Aqui agarro el ID el producto seleccionado
    except:
        return []


def calcular_total(usuario_id):
    try:
        sql = """
            SELECT SUM(p.precio * v.cantidad)
            FROM ventas v
            JOIN productos p ON v.id_producto = p.id
            WHERE v.usuario_id = %s
        """
        val = (usuario_id,)
        cursor.execute(sql, val)
        resultado = cursor.fetchone()
        return resultado[0] if resultado[0] is not None else 0
    except:
        return 0


def comprar(usuario_id, id_producto, nombre_prodcuto , cantidad):
    try:
        sql="insert into ventas (usuario_id, id_producto, nombre_producto, cantidad, fecha) values (%s,%s,%s,%s,NOW())"
        val=(usuario_id, id_producto, nombre_prodcuto, cantidad)
        cursor.execute(sql,val)
        conexion.commit()

        return True
    except:
        return False


def mostrar(usuario_id):
    try:
        sql="select * from ventas where usuario_id=%s"
        val=(usuario_id,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except:
        return [] 
    

def mostrar_con_id(id):
    try:
        sql="select * from ventas where id_producto=%s"
        val=(id,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except:
        return [] 
    
    

def mostrar_productos():
    try:
        cursor.execute("select * from productos") 
        conexion.commit()
        return cursor.fetchall()
    except:
        return []  


def modificar(id, id_nuevo, cantidad):
    try:
        nombre_producto = obtener_nombre_producto(id_nuevo)
        if not nombre_producto:
            return False
        
        sql="update ventas set id_producto=%s, nombre_producto=%s, cantidad=%s, fecha=NOW() where id=%s"
        val=(id_nuevo, nombre_producto, cantidad, id)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def borrar(id):
    try:
        cursor.execute("delete from ventas where id=%s", (id,))
        conexion.commit()

        return True
    except:
        return False
    

def buscar(usuario_id):
    try:
        sql="select * from ventas where nombre_producto=%s"
        val=(usuario_id,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except:
        return []

def calcular_total_compra(id_producto, cantidad):
    try:
        sql = "SELECT precio FROM productos WHERE id = %s"
        val = (id_producto,)
        cursor.execute(sql, val)
        resultado = cursor.fetchone()
        if resultado:
            precio = resultado[0]
            return precio * cantidad
        else:
            return 0
    except:
        return 0










