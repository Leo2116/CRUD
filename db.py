import sqlite3 # Importa el módulo para trabajar con SQLite
import os      # Importa el módulo para interactuar con el sistema operativo

# --- Configuración de la base de datos SQLite ---
# Define el nombre del archivo de la base de datos.
DATABASE = 'database.db'

# Define la ruta completa al archivo de la base de datos.
# os.path.abspath(os.path.dirname(__file__)) obtiene el directorio actual del script.
# os.path.join une el directorio con el nombre del archivo de la base de datos.
DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), DATABASE)

# Función para obtener una conexión a la base de datos
def get_db_connection():
    # Establece una conexión con la base de datos SQLite.
    # Si el archivo no existe, lo crea.
    conn = sqlite3.connect(DATABASE_PATH)
    # sqlite3.Row permite acceder a las columnas por nombre (como un diccionario).
    conn.row_factory = sqlite3.Row
    return conn

# Función para inicializar la base de datos (crear la tabla si no existe)
def init_db():
    conn = get_db_connection() # Obtiene una conexión
    # Ejecuta comandos SQL para crear la tabla 'alumnos'.
    # IF NOT EXISTS asegura que la tabla solo se cree si no existe ya.
    # INTEGER PRIMARY KEY AUTOINCREMENT asegura que 'id' sea único y se incremente automáticamente.
    conn.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    ''')
    conn.commit() # Guarda los cambios en la base de datos
    conn.close() # Cierra la conexión

# Este bloque se ejecuta solo si db.py se ejecuta directamente (no es el caso normal en Flask)
# Es útil para probar la inicialización de la base de datos de forma independiente.
if __name__ == '__main__':
    print(f"Inicializando la base de datos en: {DATABASE_PATH}")
    init_db()
    print("Base de datos inicializada o ya existente.")
