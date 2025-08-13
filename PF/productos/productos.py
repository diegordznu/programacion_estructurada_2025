from conexionBD import *
import datetime




def agregar(nombre,precio):
    try:
        sql="insert into productos (nombre, precio, fecha) values (%s,%s,NOW())"
        val=(nombre,precio)
        cursor.execute(sql,val)
        conexion.commit()

        return True
    except:
        return False