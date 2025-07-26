import mysql.connector
from mysql.connector import Error

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_nostas",
    )
    cursor=conexion.cursor(buffered=True)
except Error as e:
    print("en este momento no es posible comunicarse con el sistema, por favor intentelo más tarde...{e}")