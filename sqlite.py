import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("base_de_prueba.db")

# Crear un cursor para realizar operaciones
cursor = conexion.cursor()

# CREATE TABLE
def create_table():
    tables = [
    """CREATE TABLE IF NOT EXISTS base_ventas ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER,
    local TEXT,
    producto TEXT,
    precio REAL,
    cantidad INTEGER, 
    fecha DATE
)
"""
]

    
    for table in tables:
        cursor.execute(table)

# INSERT

def insert_comprador( nombre, edad, local, producto, precio, cantidad, fecha):
    statement= "INSERT INTO base_ventas (nombre, edad, local, producto, precio, cantidad, fecha) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [nombre, edad, local, producto, precio, cantidad, fecha])
    # Hacer commit de los cambios
    conexion.commit()
    return True
    if insert_comprador == True:
        print("Comprador Agregado")
    else:
        print("No se pudo agregar el comprador")
#UPDATE
def update_comprador(id, nombre, edad, local, producto, precio, cantidad, fecha):
    statement= "UPDATE base_ventas SET nombre, = ?, nombre = ?, edad, local = ?, producto = ?, precio = ?, cantidad = ?, fecha = ? WHERE id = ?"
    cursor.execute(statement, [nombre, edad, local, producto, precio, cantidad, fecha, id])
    conexion.commit()
    return True
    if update_comprador == True:
        print("Comprador Actualizado")
    else:
        print("No se pudo actualizar el comprador")
    
#DELETE
def delete_comprador(id):
    statement= "DELETE FROM base_ventas WHERE id = ?"
    cursor.execute(statement, [id])
    conexion.commit()
    return True
    if delete_comprador == True:
        print("Comprador eliminado")
    else:
        print("No se pudo eliminar el comprador")

#GET BY ID
def get_comprador_by_id(id):
    statement = "SELECT id, nombre, edad, local, producto, precio, cantidad, fecha FROM base_ventas WHERE id = ?"
    cursor.execute(statement, [id])
    resultado_id = cursor.fetchone()
    print(resultado_id)
    #SELECT todos los compradores
def get_compradores():
    query = "SELECT id, nombre, edad, local, producto, precio, cantidad, fecha FROM base_ventas"
    cursor.execute(query)
    resultado_all = cursor.fetchall()
    print(resultado_all)


