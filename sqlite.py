import sqlite3 as sql

#creo la base de datos

def createDB():
    conn = sql.connect("comidas.db")
    conn.commit()
    conn.close()

# creo una tabla
def createTable():
    conn = sql.connect("comidas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE comidas (
        nombre text,
        precio int,
        cantidad int
        )"""
    )
    conn.commit()
    conn.close()

#inserto una fila

def insertRow(nombre, precio, cantidad):
    conn = sql.connect("comidas.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO comidas VALUES (?, ?, ?)""",
        (nombre, precio, cantidad)
    )
    conn.commit()
    conn.close()

#extraigo los datos de la tabla

def readtRow():
    conn = sql.connect("comidas.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM comidas""",
        
    )
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)




if __name__ == "__main__":
    # createDB()
    # createTable()
    #insertRow("Lasaña", 123, 2)
    #insertRow("Pollo", 343, 3)
    readtRow()
    