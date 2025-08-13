import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_carne"
    )
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...")
    conexion = None
    cursor = None


