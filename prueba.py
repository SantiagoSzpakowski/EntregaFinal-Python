import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Borrar la tabla Proyecto
cursor.execute('DROP TABLE IF EXISTS Producto')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

