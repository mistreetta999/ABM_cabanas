import sqlite3
from pathlib import Path

# Ruta al archivo SQLite usado por Django
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"

def get_connection():
    """Devuelve una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    """Ejemplo de inicialización manual de tablas (no reemplaza migraciones de Django)."""
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla simple de ejemplo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cabanas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        capacidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        disponible INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()
